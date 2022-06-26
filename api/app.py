from flask import Flask, jsonify, make_response
from utils.util_data import FeedbackOperations
from constants import app_constants as const
from constants.app_constants import StatusCodes
from utils.custom_exceptions import FileMissingError, DataMissingError

app = Flask(__name__)

@app.route(const.HEALTH)
def health_status():
    ''' Get API health, can be used to check liveness/readiness of pod'''

    return make_response(jsonify(status = const.UP), StatusCodes.SUCCESS.value)

@app.route(const.API_FEEDBACK, methods = ["GET"])
def get_data():
    ''' Method to fetch data stored '''

    try:
        obj = FeedbackOperations()
        response = obj.get_feedback()
        return make_response(jsonify(data = response), StatusCodes.SUCCESS.value)
            
    except FileMissingError as ex:
        return make_response(jsonify(status = str(ex)), StatusCodes.NOT_FOUND.value)
    except DataMissingError as ex:
        return make_response(jsonify(status = str(ex)), StatusCodes.UNEXPECTED.value)
    except Exception as ex:
        print(const.GENERIC_ERROR.format(action="fetch", err = ex))
        return make_response(jsonify(status = const.GENERIC_RESPONSE_MESSAGE.format(ops="fetch")), StatusCodes.SERVER_ERROR.value)
            

@app.route(const.API_FEEDBACK, methods = ["POST"])
def store_data():
    ''' Method to store data '''
    try:        
        objdata = FeedbackOperations()
        resp = objdata.store_feedback()
        return make_response(jsonify(status = resp), StatusCodes.CREATED.value)
    except FileMissingError as ex:
        return make_response(jsonify(status = str(ex)), StatusCodes.NOT_FOUND.value)
    except Exception as ex:
        # print(const.GENERIC_ERROR.format(action="store", err = ex))
        return make_response(jsonify(status = const.GENERIC_RESPONSE_MESSAGE.format(ops="store")), StatusCodes.SERVER_ERROR.value)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=6000,
        debug=True
        )