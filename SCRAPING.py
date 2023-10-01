import requests
from bs4 import BeautifulSoup
import csv

# URL of the website to scrape
url = "http://quotes.toscrape.com"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the HTML elements containing the data you want to scrape
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')

    # Create a list to store the scraped data
    scraped_data = []

    # Iterate through the quotes and authors and store them in the list
    for i in range(len(quotes)):
        quote_text = quotes[i].get_text()
        author_name = authors[i].get_text()
        scraped_data.append({'Quote': quote_text, 'Author': author_name})

    # Save the scraped data in a CSV file
    with open('scraped_quotes.csv', 'w', newline='') as csv_file:
        fieldnames = ['Quote', 'Author']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for data in scraped_data:
            writer.writerow(data)

    print("Scraped data has been saved in 'scraped_quotes.csv'")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)