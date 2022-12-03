import gdown
import re
import os
import json
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('API_KEY')

def get_file_id_from_raw_url(raw_url):
    try:
        result = re.search('https://drive.google.com/file/d/(.*)', raw_url)
        file_id = re.sub('/view\?usp=sharing', '', result.group(1))
        return file_id
    except Exception as e:
        print(f"An error occurred while getting the file ID from the raw URL: {e}")

# * String the id from the original link and add it to the new system
def download_drive_file(raw_url, save_path_url):
    try:
        file_id = get_file_id_from_raw_url(raw_url)
        clean_url = f'https://www.googleapis.com/drive/v3/files/{file_id}?alt=media&key={API_KEY}'
        gdown.download(clean_url, save_path_url, quiet=False)
        return file_id
    except Exception as e:
        print(f"An error occurred while downloading the file from Google Drive: {e}")

def get_raw_geojson_from_file(save_path_url):
    """load the geojson data from the coordinates file downloaded from google drive.
    Args:
        save_path_url string: the path of the saved coordinates file taken from google drive

    Returns:
        geojson: json data formated with geojson data types and feature arrays
    """
    try:
        f = open(save_path_url)
        raw_geojson_data = json.load(f)
        return raw_geojson_data
    except Exception as e:
        print(f"An error occurred while getting the raw GeoJSON from the file: {e}")
