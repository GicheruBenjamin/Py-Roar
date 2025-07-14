
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional, Any
from duplicity.cli_main import action


class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"

class Role(Enum):
    USER = "user"
    LEADER = "leader"
    ADMIN = "admin"

@dataclass
class Routetype:
    """
    Rest route object
    """
    # Core
    method: HttpMethod
    path : str
    handler: str
    #Docs
    name: str
    description: str
    # Validation , serialization and deserialization
    request_model: Dict[str, Any]
    response_model: Dict[str, Any]
    # Middleware
    auth_required: bool
    role : Role

@dataclass
class Dispatchtype:
    """
    Socket dispatch object
    """
    # Core
    action: str
    handler: str
    #Docs
    name: str
    description: str
    # Validation , serialization and deserialization
    request_model: Dict[str, Any]
    response_model: Dict[str, Any] = field(default_factory=dict)
    # Middleware
    auth_required: bool
    role : Role

@dataclass
class Routertype:
    """
    Allows implementation of routers
    """
    routes: List[Routetype]

@dataclass
class Dispatchertype:
    """
    Allows implementation of dispatchers
    """
    dispatches: List[Dispatchtype]

@dataclass
class Apptype:
    """
    Allows implementation of apps
    """
    router : Routertype
    dispatcher : Dispatchertype

@dataclass
class Baserequest:
    """
    Base request object
    """
    method: HttpMethod
    path_params: Dict[str, Any]
    query_params: Dict[str, Any]
    cookies: Dict[str, Any]
    headers: Dict[str, Any]
    body: Dict[str, Any]

@dataclass
class Restfulrequest(Baserequest):
    """
    Restful request object
    """
    pass

@dataclass
class Socketrequest(Baserequest):
    """
    Socket request object
    """
    pass    

@dataclass
class Baseresponse:
    """
    Base response object
    """
    status_code: int
    headers: Dict[str, Any]
    body: Dict[str, Any]

@dataclass
class Restfulresponse(Baseresponse):
    """
    Restful response object
    """
    pass

@dataclass
class Socketresponse(Baseresponse):
    """
    Socket response object
    """
    pass