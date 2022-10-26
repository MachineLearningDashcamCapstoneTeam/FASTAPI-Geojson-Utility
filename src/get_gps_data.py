
from ast import Pass
import logging
import main_util as main_util
import gdownload_util as gdownload_util

data_folder_path = 'data'
coord_save_path = f'{data_folder_path}/coord.json'


def get_gps_data_from_coords(coordinates_link=''):
    try:
        main_util.checkIfFolderExistsAndCreateIfNot(data_folder_path)
        
        #* Download the file and load the raw data
        gdownload_util.download_drive_file(
             raw_url=coordinates_link, save_path_url=coord_save_path)
        
        raw_geojson_data = gdownload_util.get_raw_geojson_from_file(
             save_path_url=coord_save_path)
       
        #* Clean the raw data and delete remaining raw data
        clean_geojson_data = main_util.rawGeojsonToCleanGeojson(
             raw_geojson_data)

        main_util.deleteAllFilesInFolder(data_folder_path)
           
        return clean_geojson_data;
    except Exception as e:
        logging.error(e)
        return 400