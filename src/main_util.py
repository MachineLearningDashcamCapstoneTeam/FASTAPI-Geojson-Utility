from asyncio import constants
import logging
import os
from uuid import uuid4


def checkIfFolderExistsAndCreateIfNot(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def deleteFileIfItExists(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def deleteAllFilesInFolder(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            logging.error(e)

def deleteAllFoldersInFolder(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        try:
            if os.path.isdir(file_path):
                os.rmdir(file_path)
        except Exception as e:
            logging.error(e)
