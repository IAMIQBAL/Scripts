import keyboard

keys = keyboard.record(until="ENTER")
keyboard.play(keys, 0.5)