
# app/core/res.py
"""
This module contains the Response class.
a restful response
a socket response
"""

class Baseresponse:
    def __init__(self,status_code,headers,body):
        self.status_code = status_code
        self.headers = headers
        self.body = body

class Restfulresponse(Baseresponse):
    def __init__(self,status_code,headers,body):
        super().__init__(status_code,headers,body)

class Socketresponse(Baseresponse):
    def __init__(self,status_code,headers,body):
        super().__init__(status_code,headers,body)