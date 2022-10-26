import gdown
import re
import os
import json

API_KEY = os.getenv('API_KEY')

#* String the id from the original link and add it to the new system
def download_drive_file(raw_url, save_path_url):
    result = re.search('https://drive.google.com/file/d/(.*)', raw_url)
    file_id = re.sub('/view\?usp=sharing', '', result.group(1))
    clean_url = f'https://www.googleapis.com/drive/v3/files/{file_id}?alt=media&key={API_KEY}' 
    gdown.download(clean_url, save_path_url, quiet=False)

def get_raw_geojson_from_file(save_path_url):
    f = open(save_path_url)
    raw_geojson_data = json.load(f)
    return raw_geojson_data;