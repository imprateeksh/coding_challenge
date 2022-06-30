''' This file holds the constants used in this project '''

#-------------- CONSTRUCTING JSON DATA CONSTANTS --------------

ORG_NAMES = ('ABC', 'MyTech', 'OrgONE', 'InterNetworks')
RATING = ('3/5', '4.5/5', '4/5', '3.5/5')
OPINION = ('POSITIVE', 'NEGATIVE', 'NEUTRAL')
PROS = ['Good work culture', 'Improvement Opportunities', 'Clear Vision', 'Nice Food', 'Co-operative Staff']
CONS = ['Not a healthy work environment', 'Less pay', 'No Learning opportunities', 'Micro management', 'No planning']

#-------------- ENDPOINT SPECIFIC INFORMATION --------------
UP = "UP"
HEALTH = "/health"
API_POST = "/feedback"
API_GET = "/results"

#-------------- OTHER CONSTANTS --------------
FILE_PATH = '/src/api/data/feeds.json'
LOG_PATH = '/src/api/logs'

LOG_FORMATTER = "[%(asctime)s] [%(levelname)s] [%(funcName)s:%(lineno)d ]: %(message)s"
#-------------- STATUS CODES -----------
from enum import Enum
class StatusCodes(Enum):
    SUCCESS = 200
    CREATED = 201
    NOT_FOUND = 404
    UNEXPECTED = 409
    SERVER_ERROR = 500


#-------------- MESSAGES --------------    
GENERIC_ERROR = "Unable to {action} data. Error received \n : {err}"
GENERIC_RESPONSE_MESSAGE = "Failed to {ops} data."
EMPTY_DATA = "Empty data.Nothing present as of now."
FEEDBACK_ADDED = "Feedback added successfully."
FILE_MISS_ERROR_MSG = "Data storage file is not present."
UNEXPECTED_ERROR = "Unexpected error occurred."