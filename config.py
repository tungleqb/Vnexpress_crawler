# Configuration settings for the scraper

# Request headers to mimic a real browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
}

# Base URL for scraping
BASE_URL = 'https://vnexpress.net/the-gioi'

# Ad patterns in VnExpress
AD_PATTERNS = [
    'class="banner"',
    'class="ads"',
    'class="advertisement"',
    'class="sponsor"',
    'class="branded-content"',
]

# Maximum retries for failed requests
MAX_RETRIES = 3

# Request timeout in seconds
TIMEOUT = 10

# Excel output settings
EXCEL_SETTINGS = {
    'filename': 'vnexpress_articles.xlsx',
    'sheet_name': 'Articles',
    'columns': ['ID', 'URL', 'Title']  # Removed timestamp from columns
}