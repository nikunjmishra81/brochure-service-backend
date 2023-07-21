__all__ = ["make_json_response", "create_timestamp", "custom_logger", "read_file"]

from flask import jsonify, make_response, json
import logging, logging.handlers
import os
from typing import List, Dict
from config.settings import DUMMY_RESPONSE_FILE_PATH, DUMMY_RESPONSE_FILE_NAME
from filters import constants
from filters.constants import BASE_FILE_ERROR



def make_json_response(response: dict, statuscode: int) -> dict:
    """
        This method converts a response into json response. 
        Parameters
        ----------
            response : dict
                response in the form dictionary
            statuscode : int
                HTTP status code

        Returns
        -------
            make_response : dict
                returns a converted json response with a HTTP status code.

    """
    return make_response(jsonify(response), statuscode)


def create_timestamp():
    """
        This method creates a timestamp. 

        Returns
        -------
            datetime

    """
    import datetime

    return "{:%Y-%m-%d_%H-%M-%S}".format(datetime.datetime.now())


def custom_logger(logger_name: str, level: str = logging.INFO):
    """
        This method creates and initialize logging with different levels.

        Parameters
        ----------
            logger_name : str
                path of the logging file.
            level : str
                log level (Info, Debug, Error)

        Returns
        -------
            logging details

    """
    import sys

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    format_string: str = "%(asctime)s - [%(pathname)s - %(lineno)2s] - %(levelname)s - %(message)s"
    logger.handlers = []
    log_format = logging.Formatter(format_string)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)
    # Creating and adding the file handler
    file_handler = logging.FileHandler(logger_name, mode="a")
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)
    return logger


def check_if_file_exists(file_name: str = None) -> str:
    """
        This method check if the file exists and return.

        Returns
        -------
            file_path : str
                location of the file otherwise failure message(file doesn't exist).


    """

    file_path: str = os.path.join(DUMMY_RESPONSE_FILE_PATH, DUMMY_RESPONSE_FILE_NAME)
    if not os.path.exists(file_path):
        return make_json_response({"file_not_exist": BASE_FILE_ERROR}, 200)
    return file_path


def read_file(filename: str) -> List:
    """
        This method reads an json file having dummy data
        Parameters
        ----------
            filename : str
                Location of the input file.

        Returns
        -------
            read_xls : JSON
                Dictionary of dummy json.
    """

    file_json = json.load(open(filename))
    
    return file_json


def validated_payload(request_body: dict):
    """
        This method reads an request_body having various params and validates it
        Parameters
        ----------
            request_body : str
                

        Returns
        -------
            paylod : dict or bool
                Dictionary of dummy json.
    """
    lat = request_body.get('lat', None)
    lng = request_body.get('lng', None)
    try:
        lat = float(lat)
        lng = float(lng)
    except:
        return False
    
    publisher_ids = request_body.get('publisherIds', None)
    query = request_body.get('query', None)
    page = request_body.get('page', constants.DEFAULT_PAGE)
    size = request_body.get('size', constants.PAGE_SIZE)

    filter_query =  {
        'lat' : lat,
        'lng' : lng,
        'publisher_id' : publisher_ids,
        'query' : query,
        'page' : page,
        'size' : size,

    }

    
    
    return filter_query

