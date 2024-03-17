# import helper programs
from get_files import get_files, get_previous_ending_page, save_ending_page
from make_pic import make_pic
from sheets_update import sheets_update
from img_upload import upload_image

images_folder = 'images'

def main():
    previous_ending_page = get_previous_ending_page()

    # Get the page range
    starting_page, ending_page = get_inputs()
    save_ending_page(ending_page)

    # Get the JSON files
    #   json/block_list.json, json/green_list.json, json/images_urls.json and json/quotes.json
    get_files(starting_page, ending_page)

    # Info on how to best arrange quote split
    info_quote_split()

    # Create and image from every quote(key) in json/quotes.json
    make_pic()

    # Upload images to google drive
    upload_image(images_folder)

    # update google sheets with:
    #   block list, green list, url, authors and quotes columns
    sheets_update()


def info_quote_split():
    print('\nAll the files have been exported.\n')
    print('In "quotes.json" from "json" folder, the quotes will be split by the following chars:')
    print('     ,  .  :  ;\n')
    print('And "%", this one is mainly use for spliting manualy.')
    print('In other words, place a "%" anywhere you would like your quote to be splited.\n')
    input('When you happy with your quotes, just type anything (at all) in the terminal: ')


def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass

def get_inputs():
    starting_page = get_valid_input("Starting page: ")

    while True:
        try:
            ending_page = get_valid_input("Ending page (inclusive): ")
            if ending_page > starting_page:
                return starting_page, ending_page
            else:
                print("Ending page must be greater than starting page.")
        except ValueError as e:
            pass


if __name__ == "__main__":
    main()
