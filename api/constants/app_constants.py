''' This file holds the constants used in this project '''

# CONSTRUCTING JSON DATA RELATED CONSTANTS

ORG_NAMES = ('ABC', 'MyTech', 'OrgONE', 'InterNetworks')
RATING = ('3/5', '4.5/5', '4/5', '3.5/5')
OPINION = ('POSITIVE', 'NEGATIVE', 'NEUTRAL')
PROS = ['Good work culture', 'Improvement Opportunities', 'Clear Vision', 'Nice Food', 'Co-operative Staff']
CONS = ['Not a healthy work environment', 'Less pay', 'No Learning opportunities', 'Micro management', 'No planning']

# ENDPOINT SPECIFIC INFORMATION
UP = "UP"
HEALTH = "/health"
API_FEEDBACK = "/feedback"
#
from enum import Enum
class StatusCodes(Enum):
    SUCCESS = 200
    CREATED = 201
    PAGE_NOT_FOUND = 404
    SERVER_ERROR = 500
    