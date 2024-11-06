# VnExpress Web Scraper

A Python-based web scraping tool designed to extract article data from VnExpress.net. This scraper utilizes XPath for targeted data extraction and exports the collected data in both Microsoft Excel and text formats.

## Features

- **Robust Article Extraction**: Uses XPath selectors to accurately parse article content
- **Data Collection**: Captures article metadata including:
  - Article ID
  - URL
  - Title
  - Full article content
- **Dual Export Formats**:
  - Microsoft Excel export with professional formatting
  - Text file export with UTF-8 encoding
- **Error Handling**: Comprehensive error handling and retry mechanisms
- **Logging**: Detailed logging system for debugging and monitoring

## Requirements

- Python 3.11 or higher
- Required Python packages:
  - requests
  - pandas
  - beautifulsoup4
  - trafilatura
  - lxml
  - openpyxl

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

1. Run the scraper:
```bash
python scraper.py
```

2. The scraper will:
   - Fetch articles from VnExpress.net
   - Parse article content and metadata
   - Export data to:
     - `vnexpress_articles.xlsx` (Excel format)
     - `vnexpress_articles.txt` (Text format)

## File Structure

```
vnexpress-scraper/
├── scraper.py        # Main scraper implementation
├── config.py         # Configuration settings
├── utils.py          # Utility functions
├── logs/             # Log files directory
├── README.md         # Project documentation
└── .gitignore       # Git ignore file
```

## Output Formats

### Excel Format
- Professional formatting with headers
- Auto-adjusted column widths
- Proper borders and alignment
- Columns: ID, URL, Title

### Text Format
- UTF-8 encoded
- Includes article metadata and content
- Clear separation between articles
- Human-readable format

## Error Handling

- Automatic retry mechanism for failed requests
- Comprehensive logging system
- Graceful handling of network issues
- Content validation

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
