
# app/dispatches/types.py

from typing import TypedDict, Type, Callable


class Dispatch(TypedDict):
    # Core parts
    action : str
    handler : Callable
    # For documentation
    name : str
    description : str
    # For validation and serialization(Docs too)
    request_model : Type[TypedDict]
    response_model : Type[TypedDict]