import requests
from bs4 import BeautifulSoup

# Function to scrape quotes from the website
def scrape_quotes():
    url = 'http://quotes.toscrape.com/'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting quotes and authors
        quotes = soup.find_all('div', class_='quote')
        for quote in quotes:
            text = quote.find(class_='text').get_text()
            author = quote.find(class_='author').get_text()
            print(f'"{text}" - {author}')
            print()
    except Exception as e:
        print("Error scraping quotes:", e)

# Running the scraping function
if __name__ == '__main__':
    scrape_quotes()