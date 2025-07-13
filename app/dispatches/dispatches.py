

# app/dispatches/dispatches.py
from .types import Dispatch
from typing import List
from app.config import Log

dispatches : List[Dispatch] = [
    Dispatch(
        action =  "LIST_ROOMS",
        handler = lambda: Log.info('LIST_ROOMS dispatched'),
        name = 'List Rooms',
        description = 'List all rooms',
        request_model = None,
        response_model = None
    ),
    Dispatch(
        action =  "CREATE_ROOM",
        handler = lambda: Log.info('CREATE_ROOM dispatched'),
        name = 'Create Room',
        description = 'Create a room',
        request_model = None,
        response_model = None
    ),
    Dispatch(
        action =  "GET_ROOM",
        handler = lambda: Log.info('GET_ROOM dispatched'),
        name = 'Get Room',
        description = 'Get a room',
        request_model = None,
        response_model = None
    ),
    Dispatch(
        action =  "UPDATE_ROOM",
        handler = lambda: Log.info('UPDATE_ROOM dispatched'),
        name = 'Update Room',
        description = 'Update a room',
        request_model = None,
        response_model = None
    ),
    Dispatch(
        action =  "DELETE_ROOM",
        handler = lambda: Log.info('DELETE_ROOM dispatched'),
        name = 'Delete Room',
        description = 'Delete a room',
        request_model = None,
        response_model = None
    )
]