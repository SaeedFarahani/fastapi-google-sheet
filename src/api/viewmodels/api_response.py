from ttutils.TTLogging import tt_logger


class APIResponse:
    def __init__(self):
        self.status = True
        self.data = {}
        self.message = ""
        self.code = ""

    def set_status(self, status: bool):
        if self.status:
            self.status = status
        return self

    def add_message(self, message: str):
        if self.message == "":
            self.message = message
        else:
            self.message += " " + message
        return self

    def set_data(self, data):
        self.data = data
        return self

    def add_data(self, key, value):
        if self.data is None:
            self.data = {}
        self.data[key] = value
        return self

    def get_data(self, key):
        if self.data is not None and key in self.data:
            return self.data[key]
        return None

    def add_data_dict(self, data: dict):
        if data is None:
            return self
        for key, value in data.items():
            self.data[key] = value
        return self

    def __repr__(self):
        return f"status:{self.status},message:{self.message},code:{self.code},data:{self.data}"

    def __str__(self):
        return f"status:{self.status},message:{self.message},code:{self.code},data:{self.data}"

    def log(self):
        tt_logger.info(self)
        return self

    def set_response(self, status, message, code, data):
        self.status = status
        self.message = message
        self.add_data_dict(data)
        self.code = code
        return self


def check_error_in_response(response):
    if type(response) is ContractResponse and not response.status:
        return True
    return False


class ContractResponse(APIResponse):

    def set_ok(self):
        return self.set_response(True, "mission accomplished", "s200", None)

    def set_error(self):
        return self.set_response(False, "Error in operation", "e400", None)

