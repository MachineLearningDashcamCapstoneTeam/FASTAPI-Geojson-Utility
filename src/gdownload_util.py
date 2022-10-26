import gdown
import re
import os
import json

API_KEY = os.getenv('API_KEY')

#* String the id from the original link and add it to the new system
def strip_link_from_raw_url(raw_url):
    result = re.search('https://drive.google.com/file/d/(.*)', raw_url)
    file_id = re.sub('/view\?usp=sharing', '', result.group(1))
    url = f'https://www.googleapis.com/drive/v3/files/{file_id}?alt=media&key={API_KEY}' 
    return url

