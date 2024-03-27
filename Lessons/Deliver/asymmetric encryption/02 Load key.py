from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def load_private_key(filename):
    with open(filename, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return private_key

def load_public_key(filename):
    with open(filename, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    return public_key

def key_to_text(key):
    if hasattr(key, 'private_numbers'):
        return key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ).decode()
    elif hasattr(key, 'public_numbers'):
        return key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode()
    else:
        raise ValueError("Unsupported key type")


# Load the keys from the files
private_key = load_private_key("private_key.pem")
public_key = load_public_key("public_key.pem")

# print the keys
print(key_to_text(private_key))
print(key_to_text(public_key))



