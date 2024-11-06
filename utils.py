import logging
import os
from datetime import datetime
from typing import Dict, Optional
import re

def setup_logging() -> None:
    """Configure logging for the scraper"""
    if not os.path.exists('logs'):
        os.makedirs('logs')
        
    logging.basicConfig(
        level=logging.DEBUG,  # Changed from INFO to DEBUG
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f'logs/scraper_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
            logging.StreamHandler()
        ]
    )

def extract_article_id(url: str) -> Optional[str]:
    """Extract article ID from VnExpress URL"""
    try:
        # VnExpress URLs typically end with -post_id.html
        match = re.search(r'-(\d+)\.html$', url)
        if match:
            return match.group(1)
        return None
    except Exception as e:
        logging.error(f"Failed to extract article ID from URL {url}: {str(e)}")
        return None

def parse_timestamp(timestamp_str: str) -> Optional[str]:
    """Parse and standardize VnExpress timestamp"""
    if not timestamp_str:
        logging.debug("Empty timestamp string received")
        return None
        
    try:
        # VnExpress timestamps can be in different formats
        # Format 1: "Thứ hai, 6/11/2023, 07:28 (GMT+7)"
        # Format 2: "6/11/2023, 07:28"
        # Format 3: "Thứ 2, 06/11/2023, 07:28"
        # Format 4: "2023-11-06T07:28:00"
        
        # First try ISO format
        if 'T' in timestamp_str:
            try:
                dt = datetime.fromisoformat(timestamp_str)
                return dt.isoformat()
            except ValueError:
                pass

        # Remove GMT+7 and clean the string
        cleaned = timestamp_str.replace('(GMT+7)', '').strip()
        
        # Try to find date and time using regex
        date_pattern = r'(\d{1,2}/\d{1,2}/\d{4})'
        time_pattern = r'(\d{1,2}:\d{2}(?::\d{2})?)'
        
        date_match = re.search(date_pattern, cleaned)
        time_match = re.search(time_pattern, cleaned)
        
        if date_match and time_match:
            date_str = date_match.group(1)
            time_str = time_match.group(1)
            dt = datetime.strptime(f"{date_str} {time_str}", "%d/%m/%Y %H:%M")
            return dt.isoformat()
            
        logging.debug(f"Could not parse timestamp: {timestamp_str}")
        return None
    except Exception as e:
        logging.debug(f"Failed to parse timestamp '{timestamp_str}': {str(e)}")
        return None

def is_advertisement(article_element) -> bool:
    """Check if an article element is an advertisement"""
    from config import AD_PATTERNS
    
    if not article_element:
        return True
        
    html_str = str(article_element)
    return any(pattern in html_str for pattern in AD_PATTERNS)
