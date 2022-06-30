import random
import uuid
import json
import os
from constants import app_constants as const
from utils.custom_exceptions import FileMissingError, GenericError, DataMissingError
from utils.util_logger import Logger


class FeedbackOperations:

    def __init__(self):
        self.data_dict = dict()
    

    def _create_feedback(self):
        ''' Construct random json data'''

        self.data_dict["id"] = str(uuid.uuid1())
        self.data_dict["org"] = random.choice(const.ORG_NAMES)
        self.data_dict["rating"] = random.choice(const.RATING)
        self.data_dict["opinion"] = random.choice(const.OPINION)
        self.data_dict["pros"] = random.sample(const.PROS, 3)
        self.data_dict["cons"] = random.sample(const.CONS, 3)

        Logger.info(f"Created data: {self.data_dict}")
        return self.data_dict

    def store_feedback(self):
        try:
            Logger.info("Initiating data storage...")
            self._create_feedback()
            with open(const.FILE_PATH, 'a') as f:
                f.write(json.dumps(self.data_dict))
                Logger.info("Added data successfully")
                return const.FEEDBACK_ADDED

        except FileNotFoundError as ex:
            Logger.error(f"Error seen is : {str(ex)}")
            raise FileMissingError(const.FILE_MISS_ERROR_MSG)
            
        except Exception as ex:
            Logger.error(f"Error seen is : {str(ex)}")
            raise GenericError(const.UNEXPECTED_ERROR)
    
    def get_feedback(self):
        ''' This method aims to get data from the file'''

        try:
            with open(const.FILE_PATH, 'r') as f:
                data = f.read()                
                if not data:
                    raise DataMissingError(const.EMPTY_DATA)                
                Logger.info(f"Data retrieved successfully: \t {data}")
                return data

        except FileNotFoundError as ex:
            Logger.error(f"Error seen is : {str(ex)}")
            raise FileMissingError(const.FILE_MISS_ERROR_MSG)

        except Exception as ex:
            Logger.error(f"Error seen is : {str(ex)}")
            raise GenericError(const.UNEXPECTED_ERROR)
