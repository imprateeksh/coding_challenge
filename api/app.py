from flask import Flask, jsonify, make_response
from utils.util_data import FeedbackOperations
from constants import app_constants as const
from constants.app_constants import StatusCodes
from utils.custom_exceptions import FileMissingError, DataMissingError
from utils.util_logger import Logger as log
from utils.util_token import create_token, authenticate_token

app = Flask(__name__)

@app.route(const.API_GET_TOKEN)
def get_token():
    token = create_token()
    if not token:
        return make_response(jsonify(status = "Not able to create token"), StatusCodes.SERVER_ERROR)
    return make_response(jsonify(token = token), StatusCodes.SUCCESS)

@app.route(const.HEALTH)
def health_status():
    ''' Get API health, can be used to check liveness/readiness of pod'''

    return make_response(jsonify(status = const.UP), StatusCodes.SUCCESS.value)

@authenticate_token
@app.route(const.API_GET, methods = ["GET"])
def get_data():
    ''' Method to fetch data stored '''

    try:
        obj = FeedbackOperations()
        response = obj.get_feedback()
        return make_response(response, StatusCodes.SUCCESS.value)
            
    except FileMissingError as ex:
        log.error(ex)
        return make_response(jsonify(status = str(ex)), StatusCodes.NOT_FOUND.value)

    except DataMissingError as ex:
        log.error(ex)
        return make_response(jsonify(status = str(ex)), StatusCodes.UNEXPECTED.value)

    except Exception as ex:
        log.error(const.GENERIC_ERROR.format(action="fetch", err = ex))
        return make_response(jsonify(status = const.GENERIC_RESPONSE_MESSAGE.format(ops="fetch")), StatusCodes.SERVER_ERROR.value)
            

@authenticate_token
@app.route(const.API_POST, methods = ["POST"])
def store_data():
    ''' Method to store data '''
    try:        
        objdata = FeedbackOperations()
        resp = objdata.store_feedback()
        return make_response(jsonify(status = resp), StatusCodes.CREATED.value)
    except FileMissingError as ex:
        log.error(str(ex))
        return make_response(jsonify(status = const.FILE_MISS_ERROR_MSG), StatusCodes.NOT_FOUND.value)
    except Exception as ex:
        log.error(const.GENERIC_ERROR.format(action="store", err = ex))
        return make_response(jsonify(status = const.GENERIC_RESPONSE_MESSAGE.format(ops="store")), StatusCodes.SERVER_ERROR.value)


if __name__ == "__main__":
    app.run(
        host= const.IP,
        port=const.PORT,
        debug=const.DEBUG_VAL
        )