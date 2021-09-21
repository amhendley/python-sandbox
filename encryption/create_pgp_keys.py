from datetime import timedelta
from pgpy import PGPKey, PGPUID
from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm


# we can start by generating a primary key. For this example, we'll use RSA, but it could be DSA or ECDSA as well
key = PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)

# we now have some key material, but our new key doesn't have a user ID yet, and therefore is not yet usable!
uid = PGPUID.new('Andrew Hendley', comment='It''s me', email='andrew.hendley@jbwere.com')

# now we must add the new user id to the key. We'll need to specify all of our preferences at this point
# because PGPy doesn't have any built-in key preference defaults at this time
# this example is similar to GnuPG 2.1.x defaults, with no expiration or preferred keyserver
key.add_uid(uid, usage={KeyFlags.Sign, KeyFlags.EncryptCommunications, KeyFlags.EncryptStorage},
            hashes=[HashAlgorithm.SHA256, HashAlgorithm.SHA384, HashAlgorithm.SHA512, HashAlgorithm.SHA224],
            ciphers=[SymmetricKeyAlgorithm.AES256, SymmetricKeyAlgorithm.AES192, SymmetricKeyAlgorithm.AES128],
            compression=[CompressionAlgorithm.ZLIB, CompressionAlgorithm.BZ2, CompressionAlgorithm.ZIP, CompressionAlgorithm.Uncompressed],
            key_expires=timedelta(days=365))

# assuming we already have a primary key, we can generate a new key and add it as a subkey thusly:
subkey = PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)

# preferences that are specific to the subkey can be chosen here
# any preference(s) needed for actions by this subkey that not specified here
# will seamlessly "inherit" from those specified on the selected User ID
key.add_subkey(subkey, usage={KeyFlags.Authentication})

# key.protect(passphrase='LetMeIn', enc_alg=SymmetricKeyAlgorithm.AES256, hash_alg=HashAlgorithm.SHA256)

pub_key = key.pubkey

with open('working_key.asc', mode='w') as f:
    f.write(str(key))

with open('working_key.pub', mode='w') as f:
    f.write(str(pub_key))

print("=====KEY=====\n", key)
print("=====PUBLIC KEY=====\n", pub_key)
# print("=====UID=====\n", uid)
# print("=====SUBKEY=====\n", subkey)
