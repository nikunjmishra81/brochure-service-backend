
from flask import request
from flask_restful import Resource

from filters import constants
from filters.service import GetBrochureDataService
from utils.shared import (check_if_file_exists, make_json_response,
                          validated_payload)


class FilteredBrochureDataAPIView(Resource):

    def get(self):
        """
            Filterd data List API View

            - To read the json file and get the list of brochure data.

        """
        
        request_body = request.args
        valid_payload = validated_payload(request_body)
        if not valid_payload:
            return make_json_response(
            {"failure_message": constants.INVALID_LATITUDE_LONGITUDE}, 500
        )
        
        
        file_path = check_if_file_exists("")
        if not isinstance(file_path, str):
            return make_json_response(
                {"failure_message": constants.BASE_FILE_ERROR}, 500
            )

        try:

            non_paginated_data = GetBrochureDataService.filter_prepare_data(file_path, valid_payload)
            paginated_data = GetBrochureDataService.calculate_paginated_data(non_paginated_data, valid_payload)

        except Exception as e:
            error_message = {
                "error_message": f"{constants.FETCH_DATA_ERROR + ' => ' + str(e)}"
            }
            return make_json_response(error_message, 500)

        return make_json_response(
            {
                "success_message": constants.FETCH_DATA_ERROR,
                "data": paginated_data,
            },
            200,
        )

