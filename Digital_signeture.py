from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa 
from cryptography.hazmat.primitives.asymmetric import padding 
from cryptography.hazmat.primitives import serialization 
private_key = rsa.generate_private_key(
public_exponent=65537, key_size=2048
)
private_pem = private_key.private_bytes( encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption()
)
public_key = private_key.public_key() 
public_pem = public_key.public_bytes(
encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo
)
message = b"Hello, this is a test message." 
signature = private_key.sign(
message,
padding.PSS(
mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
),
hashes.SHA256()
)
with open("private_key.pem", "wb") as f: f.write(private_pem)
with open("public_key.pem", "wb") as f: f.write(public_pem)
with open("signature.bin", "wb") as f: f.write(signature)
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding 
from cryptography.hazmat.primitives import serialization
with open("public_key.pem", "rb") as f: public_pem = f.read()
with open("signature.bin", "rb") as f: signature = f.read()
public_key = serialization.load_pem_public_key(public_pem) 
message = b"Hello, this is a test message."
try:
    public_key.verify(
    signature, message,
    padding.PSS(
    mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
    print("Signature is valid.") 
except Exception:
    print("Signature is invalid.")


