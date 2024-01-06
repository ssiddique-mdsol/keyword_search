# Web Content Keyword Search Script

## Overview
This Python script is designed to search for specific keywords or phrases within the content of web pages. It reads a list of URLs and a list of keyword patterns from two separate text files. The script then searches for these patterns in the text content of each web page, excluding HTML tags. It assigns a priority based on the number of keywords found in each sentence and outputs the results to a CSV file.

## Features
- **Pattern Matching:** Searches for given keywords or phrases in the content of web pages.
- **Priority Assignment:** Assigns priority based on the presence of keywords.
- **Output to CSV:** Results are written to a CSV file, including URL, pattern, snippet of content, priority, and found keywords.

## Requirements
- Python 3
- Libraries: `requests`, `beautifulsoup4`

To install the required Python libraries, run:

```
pip install requests beautifulsoup4
```

## Usage
1. Prepare two text files:
   - `urls.txt`: Contains URLs to search, one per line.
   - `patterns.txt`: Contains keyword patterns, one per line. Keywords in a pattern are separated by spaces.

2. Run the script:

```
python keyword_search_script.py
```

3. The script will create an output CSV file named `output.csv`. This file will contain the following columns:
   - `URL`: The URL of the web page.
   - `Pattern`: The keyword pattern used for searching.
   - `Snippet`: A snippet of the content where the keywords were found.
   - `Priority`: Priority based on the number of keywords found (0 for all, increasing with fewer matches).
   - `Found_Keywords`: Keywords that were found in the snippet.

## Output File Format
The output is a CSV file with the following columns:
- `URL`
- `Pattern`
- `Snippet`
- `Priority`
- `Found_Keywords`

## Limitations
- The script does not perform advanced fuzzy matching. It searches for exact matches of keywords.
- The performance of the script depends on the network speed and the response time of the websites being accessed.

## License
[MIT License](LICENSE)

## Contributions
Contributions are welcome. Please open an issue or submit a pull request with your suggestions.

## Author
[Your Name]

## Acknowledgments
Thanks to all contributors who have helped in refining this script.
