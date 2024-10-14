# Fortune Global 500 Web Scraper

This Python script scrapes the Fortune Global 500 rankings for each year from 1995 to 2024. It extracts details like revenues, profits, assets, and more, saving the data into a structured CSV format for analysis.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)


## Features
- Scrapes Fortune Global 500 data for multiple years (1995-2024)
- Mimics human interaction with random sleep intervals
- Extracts data embedded in JSON format within the webpage (I chose this route because the webpage implements a system where only 10 rows out of 500 are available to be scraped via the 'tr' tags)
- Saves data into a CSV file for easy analysis

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/wannjala/fortune500-scraper.git
   cd fortune500-scraper
   ```

2. **Install dependencies**:
   Install the required Python packages listed in `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script**:
   ```bash
   python scraper.py
   ```

Make sure you have Python 3.x installed on your machine.

## Usage

Run the script to scrape data for multiple years:
```bash
python scraper.py
```

