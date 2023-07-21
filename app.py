from flask import Flask
from flask_restful import Api
import os
from config.settings import PORT, BACKEND_HOST, CORS_ALLOWED_ORIGINS
from init_urls import initialize_api_routes
from flask_cors import CORS, cross_origin
from utils.shared import make_json_response


app = Flask(__name__)

"""setting CORS"""
CORS(app, resource={r"/*": {"origins": CORS_ALLOWED_ORIGINS}})
app.config["CORS_HEADERS"] = "Content-Type"

"""Config setup"""
app.config.from_pyfile("config" + os.path.sep + "settings.py")
api = Api(app)


@app.errorhandler(Exception)
def all_exception_handler(error: str):
    """
        Exception handler method

        - Common exception handler to handle exceptions and raise the error.

        Parameter
        ----------
            error: str
                error details

    """
    error_message: str = getattr(error, "message", str(error))
    if app.config["DEBUG"]:
        return make_json_response({"error": str(error_message)}, 500)

    return make_json_response(
        {"error": "Something went wrong. Please try again later"}, 500
    )


@app.errorhandler(404)
def api_not_found(error: str):
    """
        API not found method

        - Check the API url and raise an exception if the matching URL not found.

        Parameter
        ----------
            error: str
                error details

    """
    return make_json_response(f"{'error: API does not exist. => ' + str(error)}", 404)


@app.route("/")
@cross_origin()
def app_index():
    """
        API Index method

        - Show a message to refer the document if the user uses the default route path.
    """
    return make_json_response({"index": "Please refer to document for API signatures"})


# - To intialize all API routes
initialize_api_routes(api)

if __name__ == "__main__":
    app.run(host=BACKEND_HOST, port=PORT, debug = True)
