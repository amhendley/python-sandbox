import keyring
import keyring.util.platform_ as keyring_platform


print(keyring_platform.config_root())

print(keyring.get_keyring())

NAMESPACE = "myApp"
ENTRY = "API_KEY"

keyring.set_password(NAMESPACE, ENTRY, "a3491fb2-000f-4d9f-943e-127cfe29c39c")
print(keyring.get_password(NAMESPACE, ENTRY))

cred = keyring.get_credential(NAMESPACE, ENTRY)
print(f"Password for username {cred.username} in namespace {NAMESPACE} is {cred.password}")
