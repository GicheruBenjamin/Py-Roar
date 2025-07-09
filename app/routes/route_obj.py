
from typing import Callable , List
from enum import Enum

class Method(Enum):
    '''
    Enum for HTTP Methods to ensure no unpredictability
    '''
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    PATCH = 'PATCH'


class Route:
    '''
    Route object for the application.
    Shows a representation of a route.
    a path of the reource
    a description of the route {for documentation}
    a model which happens to be a class that is used to validate the request
    a method which is the HTTP method
    a handler which is the function that is called when the route is hit
    '''
    def __init__(self, path: str, descrption: str, model : Callable, method: Method, handler: Callable):
        self.path = path
        self.method = method
        self.handler = handler  
        self.description = descrption
    

class Routegroup:
    '''
    Routegroup object for the application.
    Shows a representation of a routegroup.
    a prefix of the reource
    a description of the routegroup {for documentation}
    a list of routes that are in this group
    '''
    def __init__(self, prefix: str, description: str, routes: List[Route]):
        self.prefix = prefix
        self.description = description  
        self.routes = routes



auth_routes:Routegroup =
    Routegroup(
        prefix = '/auth',
        description = 'Authentication Routes for the user',
        routes : List[Route] = [
            Route(
                path = '/login',
                description = 'Login a user',
                model = None,
                method = Method.POST,
                handler = None
            ),
            Route(
                path = '/register',
                description = 'Register a user',
                model = None,
                method = Method.POST,
                handler = None
            )
            Route(
                path = '/logout',
                description = 'Logout a user',
                model = None,
                method = Method.GET,
                handler = None
            )
            Route(
                path = '/me',
                description = 'Get the current user',
                model = None,
                method = Method.GET,
                handler = None
            )
            Route(
                path = '/forgot-password',
                description = 'Forgot password',
                model = None,
                method = Method.POST,
                handler = None
            ),
            Route(
                path = '/reset-password',
                description = 'Reset password',
                model = None,
                method = Method.POST,
                handler = None
            )
            Route(
                path = '/refresh-token',
                description = 'Refresh token',
                model = None,
                method = Method.POST,
                handler = None
            )
        ]
    )

user_routes:Routegroup =
    Routegroup(
        prefix = '/users',
        description = 'User Routes for the user',
        routes : List[Route] = [
            Route(
                path = '/',
                description = 'Get all users',
                model = None,
                method = Method.GET,
                handler = None
            ),
            Route(
                path = '/',
                description = 'Get a user',
                model = None,
                method = Method.GET,
                handler = None
            ),
            Route(
                path = '/',
                description = 'Create a user',
                model = None,
                method = Method.POST,
                handler = None
            ),
            Route(
                path = '/',
                description = 'Update a user',
                model = None,
                method = Method.PUT,
                handler = None
            ),
            Route(
                path = '/',
                description = 'Delete a user',
                model = None,
                method = Method.DELETE,
                handler = None
            )
        ]
    )

post_routes:Routegroup =
    Routegroup(
        prefix = '/posts',
        description = 'Post Routes for the user',
        routes : List[Route] = [
            Route(
                path = '/',
                description = 'Get all posts',
                model = None,
                method = Method.GET,
                handler = None
            ),
            Route(
                path = '/',
                description = 'Get a post',
                model = None,
                method = Method.GET,
                handler = None
            ),
            Route(
                path = '/',
                description = 'Create a post',
                model = None,
                method = Method.POST,
                handler = None
            ),
            Route(
                path = '/',
                description = 'Update a post',
                model = None,
                method = Method.PUT,
                handler = None
            ),
            Route(
                path = '/',
                description = 'Delete a post',
                model = None,
                method = Method.DELETE,
                handler = None
            ),
        ]
    )