from flask import Flask, jsonify, make_response
from utils.util_data import FeedbackOperations
from constants import app_constants as const
from constants.app_constants import StatusCodes
from utils.custom_exceptions import FileMissingError, DataMissingError
from utils.util_logger import Logger
from utils.util_token import create_token, authenticate_token

app = Flask(__name__)

log = Logger()

@app.route(const.API_GET_TOKEN, methods = ["GET"])
def get_token():
    token = create_token()
    # log.info(f"Token created as : {token}")
    if not token:
        log.error("Unable to create Token")
        return make_response(jsonify(status = "Not able to create token"), StatusCodes.SERVER_ERROR)
    return {"tok": token}

@app.route(const.HEALTH)
def health_status():
    ''' Get API health, can be used to check liveness/readiness of pod'''

    return make_response(jsonify(status = const.UP), StatusCodes.SUCCESS.value)


@app.route(const.API_GET, methods = ["GET"])
@authenticate_token
def get_data():
    ''' Method to fetch data stored '''

    try:
        obj = FeedbackOperations()
        response = obj.get_feedback()
        log.info("Getting data from json file")
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
            

@app.route(const.API_POST, methods = ["POST"])
@authenticate_token
def store_data():
    ''' Method to store data '''
    try:        
        objdata = FeedbackOperations()
        resp = objdata.store_feedback()
        log.info("Data stored successfully")
        return make_response(jsonify(status = resp), StatusCodes.CREATED.value)
    
    except FileMissingError as ex:
        log.error(str(ex))
        return make_response(jsonify(status = const.FILE_MISS_ERROR_MSG), StatusCodes.NOT_FOUND.value)
    
    except Exception as ex:
        log.error(const.GENERIC_ERROR.format(action="store", err = ex))
        # return make_response(jsonify(status = const.GENERIC_RESPONSE_MESSAGE.format(ops="store")), StatusCodes.SERVER_ERROR.value)
        return make_response(jsonify(status = str(ex)), StatusCodes.SERVER_ERROR.value)


if __name__ == "__main__":
    app.run(
        host= const.IP,
        port=const.PORT,
        debug=const.DEBUG_VAL
        )