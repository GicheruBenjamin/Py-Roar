
# app/routes/routes.py

from .types import Route
from typing import List
from app.config import Log

auth_prefix = '/auth'

auth_routes:List[Route] = [
    Route(
        path = f"{auth_prefix}/login",
        method = 'POST',
        handler = lambda: Log.info('Login route hit'),
        name = 'Login',
        description = 'Login a user',
        request_model = None,
        response_model = None,
        auth_required = True
    ),
    Route(
        path = f"{auth_prefix}/register",
        method = 'POST',
        handler = lambda: Log.info('Register route hit'),
        name = 'Register',
        description = 'Register a user',
        request_model = None,
        response_model = None,
        auth_required = True
    ),
    Route(
        path = f"{auth_prefix}/logout",
        method = 'GET',
        handler = lambda: Log.info('Logout route hit'),
        name = 'Logout',
        description = 'Logout a user',
        request_model = None,
        response_model = None,
        auth_required = True
    ),
    Route(
        path = f"{auth_prefix}/me",
        method = 'GET',
        handler = lambda: Log.info('Me route hit'),
        name = 'Me',
        description = 'Get the current user',
        request_model = None,
        response_model = None,
        auth_required = True
    ),
    Route(
        path = f"{auth_prefix}/forgot-password",
        method = 'POST',
        handler = lambda: Log.info('Forgot password route hit'),
        name = 'Forgot Password',
        description = 'Forgot password',
        request_model = None,
        response_model = None,
        auth_required = True
    ),
    Route(
        path = f"{auth_prefix}/reset-password",
        method = 'POST',
        handler = lambda: Log.info('Reset password route hit'),
        name = 'Reset Password',
        description = 'Reset password',
        request_model = None,
        response_model = None,
        auth_required = True
    ),
    Route(
        path = f"{auth_prefix}/refresh-token",
        method = 'POST',
        handler = lambda: Log.info('Refresh token route hit'),
        name = 'Refresh Token',
        description = 'Refresh token',
        request_model = None,
        response_model = None,
        auth_required = True
    )
]