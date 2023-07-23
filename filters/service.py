__all__ = ["GetBrochureDataService"]

from typing import List
from utils.shared import read_file
from math import ceil


class GetBrochureDataService:
    @classmethod
    def filter_prepare_data(cls, file: str, request_body: dict) -> List:
        """
        This method reads the file, parse the data , filter the data and caluclate all the KPI's.

        Parameters
        ----------
            file: str
                file path
            request_body: dict
                validated request body dictionary

        Returns
        -------
            filterd_data :list
                returns the dictionaries filtered parameter based data

        """
        # outcomes_calculated_data: dict = {}
        # todo : Need to fix below when key not found using default dict
        
        parsed_json_data = read_file(file)
        parsed_list_data = dict(parsed_json_data)["brochures"]
        
        _lat_lng_filtered_data = list(filter(lambda x: (x["location"]["lat"] == request_body["lat"] and x["location"]["long"] == request_body["lng"]),parsed_list_data))
        
        if request_body["publisher_id"]:
            _lat_lng_filtered_data = list(
                filter(
                    lambda x: (x["publisher"]["id"] == request_body["publisher_id"]),
                    _lat_lng_filtered_data,
                )
            )
        
        if request_body["query"]:
            query = request_body["query"]
            _lat_lng_filtered_data = list(
                filter(
                    lambda x: (x["title"] == query or x["publisher"]["name"] == query),
                    _lat_lng_filtered_data,
                )
            )

        return _lat_lng_filtered_data
    
    @classmethod
    def calculate_paginated_data(cls, data: list, request_body: dict) -> dict:
        """
        This method takes full data and provide paginated data from actual.

        Parameters
        ----------
            file: str
                file path
            request_body: dict
                request body dictionary

        Returns
        -------
            filterd_data :list, overall_data : dict
                returns the dictionaries selected_school_data, overall_data

        """
        # outcomes_calculated_data: dict = {}
        # todo : Need to fix below when key not found using default dict
        # import pdb
        # pdb.set_trace()
        page = int(request_body["page"])
        size = int(request_body["size"])
        offset = size * (page - 1)
        limit = size * page


        paginated_data = {
            "page": {
                "size": size,
                "totalElements": len(data),
                "totalPages": ceil(len(data) / size),
                "number": page,
            }
        }
        final_data = {"_embedded": {"brochures": data[offset : offset + limit]}}

        final_dictionary ={**paginated_data, **final_data}
        
        return final_dictionary
