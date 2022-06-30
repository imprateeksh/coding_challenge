from functools import wraps
import jwt
from datetime import datetime, timedelta
import json
# from constants.app_constants import StatusCodes
from constants import app_constants as const
from utils.custom_exceptions import TokenExpiredError, InvalidTokenError, HeaderMissingError, TokenMissingError
from utils.util_logger import Logger
import secrets
from flask import request

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
        ''' Provide token in form of Auth Bearer like Authorization : Bearer abcd123'''
        
        header = request.headers.get('Authorization')
        if not header:
            raise HeaderMissingError(const.HEADER_MISSING)
        try:
            _, token = header.split()
            if not token:
                raise TokenMissingError(const.TOKEN_MISSING)

            val = jwt.decode('token', key = const.auth_key, algorithms = ["HS256"])

        except HeaderMissingError:
            Logger.error(const.HEADER_MISSING)
        except TokenMissingError:
            Logger.error(const.TOKEN_MISSING)
        except jwt.ExpiredSignatureError:
            Logger.error(const.TOKEN_EXPIRED)
            raise TokenExpiredError("Token Expired")
        except Exception:
            Logger.error("Error: Invalid Token value, 401")            
            raise InvalidTokenError("Invalid Token")
        return func(*args, **kwargs)
    return inner_func