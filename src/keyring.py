from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
import hashlib
import os


issuer = os.environ.get("EASY_JWKS_ISSUER", "http://localhost:8000").rstrip("/")

with open(os.environ.get("EASY_JWKS_KEYFILE", "key.pem"), "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
    )

public_key = private_key.public_key()
kid = hashlib.sha1(public_key.public_bytes(serialization.Encoding.DER, serialization.PublicFormat.SubjectPublicKeyInfo)).hexdigest()
