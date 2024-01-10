# store_events.py
"""
This is a script that will record your actions until you press "q" and then
save them into a csv file.
"""
from pynput import keyboard, mouse
import csv
import time

# Lists to store recorded keyboard and mouse events
recorded_events = []
current_time = time.time()
# Function to handle keyboard events
def on_press(key):
    try:
        # Add pressed key to the recorded events list
        # if the key is shift, do nothing:
        if key == keyboard.Key.shift:
            pass
        else:
            recorded_events.append(('key_press', key.char, time.time() - current_time))
            if key.char == 'q':
                # Stop listening for events
                keyboard_listener.stop()
                mouse_listener.stop()
                # Save recorded events to a csv file
                with open('recorded_events.csv', 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(['event_type',
                                    'time_since_last_event', 
                                    'key_pressed', 
                                    'mouse_position_x', 
                                    'mouse_poistion_y', 
                                    'mouse_button'])
                    time_slice = 0
                    last_time = 0
                    for event in recorded_events:
                        if event[0] == 'key_press':
                            writer.writerow([event[0], time_slice, event[1], '', '', ''])
                        else:
                            button = event[1][2]
                            if button == mouse.Button.left:
                                button = 'left'
                            elif button == mouse.Button.right:
                                button = 'right'
                            else:
                                button = 'middle'
                            writer.writerow([event[0], time_slice, '', event[1][0], event[1][1], button])
                        time_slice = event[2] - last_time
                        last_time = event[2]
    except AttributeError:
        # Handle special keys
        recorded_events.append(('key_press', key))

# Function to handle mouse events
def on_click(x, y, button, pressed):
    if pressed:
        # Add mouse click event to the recorded events list
        recorded_events.append(('mouse_click', (x, y, button), time.time() - current_time))

# Create an instance of Listener class
keyboard_listener = keyboard.Listener(on_press=on_press)
mouse_listener = mouse.Listener(on_click=on_click)

# Start listening for events
keyboard_listener.start()
mouse_listener.start()

# Wait for the listeners to finish
keyboard_listener.join()
mouse_listener.join()

# Print recorded events
with open('recorded_events.csv', 'r') as f:
    reader = csv.reader(f)
    # Skip the header row
    next(reader)
    for row in reader:
        data = row[1:]
        row_type = row[0]
        if row_type == 'key_press':
            print(f'Key pressed: {data[1]}, and it took {data[0]} seconds to press it')
        else:
            print(f'Mouse clicked at: {data[2]}, {data[3]} with {data[4]} button, and it took {data[0]} seconds to click it')
