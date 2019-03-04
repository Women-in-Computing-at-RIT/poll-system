"""
File::tokens.py
Author::Kevin.P.Barnett
Date::Feb.25.2019
"""

from jwt import (
    encode,
    decode,
    ExpiredSignatureError,
    InvalidSignatureError
)
from os import environ
from datetime import datetime, timedelta


def generate_token_with_claims(claims):
    claims['iss'] = 'polls.wic.rit.edu'
    claims['iat'] = datetime.utcnow()
    claims['exp'] = datetime.utcnow() + timedelta(days=31)

    return encode(claims, environ['POLLS_SECRET'], algorithm='HS256')


def validate_token(func):
    def decorator(token):
        try:
            decode(token, environ['POLLS_SECRET'], algorithms=['HS256'])
            func()
        except ExpiredSignatureError:
            print('Token Expired')
        except InvalidSignatureError:
            print('Token Modified')

    return decorator
