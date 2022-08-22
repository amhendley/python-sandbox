import string
import secrets


length = 15

for i in range(10):
    # Choose wide set of characters, but consider what your system can handle
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))

    print(password)
