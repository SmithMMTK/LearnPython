from pynput import keyboard

def on_key_press(key):
    try:
        if key == keyboard.Key.enter:
            return False  # Stop listener
        else:
            if hasattr(key, 'char'):
                keystrokes.append(key.char)
            else:
                keystrokes.append(str(key))
    except AttributeError:
        pass

keystrokes = []
listener = keyboard.Listener(on_press=on_key_press)

print("Press keys and press Enter to display:")

with listener as l:
    l.join()

print("\nKeystrokes entered:")
print("".join(keystrokes))
