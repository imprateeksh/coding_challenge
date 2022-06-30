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

log = Logger()

def create_token():
    ''' This method generates the token required. '''
    token = ''
    try:
        id = secrets.token_urlsafe(10)
        log.info("Create token initiated.")
        token = jwt.encode(
            {
                'random_id': id, 
                'exp': datetime.utcnow() + timedelta(minutes=5)
            },
            key= const.auth_key)

    except Exception as ex:
        log.error("Error while creating token")
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
            log.error(const.HEADER_MISSING)
        except TokenMissingError:
            log.error(const.TOKEN_MISSING)
        except jwt.ExpiredSignatureError:
            log.error(const.TOKEN_EXPIRED)
            raise TokenExpiredError("Token Expired")
        except Exception:
            log.error("Error: Invalid Token value, 401")            
            raise InvalidTokenError("Invalid Token")
        return func(*args, **kwargs)
    return inner_func