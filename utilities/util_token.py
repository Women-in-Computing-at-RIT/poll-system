"""
File::util_token.py
Author::Kevin.P.Barnett
Date::Feb.25.2019
"""

from jwt import (
    encode,
    decode,
    ExpiredSignatureError,
    InvalidSignatureError
)
from flask import request
from os import environ
import json
from datetime import datetime, timedelta
from functools import wraps


def generate_token_with_claims(claims):
    claims['iss'] = 'polls.wic.rit.edu'
    claims['iat'] = datetime.utcnow()
    claims['exp'] = datetime.utcnow() + timedelta(days=31)

    return encode(claims, environ['POLLS_SECRET'], algorithm='HS256')


def validate_token(func):
    @wraps(func)
    def decorator():
        try:
            print(request.headers.get('Authorization'))
            token = request.headers.get('Authorization')
            jsonToken = decode(token, environ['POLLS_SECRET'], algorithms=['HS256'])
            return func(jsonToken)
        except TypeError as e:
            print('Token Not Found')
            print(e)
            return json.dumps({
                'msg': 'token not found'
            }), 404
        except ExpiredSignatureError:
            print('Token Expired')
            return json.dumps({
                'msg': 'token expired'
            }), 403
        except InvalidSignatureError:
            print('Token Modified')
            return json.dumps({
                'msg': 'token modified'
            }), 403

    return decorator
