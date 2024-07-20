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

def decrypt_file(input_filename, output_filename, key):
    cipher_suite = Fernet(key)
    
    try:
        with open(input_filename, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
            print(f"Encrypted data size: {len(encrypted_data)} bytes")

        # Split encrypted data by delimiter (newline)
        encrypted_chunks = encrypted_data.split(b'\n')
        decrypted_data = b''

        for chunk in encrypted_chunks:
            if chunk:  # Avoid empty chunks
                try:
                    decrypted_data += cipher_suite.decrypt(chunk)
                except Exception as e:
                    print(f"Error decrypting chunk: {str(e)}")

        # Write decrypted data to output file
        with open(output_filename, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)
        
        print(f"Decryption successful. Decrypted data saved to {output_filename}.")
    
    except Exception as e:
        print(f"Error during decryption: {str(e)}")

if __name__ == "__main__":
    encryption_key = get_encryption_key()
    decrypt_file('keyfile.txt', 'decrypt_keyfile.txt', encryption_key)