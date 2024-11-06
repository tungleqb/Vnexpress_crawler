import requests
import pandas as pd
from bs4 import BeautifulSoup
import logging
from typing import List, Dict, Optional
import time
import trafilatura
from lxml import html

from config import HEADERS, BASE_URL, MAX_RETRIES, TIMEOUT, EXCEL_SETTINGS
from utils import setup_logging, extract_article_id, is_advertisement

class VnExpressScraper:
    def __init__(self):
        setup_logging()
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    def fetch_page(self, url: str) -> Optional[str]:
        """Fetch page content with retry logic"""
        for attempt in range(MAX_RETRIES):
            try:
                response = self.session.get(url, timeout=TIMEOUT)
                response.raise_for_status()
                return response.text
            except requests.RequestException as e:
                logging.error(f"Attempt {attempt + 1}/{MAX_RETRIES} failed: {str(e)}")
                if attempt == MAX_RETRIES - 1:
                    logging.error(f"Failed to fetch {url} after {MAX_RETRIES} attempts")
                    return None
                time.sleep(2 ** attempt)  # Exponential backoff
        return None

    def parse_articles(self, html_content: str) -> List[Dict]:
        """Parse article data from HTML content using XPath"""
        articles = []
        try:
            # Parse HTML using lxml
            tree = html.fromstring(html_content)
            
            # Find all article elements using XPath
            article_elements = tree.xpath("//article[@data-offset or @data-swap]")
            logging.info(f"Found {len(article_elements)} potential article elements")

            for article in article_elements:
                try:
                    # Extract title and URL using XPath
                    title_elements = article.xpath(".//h3/a[@title]")
                    if not title_elements:
                        logging.debug("No title element found")
                        continue

                    title_element = title_elements[0]
                    title = title_element.get('title', '').strip()
                    url = title_element.get('href', '')

                    if not title or not url:
                        logging.debug("Missing title or URL")
                        continue

                    article_id = extract_article_id(url)
                    if not article_id:
                        logging.debug(f"No valid article ID found for URL: {url}")
                        continue

                    articles.append({
                        'ID': article_id,
                        'URL': url,
                        'Title': title
                    })
                    logging.info(f"Successfully parsed article: {title}")

                except Exception as e:
                    logging.error(f"Error parsing article: {str(e)}")
                    continue

        except Exception as e:
            logging.error(f"Error parsing HTML content: {str(e)}")
        
        return articles

    def export_to_excel(self, articles: List[Dict]) -> bool:
        """Export articles to Excel file"""
        try:
            if not articles:
                logging.warning("No articles to export")
                return False
                
            df = pd.DataFrame(articles)
            
            # Update columns to exclude timestamp
            columns = ['ID', 'URL', 'Title']
            
            # Ensure proper encoding for Vietnamese characters
            with pd.ExcelWriter(
                EXCEL_SETTINGS['filename'],
                engine='openpyxl',
                mode='w'
            ) as writer:
                df.to_excel(
                    writer,
                    sheet_name=EXCEL_SETTINGS['sheet_name'],
                    index=False,
                    columns=columns
                )
            
            logging.info(f"Successfully exported {len(articles)} articles to {EXCEL_SETTINGS['filename']}")
            return True
            
        except Exception as e:
            logging.error(f"Failed to export to Excel: {str(e)}")
            return False

    def run(self):
        """Main scraping process"""
        logging.info("Starting VnExpress scraper...")
        
        html_content = self.fetch_page(BASE_URL)
        if not html_content:
            logging.error("Failed to fetch content. Exiting...")
            return

        logging.debug("Successfully fetched page content")
        articles = self.parse_articles(html_content)
        logging.info(f"Found {len(articles)} valid articles")

        if articles:
            self.export_to_excel(articles)
        else:
            logging.warning("No articles found to export")

if __name__ == "__main__":
    scraper = VnExpressScraper()
    scraper.run()
