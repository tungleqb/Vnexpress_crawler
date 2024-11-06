# VnExpress Web Scraper

A Python-based web scraping tool designed to extract article data from VnExpress.net. This scraper utilizes XPath for targeted data extraction and exports the collected data in both Microsoft Excel and text formats, with full support for Vietnamese character encoding.

## Features

- **Flexible Article Extraction**: 
  - Configurable XPath selectors for different page layouts
  - Support for both news articles and opinion pieces
  - Handles Vietnamese character encoding
- **Comprehensive Data Collection**: 
  - Article ID (extracted from URL)
  - URL
  - Title
  - Full article content
- **Dual Export Formats**:
  - Microsoft Excel export with professional formatting
  - Text file export with UTF-8 encoding
- **Robust Error Handling**: 
  - Comprehensive error handling and retry mechanisms
  - Automatic retry for failed requests
  - Content validation
- **Detailed Logging**: 
  - Comprehensive logging system for debugging
  - Log rotation and archival
  - Debug and info level logging options

## Requirements

- Python 3.11 or higher
- Required Python packages:
  - requests: For making HTTP requests
  - pandas: For data manipulation
  - beautifulsoup4: For HTML parsing
  - trafilatura: For content extraction
  - lxml: For XPath processing
  - openpyxl: For Excel file creation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/vnexpress-scraper.git
cd vnexpress-scraper
```

2. Install required packages:
```bash
pip install requests pandas beautifulsoup4 trafilatura lxml openpyxl
```

## Usage

### Basic Usage

Run the scraper with default settings:
```bash
python scraper.py
```

This will:
- Scrape articles from VnExpress.net homepage
- Export data to:
  - `vnexpress_articles.xlsx` (Excel format)
  - `vnexpress_articles.txt` (Text format)

### Advanced Usage

The scraper supports various command-line arguments for customization:

```bash
python scraper.py --url "https://vnexpress.net/the-gioi" \
                 --article-xpath "//article[contains(@class, 'item-news')]" \
                 --title-xpath ".//h3[@class='title-news']/a" \
                 --excel-output "world_news.xlsx" \
                 --text-output "world_news.txt"
```

### Command-line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `--url` | URL to scrape | VnExpress homepage |
| `--article-xpath` | XPath for article elements | See config.py |
| `--title-xpath` | XPath for title elements | See config.py |
| `--title-attr` | Attribute name for title | 'title' |
| `--url-attr` | Attribute name for URL | 'href' |
| `--excel-output` | Custom filename for Excel output | 'vnexpress_articles.xlsx' |
| `--text-output` | Custom filename for text output | 'vnexpress_articles.txt' |

## Configuration

The `config.py` file contains various settings that can be customized:

### Request Settings
- `HEADERS`: Browser-like headers for requests
- `MAX_RETRIES`: Maximum retry attempts (default: 3)
- `TIMEOUT`: Request timeout in seconds (default: 10)

### XPath Selectors
Default selectors in `DEFAULT_CONFIG`:
```python
{
    'article': "//article[contains(@class, 'item-news') or contains(@class, 'full-content')]",
    'title': ".//h3[@class='title-news']/a | .//h2[@class='title-news']/a",
    'title_attr': 'title',
    'url_attr': 'href'
}
```

### Export Settings
- Excel settings (EXCEL_SETTINGS):
  - Default filename
  - Sheet name
  - Column configuration
- Text settings (TEXT_SETTINGS):
  - Default filename
  - UTF-8 encoding
  - Custom separators

## Project Structure

```
vnexpress-scraper/
├── scraper.py        # Main scraper implementation
├── config.py         # Configuration settings
├── utils.py          # Utility functions
├── logs/             # Log files directory
│   └── *.log        # Rotated log files
├── README.md         # Project documentation
└── .gitignore       # Git ignore patterns
```

## Output Formats

### Excel Format (*.xlsx)
- Professional formatting with:
  - Bold headers with background color
  - Auto-adjusted column widths
  - Proper borders and alignment
  - Columns: ID, URL, Title

### Text Format (*.txt)
- UTF-8 encoded for Vietnamese support
- Clear article separation
- Includes:
  - Article metadata (ID, Title, URL)
  - Full article content
  - Formatted for readability

## Troubleshooting

### Common Issues

1. **No Articles Found**
   - Check if the URL is accessible
   - Verify XPath selectors match the page structure
   - Ensure proper network connectivity

2. **Character Encoding Issues**
   - Verify UTF-8 encoding in text output
   - Check terminal/editor supports Vietnamese characters

3. **Rate Limiting**
   - Adjust retry settings in config.py
   - Consider adding delays between requests

### Logging

Check the `logs` directory for detailed error information and debugging:
```bash
tail -f logs/scraper_YYYYMMDD_HHMMSS.log
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
