from pgpy import PGPKey, PGPMessage


key, _ = PGPKey.from_file('working_key.pub')
print(key)

# message = PGPMessage.new("requirements.txt", file=True)
# print(message)

with open('requirements.txt', mode='r') as f:
    lines = f.readlines()
message = PGPMessage.new('\n'.join(lines), literal=True)
print(message)

encrypted_message = key.encrypt(message)
print(encrypted_message)


with open('requirements.txt.pgp', mode='w') as f:
    f.write(str(encrypted_message))
