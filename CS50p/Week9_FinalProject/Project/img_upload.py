from googleapiclient.discovery import build
from google.oauth2 import service_account
from urllib.parse import quote
import os
import google_drive_ids as drive
from sheets_update import get_images_url
from get_files import update_images_url

scopes = ['https://www.googleapis.com/auth/drive']
service_account_file = 'creds/account_credentials.json'
parent_folder_id = drive.parent_folder_id

def authenticate():
    creds = service_account.Credentials.from_service_account_file(service_account_file, scopes=scopes)
    return creds


def upload_image(folder_path):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    images_url = get_images_url()

    for image_file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, image_file)

        # Encode the image file name
        encoded_image_file = quote(image_file)

        # get names from files in folder_path from google frive
        existing_files = service.files().list(q=f"name='{encoded_image_file}'").execute()

        # Check if a file with the same name already exists
        if not existing_files.get('files'):
            file_url = upload(file_path, service)
            images_url.append(file_url)

        update_images_url(images_url)


def upload(file_path, service):
    file_metadata = {
        'name' : file_path.split('\\')[-1],
        'parents' : [parent_folder_id]
    }

    file = service.files().create(
        body = file_metadata,
        media_body = file_path
    ).execute()

    # Get the file ID and construct the URL
    file_id = file.get('id')
    file_url = f"https://drive.google.com/uc?id={file_id}"

    return file_url


if __name__ == "__main__":
    upload_image('images')
