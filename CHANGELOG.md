# Changelog

All notable changes to the Fortune 500 Global Companies Scraper project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Improved error handling for network timeouts
- Progress bar to show scraping status

### Changed
- Optimized data parsing algorithm for faster processing

### Fixed
- Issue with parsing company names containing commas

## [1.0.0] - 2024-10-14

### Added
- Initial release of Fortune 500 Global Companies Scraper
- Scraping functionality for the following data points:
  - Company name
  - Revenue
  - Profit
  - Assets
  - Global 500 status
  - Another almost 25 attributes (although some are redundant and may require removal when analysing the dataset).
- CSV output of scraped data
- README with installation and usage instructions
- Requirements file listing project dependencies

### Changed
- N/A

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- N/A

### Security
- Implemented rate limiting to respect Fortune's servers