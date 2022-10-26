from asyncio import constants
from datetime import datetime
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


speedColors = [
    '#fa6e6e',
    '#fa9b45',
    '#fbf01c',
    '#88ed02',
    '#13c600',
    '#00ba73',
    '#00a9d1',
    '#0093ff',
    '#0071ff',
    '#1800ff',
]


def getSpeedColor(speed):
    speedIndex = int(speed / 10)
    if (speedIndex >= len(speedColors)):
        speedIndex = len(speedColors)
    return speedColors[speedIndex]


def getSpeed(properties):

    for key, value in properties.items():
        lowerKey = key.lower()
        if('speed' in lowerKey):
            return value
    return 0


def rawGPStoGEOJSON(rawGPS):
    GPSElementList = rawGPS['features']
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    geojson = {
        "type": "FeatureCollection",
        "dataName": 'Selected-Trip',
        "dateTime": date_time,
        "dataType": "Point",
        "features": []
    }

    for gpsElement in GPSElementList:
        properties = gpsElement["properties"]

        properties['Id'] = uuid4()
        properties['Item'] = 'Driving Point'
        properties['Count'] = 1
        properties['Color'] = getSpeedColor(getSpeed(properties))

        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": gpsElement['geometry']['coordinates']
            },
            "properties": properties}

        geojson['features'].append(feature)

    return geojson
