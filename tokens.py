"""
File::token_validation.py
Author::Kevin.P.Barnett
Date::Feb.25.2019
"""

from jwt import decode
from os import environ

def validate_token(func, token):
    def decorator():
        #Before Function
        try:
            decode(token, environ['POLLS_SECRET'], algorithms=['HS256'])
        except 

        func()

    return decorator
