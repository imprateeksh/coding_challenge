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
                'exp': datetime.utcnow() + timedelta(minutes=15)
            },
            key= const.auth_key)

    except Exception as ex:
        log.error(f"Error while creating token: \n {str(ex)}")
    finally:
        return token

def authenticate_token(func):
    ''' This method is used to authenticate API calls '''

    @wraps(func)
    def inner_func(*args, **kwargs):
        ''' Provide token in form of Auth Bearer like Authorization : Bearer abcd123'''

        header = request.headers['Authorization']
        log.info(f"Header info received: {header}")
        if not header:
            raise HeaderMissingError(const.HEADER_MISSING)
        try:
            _, token = header.split() # Bearer: Tok
            if not token:
                raise TokenMissingError(const.TOKEN_MISSING)

            val = jwt.decode(token, key = const.auth_key, algorithms = ["HS256"])

        except (HeaderMissingError,TokenMissingError) as ex:
            log.error(str(ex))
            return str(ex)

        except jwt.ExpiredSignatureError as ex:
            log.error(f"Token Expired: {str(ex)}")
            return str(ex)

        except Exception as ex:
            log.error(str(ex))
            return str(ex)

        return func(*args, **kwargs)

    return inner_func