import os
from cryptography.fernet import Fernet

def get_encryption_key():
    try:
        with open('ekey.txt', 'r') as key_file:
            key = key_file.read().strip()
        return key.encode()
    except FileNotFoundError:
        raise ValueError("Encryption key file not found.")
    except Exception as e:
        raise ValueError(f"Error reading encryption key: {str(e)}")

def process_file(file_path, decrypt=True):
    encryption_key = get_encryption_key()
    cipher_suite = Fernet(encryption_key)
    
    try:
        if decrypt:
            # Decrypt the file
            with open(file_path, 'rb') as file:
                encrypted_data = file.read()
            
            decrypted_data = cipher_suite.decrypt(encrypted_data)
            
            with open('decrypted_keyfile.txt', 'wb') as file:
                file.write(decrypted_data)
            print("File decrypted and saved as 'decrypted_keyfile.txt'.")
        
        else:
            # Encrypt the file
            with open(file_path, 'rb') as file:
                data = file.read()
            
            encrypted_data = cipher_suite.encrypt(data)
            
            with open('encrypted_keyfile.txt', 'wb') as file:
                file.write(encrypted_data)
            print("File encrypted and saved as 'encrypted_keyfile.txt'.")
        
    except FileNotFoundError:
        raise ValueError("File not found.")
    except Exception as e:
        raise ValueError(f"Error during file processing: {str(e)}")

if __name__ == "__main__":
    # True to decrypt or False to encrypt
<<<<<<< HEAD
    decrypt = True
=======
    decrypt = False
>>>>>>> parent of 332cb8d (working decryption)
    process_file('keyfile.txt', decrypt)
