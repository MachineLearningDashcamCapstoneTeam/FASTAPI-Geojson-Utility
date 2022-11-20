
from ast import Pass
import logging
import src.lib.folder_util as folder_util
import src.lib.gdownload_util as gdownload_util
import src.lib.geojson_util as geojson_util

data_folder_path = 'src/data'
coord_save_path = f'{data_folder_path}/coord.json'

def get_raw_gps_data_from_coords_file(coordinates_link=''):
    try:
        
        folder_util.checkIfFolderExistsAndCreateIfNot(data_folder_path)
        # * Download the file and load the raw data
        gdownload_util.download_drive_file(
            raw_url=coordinates_link, save_path_url=coord_save_path)
        raw_geojson_data = gdownload_util.get_raw_geojson_from_file(
            save_path_url=coord_save_path)
        folder_util.deleteAllFilesInFolder(data_folder_path)
        return raw_geojson_data
    except Exception as e:
        logging.error(e)
        return e



def get_gps_data_from_coords_file(coordinates_link=''):
    try:
        
        folder_util.checkIfFolderExistsAndCreateIfNot(data_folder_path)
        # * Download the file and load the raw data
        gdownload_util.download_drive_file(
            raw_url=coordinates_link, save_path_url=coord_save_path)
        raw_geojson_data = gdownload_util.get_raw_geojson_from_file(
            save_path_url=coord_save_path)
        # * Clean the raw data and delete remaining raw data
        clean_geojson_data = geojson_util.raw_geojson_to_clean_geojson(
            raw_geojson_data)
        folder_util.deleteAllFilesInFolder(data_folder_path)
        return clean_geojson_data
    except Exception as e:
        logging.error(e)
        return e
