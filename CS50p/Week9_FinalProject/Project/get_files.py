import requests
from bs4 import BeautifulSoup
import json
from json import JSONDecodeError
import os.path
from death import check_author
from sheets_update import get_block_list, get_green_list

# File paths to json files
quotes_json = 'json/quotes.json'
green_list_json = 'json/green_list.json'
block_list_json = 'json/block_list.json'
images_url_json = 'json/images_urls.json'

# to be used in Helper functions for main.py
previous_ending_page_path = 'data/previous_endind_page.txt'


def get_files(starting_page, ending_page):
    quote_dict = get_dict(starting_page, ending_page)
    get_quotes_json(quote_dict)


def get_dict(starting_page, ending_page):
    # Load the block and green lists from the Google sheets
    block_list = set(get_block_list())
    green_list = set(get_green_list())

    # create dict
    quote_dict = {}

    i = starting_page
    while i <= ending_page:
        # Send a request to the web page
        url = f'https://www.goodreads.com/quotes?page={i}'
        response = requests.get(url)

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the div elements with class="quote"
        quotes = soup.find_all('div', class_='quote')


        # Loop through the quotes
        for quote in quotes:
            # Find the quote text inside a span with class="quoteText"
            span = quote.find('div', class_='quoteText')
            if span is not None:
                quote_text = span.text.strip()
                quote_text = quote_text.split('―')[0].strip()
                quote_text = quote_text.replace('"', '')
            else:
                quote_text = None

            # Find the author name inside a span with class="authorOrTitle"
            author = quote.find('span', class_='authorOrTitle').text.strip().replace(',', '')
            print(author)

            # Add kei-value pairs to quote_dict
            if author not in block_list:
                if author in green_list:
                    quote_dict[quote_text.replace('"', '')] = author
                else: # Check if author is valid
                    if check_author(str(author)) == True:
                        quote_dict[quote_text.replace('"', '')] = author
                        green_list.add(author)
                    else:
                        # If the author is not valid, add them to the block list
                        block_list.add(author)

        update_block_list(block_list)
        update_green_list(green_list)

        # increment i (page)
        i = i + 1

    return quote_dict


def update_green_list(green_list):
    green_list = list(green_list)
    green_list = [[i] for i in green_list]
    # Write the list of lists in the JSON file
    with open(green_list_json, 'w') as file:
        file.truncate()
        json.dump(green_list, file, separators=(',', '\n'))


def update_block_list(block_list):
    block_list = list(block_list)
    block_list = [[i] for i in block_list]
    # Write the list of lists in the JSON file
    with open(block_list_json, 'w') as file:
        file.truncate()
        json.dump(block_list, file, separators=(',', '\n'))


def get_quotes_json(quote_dict):  # save as json
    with open(quotes_json, 'w') as f:
        json.dump(quote_dict, f, indent=4, separators=('\n,', ':\n'))


'''
    Helper function for main.py
        It will provide the ending_page variable from last time the program has run
        And update it
'''

def get_previous_ending_page():
    # Try to read the current count
    try:
        with open(previous_ending_page_path, 'r') as file:
            previous_ending_page = int(file.read().strip())
            print(f'Previous ending page: {previous_ending_page}\n')
    except FileNotFoundError:
        pass


def save_ending_page(ending_page):
    # update previous_ending_page
    previous_ending_page = ending_page

    # Write the new previous_ending_page back to the file
    with open(previous_ending_page_path, 'w') as file:
        file.write(str(previous_ending_page))

'''
    Helper function for img_upload.py
'''
def update_images_url(url_list):
    url_list = list(url_list)
    url_list = [[i] for i in url_list]
    # Write the list of lists in the JSON file
    with open(images_url_json, 'w') as file:
        file.truncate()
        json.dump(url_list, file, separators=(',', '\n'))


if __name__ == "__main__":
    get_files(5, 6)
