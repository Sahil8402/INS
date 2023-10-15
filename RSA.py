from cryptography.hazmat.primitives.asymmetric import rsa,padding 
from cryptography.hazmat.primitives import serialization, hashes 
private_key = rsa.generate_private_key(
    public_exponent=65537, key_size=2048)
public_key = private_key.public_key() 
message = b"(200303108007)" 
ciphertext = public_key.encrypt( message,
padding.OAEP( mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(),
label=None
) )
decrypted_message = private_key.decrypt( ciphertext,
padding.OAEP( mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(),
label=None
) )
print("Original message:", message) 
print ("Encrpyted Message",ciphertext)
print("Decrypted message:", decrypted_message.decode('utf-8'))
