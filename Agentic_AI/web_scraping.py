import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page to scrape
# url = 'https://en.wikipedia.org/wiki/Football'
url = "https://en.wikipedia.org/wiki/Baseball"

# Send a GET request to the webpage
response = requests.get(url)

# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(response.content, 'html.parser')

# Extract all the text from the page
paragraph = soup.find_all('p')

# Print the full page text
print("All information extracted from the Wikipedia page:")
# print(page_text)

# Optionally, save the scraped content to a text file
with open('baseball_wiki.txt', 'w', encoding='utf-8') as file:
    for para in paragraph:
        file.write(para.get_text())
