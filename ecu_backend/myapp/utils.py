from cryptography.fernet import Fernet

# Replace this key with YOUR generated key from Fernet.generate_key()
FERNET_KEY = b"YOUR_GENERATED_KEY_HERE"

fernet = Fernet(FERNET_KEY)

def encrypt_password(password):
    return fernet.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    return fernet.decrypt(encrypted_password.encode()).decode()
