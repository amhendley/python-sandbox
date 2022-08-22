from passlib.context import CryptContext
from getpass import getpass


ctx = CryptContext(schemes=["bcrypt", "argon2", "scrypt"],
                   default="bcrypt",
                   bcrypt__rounds=14)

password = getpass()
hashed_password = ctx.hash(password)
print(hashed_password)

print(ctx.verify(password, hashed_password))
print(ctx.verify("not-the-password", hashed_password))
