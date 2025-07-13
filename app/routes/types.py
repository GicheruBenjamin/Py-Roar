
# app/routes/types.py

from typing import TypedDict, Literal, Type, List, Callable

class Route(TypedDict):
    # Core parts
    path: str
    method : Literal['GET','POST','PUT','DELETE','PATCH']
    handler : Callable
    # For documentation
    name : str
    description : str
    # For validation and serialization(Docs too)
    request_model : Type[TypedDict]
    response_model : Type[TypedDict]
    auth_required : bool = False

