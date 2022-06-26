import random
import json
import uuid
from constants import app_constants as const

class GetJsonData:

    def __init__(self):
        self.data_dict = dict()
        self._create_json_data()

    def _create_json_data(self):
        self.data_dict["id"] = str(uuid.uuid1())
        self.data_dict["org"] = random.choice(const.ORG_NAMES)
        self.data_dict["rating"] = random.choice(const.RATING)
        self.data_dict["opinion"] = random.choice(const.OPINION)
        self.data_dict["pros"] = random.choices(const.PROS, k=3)
        self.data_dict["cons"] = random.choices(const.CONS, k=3)

    def get_feeds(self):
        return json.dumps(self.data_dict, indent=4)

