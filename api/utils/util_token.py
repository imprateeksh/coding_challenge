
from http.client import HTTPException
from functools import wraps
import jwt
from datetime import datetime, timedelta
import json
from api.constants.app_constants import StatusCodes
from constants import app_constants as const
from utils.util_logger import Logger
import secrets

def create_token():
    ''' This method generates the token required. '''
    token = ''
    try:
        id = secrets.token_urlsafe(10)
        token = jwt.encode(
            {
                'random_id': id, 
                'exp': datetime.utcnow() + timedelta(minutes=5)
            },
            key= const.auth_key)

    except Exception as ex:
        Logger.error("Error while creating token")
    finally:
        return token

def authenticate_token(func):
    ''' This method is used to authenticate API calls '''

    @wraps(func)
    def inner_func(*args, **kwargs):
        ''' Provide token as query parameter like token=abcd123'''
        try:
            jwt.decode(kwargs['token'], key = const.auth_key, algorithms = ["HS256"])
        except jwt.ExpiredSignatureError:
            Logger.error("Error: Token Expired")
            raise HTTPException(status_code = StatusCodes.FORBIDDEN.value, detail = "Token Expired")
        except Exception:
            Logger.error("Error: Invalid Token value")            
            raise HTTPException(status_code = StatusCodes.UNAUTHORIZED.value, detail = "Invalid Token")
        return func(*args, **kwargs)
    return inner_func