import random
import uuid
from constants import app_constants as const
from utils.custom_exceptions import FileMissingError, GenericError, DataMissingError
import os

# TO DO : 
# CREATE FILE IF NOT EXISTS

class FeedbackOperations:

    def __init__(self):
        self.data_dict = dict()
        self._create_filepath()
    
    def _create_filepath(self):
        if not os.path.exists(const.FILE_PATH):
            pass

    def create_feedback(self):
        ''' Construct random json data'''

        self.data_dict["id"] = str(uuid.uuid1())
        self.data_dict["org"] = random.choice(const.ORG_NAMES)
        self.data_dict["rating"] = random.choice(const.RATING)
        self.data_dict["opinion"] = random.choice(const.OPINION)
        self.data_dict["pros"] = random.choices(const.PROS, k=3)
        self.data_dict["cons"] = random.choices(const.CONS, k=3)
        return self.data_dict

    def store_feedback(self):
        try:
            with open(const.FILE_PATH, 'a') as f:
                f.write(self.data_dict)
                return const.FEEDBACK_ADDED
        except FileNotFoundError:
            raise FileMissingError(const.FILE_MISS_ERROR_MSG)
        except Exception:
            raise GenericError(const.UNEXPECTED_ERROR)
    
    def get_feedback(self):
        ''' This method aims to get data from the file'''

        try:
            with open(const.FILE_PATH, 'r') as f:
                data = f.read()            
            
            if not data:
                raise DataMissingError(const.EMPTY_DATA)
            
            return data
        
        except FileNotFoundError:
            raise FileMissingError(const.FILE_MISS_ERROR_MSG)

        except Exception:
            raise GenericError(const.UNEXPECTED_ERROR)


# o = FeedbackOperations()
# print(o.get_feedback())
# print('*' * 10)
# print(o.get_feedback())
# print('*' * 10)