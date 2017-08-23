class ApiError(Exception):
    '''General error from the Algorithmia API'''
    pass

class ApiInternalError(ApiError):
    '''Error representing a server error, typically a 5xx status code'''
    pass

class DataApiError(ApiError):
    '''Error returned from the Algorithmia data API'''
    pass

class AlgorithmException(ApiError):
    '''Base algorithm error exception'''
    def __init__(self, msg, code, request_id=None):
        self.msg = msg
        self.code = code
        self.request_id = request_id
    def __str__(self):
        return repr(self.value)
