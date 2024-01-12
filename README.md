# AutoDofus
The idea of this app is to make a logger of events (mouse and keyboard) so then they can be played to gather resources.


# Usage:
You need to have your PYTHONPATH exported
## For windows:
```bash
set PYTHONPATH=%cd%
```
while being on the root of the project should do the trick.

## For linux:
```bash
export PYTHONPATH=.
```
also while being on the root of the project.


From the current directory run:
# Logger:
```bash
python3 src/logger/main.py x y
```
This will start to record your actions, then when you are done you can press esc for it to stop and save the file.
# Player:
```bash
python3 src/player/main.py x y
```

This will start to play the actions you have saved for the map x y.