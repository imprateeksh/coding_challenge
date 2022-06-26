''' Created custom exceptions needed in case of failures'''


class FileMissingError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)

class GenericError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)

class DataMissingError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)