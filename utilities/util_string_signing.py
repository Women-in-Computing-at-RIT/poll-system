"""
File::util_string_signing.py
Author::Kevin.P.Barnett
Date::Apr.21.2019
"""
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature

import base64

KEY_PATH = 'd:\\Pycharm_Project\\poll-system\\'


def generate_key_pair():
        with open(KEY_PATH+'key.pem', 'wb') as private_key_file, open(KEY_PATH+'key.pub', 'wb') as public_key_file:
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
                backend=default_backend()
            )
            private_key_data = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
            public_key = private_key.public_key()
            public_key_data = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )

            private_key_file.write(private_key_data)
            public_key_file.write(public_key_data)


def _generate_signature(msg):
    with open(KEY_PATH+'key.pem', 'rb') as private_key_file:
        private_key = serialization.load_pem_private_key(private_key_file.read(), password=None, backend=default_backend())
        return base64.urlsafe_b64encode(private_key.sign(
            msg.encode('utf8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA3_256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA3_256()
        )).decode()


def verify_signature(msg):
    split_msg = msg.split('(╯°□°)╯︵ ┻━┻')
    message = split_msg[0]
    signature = base64.urlsafe_b64decode(split_msg[1].encode())
    with open(KEY_PATH+'key.pub', 'rb') as public_key_file:
        public_key = serialization.load_pem_public_key(public_key_file.read(), backend=default_backend())
        try:
            public_key.verify(
                signature,
                message.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA3_256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA3_256()
            )
            return True
        except InvalidSignature:
            return False


def sign_string(msg):
    return msg+'(╯°□°)╯︵ ┻━┻'+_generate_signature(msg)
