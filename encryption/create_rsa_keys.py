from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


print('=====KEY=====')
_private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
_public_key = _private_key.public_key()

_pem = _private_key.private_bytes(
     encoding=serialization.Encoding.PEM,
     format=serialization.PrivateFormat.TraditionalOpenSSL,
     encryption_algorithm=serialization.NoEncryption()
)
print(_pem.decode())
with open('rsa_key.key', mode='w') as f:
    f.write(_pem.decode())

_pem = _public_key.public_bytes(
     encoding=serialization.Encoding.PEM,
     format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print(_pem.decode())
with open('rsa_key.pub', mode='w') as f:
    f.write(_pem.decode())
