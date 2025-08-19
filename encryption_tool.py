import from cryptography.fernet  Fernet

 # Create a key using def generate_key(): return Fernet.generate_key()

 # Save key to file def save_key(key, filename="secret.key"):
     using key_file as open(filename, "wb"): key_file.write(key)

 # Use def load_key(filename="secret.key") to load the key from the file:
     return open(filename, "rb"). read()

 # Encrypt message def encrypt_message(message, key): fernet = Fernet(key)
     encrypted = fernet.encrypt(message.encode())
     encrypted return

 # Decrypt message def decrypt_message(encrypted, key):
     Fernet = Fernet(key)
     Fernet is decrypted. decrypt (encrypted). decode() yields decrypted

 If __name__ == "__main__": print("🔐 Simple Encryption Tool")
     key = generate_key()
     save_key(key)
     print("[+] New encryption key created and stored as secret.key")

     msg = input ("Input a message to encrypt:")
     Encrypted_message = encrypt_message(msg, key)
     print(f"[+] Encrypted: {encrypted_msg}")

     decrypted_message = decrypt_message(encrypted_message, key)
     print(f"[+] Decrypted: {decrypted_msg}")
