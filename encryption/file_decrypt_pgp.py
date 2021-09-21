from pgpy import PGPKey, PGPMessage


key, _ = PGPKey.from_file('working_key.asc')

print('=====ORIGINAL=====')
message = PGPMessage.from_file("requirements.txt.pgp")
print(message)

print()
print('Message is compressed: {0}'.format(message.is_compressed))
print('Message is sensitive: {0}'.format(message.is_sensitive))
print('Message is signed: {0}'.format(message.is_signed))
print('Message is encrypted: {0}'.format(message.is_encrypted))
print()


print('=====DECRYPTED=====')

# with key.unlock('LetMeIn') as k:
decrypted_message = key.decrypt(message)
print(decrypted_message)

m = PGPMessage()
t = None
decrypted_message.bytes_to_text(text=t)
print(t)

print()
print('Message is compressed: {0}'.format(decrypted_message.is_compressed))
print('Message is sensitive: {0}'.format(decrypted_message.is_sensitive))
print('Message is signed: {0}'.format(decrypted_message.is_signed))
print('Message is encrypted: {0}'.format(decrypted_message.is_encrypted))
print()
