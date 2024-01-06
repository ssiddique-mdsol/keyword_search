import requests
import csv
from bs4 import BeautifulSoup
import re

# Read URLs from the first file
def read_urls(filename):
    with open(filename, 'r') as file:
        urls = file.read().splitlines()
    return urls

# Read patterns (keywords) from the second file
def read_patterns(filename):
    with open(filename, 'r') as file:
        patterns = file.read().splitlines()
    return patterns

# Function to split text into sentences
def split_into_sentences(text):
    sentences = re.split(r'[.!?]\s+', text)
    return sentences

# Check the occurrence of keywords in a sentence and assign priority
def check_keywords_and_assign_priority(sentence, keywords):
    found_keywords = [keyword for keyword in keywords if keyword.lower() in sentence.lower()]
    priority = len(keywords) - len(found_keywords)  # Priority based on the number of missing keywords
    return priority, found_keywords

# Search for patterns in the content of the URL
def search_patterns_in_url(url, patterns, csv_writer):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        text_content = soup.get_text(separator=' ', strip=True)
        sentences = split_into_sentences(text_content)
        for pattern in patterns:
            keywords = pattern.split()
            for sentence in sentences:
                priority, found_keywords = check_keywords_and_assign_priority(sentence, keywords)
                if found_keywords:
                    csv_writer.writerow([url, pattern, sentence, priority, ", ".join(found_keywords)])
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")

# Main function to run the script
def main(urls_file, patterns_file, output_csv_file):
    urls = read_urls(urls_file)
    patterns = read_patterns(patterns_file)
    with open(output_csv_file, 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['URL', 'Pattern', 'Snippet', 'Priority', 'Found_Keywords'])
        for url in urls:
            search_patterns_in_url(url, patterns, csv_writer)

# Example usage
if __name__ == "__main__":
    main('links.txt', 'keywords.txt', 'output.csv')