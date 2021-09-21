from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


with open("rsa_key.key", "rb") as key_file:
    _private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
)

with open('requirements.txt.rsa', mode='rb') as f:
    _cipher_text = f.readlines()

plaintext = _private_key.decrypt(
    _cipher_text,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
