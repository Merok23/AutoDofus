# free_money.py
"""
This is a script for fishing in dofus, in the future it could integrate
machine learning, but for now the idea is to make a script that will
record your actions for a given time and then save them in a csv so you can
then use it to fish automatically.
"""
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController, Listener
import csv
import time

# Initialize controllers for keyboard and mouse
keyboard_controller = KeyboardController()
mouse_controller = MouseController()
FILE_PATH = 'recorded_events.csv'
paused = False

def on_press(key):
    global paused

    if key == Key.f1:
        if not paused:
            paused = True
            print("Script paused")
        else:
            paused = False
            print("Resuming script")
    if key == Key.esc:
        # Stop listener
        return False

def smooth_mouse_move(start_pos, end_pos, duration):
    # Calculate the number of steps for the given duration
    steps = 50
    sleep_time = duration / steps

    # Calculate the distance to move in each step
    delta_x = (end_pos[0] - start_pos[0]) / steps
    delta_y = (end_pos[1] - start_pos[1]) / steps

    # Perform the interpolated mouse movement
    for i in range(steps):
        new_x = start_pos[0] + delta_x * (i + 1)
        new_y = start_pos[1] + delta_y * (i + 1)
        mouse_controller.position = (new_x, new_y)
        time.sleep(sleep_time)

def on_release(key):
    pass

def press_key(event):
    keyboard_controller.press(event[2])
    keyboard_controller.release(event[2])

def read_events(reader):
    start_time = time.time()
    for event in reader:
        if paused:
            while paused:
                time.sleep(0.1)

        if event[0] == 'key_press':
            press_key(event)
        else:
            current_time = time.time()
            elapsed_time = current_time - start_time
            target_time = float(event[1])
            remaining_time = target_time - elapsed_time
            if remaining_time > 0:
                time.sleep(remaining_time)
            mouse_position = (int(event[3]), int(event[4]))
            smooth_mouse_move(mouse_controller.position, mouse_position, float(event[1]))

            if event[5] == 'left':
                mouse_controller.click(Button.left)
            elif event[5] == 'right':
                mouse_controller.click(Button.right)
            else:
                mouse_controller.click(Button.middle)
            start_time = time.time()


# Create listener for keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    # Read and execute events from the CSV file
    with open(FILE_PATH, 'r') as f:
        reader = csv.reader(f)
        # Skip the header row
        next(reader)
        read_events(reader)
        
    listener.join()

