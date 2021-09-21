from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

with open("rsa_key.pub", "rb") as key_file:
    _public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
)

with open('requirements.txt', mode='r') as f:
    lines = f.readlines()
_message = '\n'.join(lines)

_cipher_text = _public_key.encrypt(
    _message.encode(),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print('=====CYPHER TEXT=====')
print(_cipher_text)

with open('requirements.txt.rsa', mode='wb') as f:
    f.write(_cipher_text)
