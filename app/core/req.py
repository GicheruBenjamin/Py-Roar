
# app/core/req.py
"""
This module contains the Request class.
a restful request
a socket request
"""

class Baserequest:
    def __init__(self,method,path_params,query_params,cookies,headers,body):
        self.method = method
        self.path_params = path_params
        self.query_params = query_params
        self.cookies = cookies
        self.headers = headers
        self.body = body

class Restfulrequest(Baserequest):
    def __init__(self,method,path_params,query_params,cookies,headers,body):
        super().__init__(method,path_params,query_params,cookies,headers,body)

class Socketrequest(Baserequest):
    def __init__(self,method,path_params,query_params,cookies,headers,body):
        super().__init__(method,path_params,query_params,cookies,headers,body)