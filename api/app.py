from flask import Flask, jsonify, make_response
from utils.construct_data import GetJsonData
from constants import app_constants as const
from constants.app_constants import StatusCodes


app = Flask(__name__)

@app.route(const.HEALTH)
def health_status():
    ''' Get API health, can be used to check liveness/readiness of pod'''

    return make_response(jsonify(status = const.UP), StatusCodes.SUCCESS)

@app.route(const.API_FEEDBACK, methods = ["GET"])
def get_all_data():
    ''' Method to fetch data stored '''
    pass


@app.route(const.API_FEEDBACK, methods = ["POST"])
def store_data():
    ''' Method to store data '''
    try:        
        objdata = GetJsonData()
        resp = objdata.get_feeds()
        # persist data here
        return make_response(jsonify(resp), StatusCodes.CREATED)
    except Exception as e:
        pass


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=6000,
        debug=True
        )