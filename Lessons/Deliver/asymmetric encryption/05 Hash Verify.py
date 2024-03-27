from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

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


# Prompt to get file name to decrypt
file_name = input("Enter the original file name: ")
signature_file = input("Enter the signature file name: ")

# Verify the signature
with open(signature_file, "rb") as sig_file:
    signature_to_verify = sig_file.read()

with open(file_name, "rb") as file:
    data = file.read()

# Add verification of the signature for file_name
digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
digest.update(data)
hashed_data = digest.finalize()

try:
    public_key.verify(
        signature_to_verify,
        hashed_data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature verified")
except:
    print("Signature not verified")






