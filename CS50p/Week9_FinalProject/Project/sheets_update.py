import gspread
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import json
import google_drive_ids as drive

# 'Open' google sheets to be use
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("creds/account_credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = drive.personal_sheet_id
workbook = client.open_by_key(sheet_id)

sheet = workbook.worksheet(drive.sheet_name)


def sheets_update():
    # Open quotes.json
    with open('json/quotes.json', 'r') as file:
        quotes_data = json.load(file)
    # Open block_list.json
    with open('json/block_list.json', 'r') as fil:
        block_list = json.load(fil)
    # Open green_list.json
    with open('json/green_list.json', 'r') as fi:
        green_list = json.load(fi)
    # Open images_urls.json
    with open('json/images_urls.json', 'r') as f:
        url_list = json.load(f)

    # Append the quotes data
    append_quotes_data(quotes_data)

    # Append the block list, green lists and url list
    update_block_list(block_list)
    update_green_list(green_list)
    update_url_list(url_list)


def append_quotes_data(quotes_data):
    # Get the column numbers of the authors and quotes
    author_col = sheet.find("authors").col

    # Get table range
    column = chr(author_col + 64) + '1'
    table_range = column + ":" + column

    # Create a list of lists to update with authors and quotes
    values = [[author, '', quote] for quote, author in quotes_data.items()]

    # Update the range of cells
    sheet.append_rows(values=values, table_range=table_range)


def update_block_list(block_list):
    block_list.sort()
    # Get table range
    column = sheet.find("block list").col
    start_cell = chr(column + 64) + '2'
    end_cell = chr(column + 64) + str(len(block_list) + 2)
    table_range = start_cell + ":" + end_cell

    # Update column
    sheet.update(range_name=table_range, values=block_list)


def update_green_list(green_list):
    green_list.sort()
    # Get table range
    column = sheet.find("green list").col
    start_cell = chr(column + 64) + '2'
    end_cell = chr(column + 64) + str(len(green_list) + 2)
    table_range = start_cell + ":" + end_cell

    # Update the range of cells
    sheet.update(range_name=table_range, values=green_list)


def update_url_list(url_list):
    url_list.sort()
    # Get table range
    column = sheet.find("url").col
    start_cell = chr(column + 64) + '2'
    end_cell = chr(column + 64) + str(len(url_list) + 2)
    table_range = start_cell + ":" + end_cell

    # Update the range of cells
    sheet.update(range_name=table_range, values=url_list)


'''
    Helper functions for get_files.py
'''
def get_block_list():
    block_col = sheet.find("block list").col
    block_list = sheet.col_values(block_col)[1:]
    return block_list


def get_green_list():
    green_col = sheet.find("green list").col
    green_list = sheet.col_values(green_col)[1:]
    return green_list



'''
    Helper functions for img_upload.py
'''
def get_images_url():
    url_col = sheet.find("url").col
    url_list = sheet.col_values(url_col)[1:]
    return url_list


if __name__ == "__main__":
    sheets_update()
