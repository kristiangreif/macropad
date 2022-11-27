# Macropad
Raspberry Pi Pico-based macropad with a radial controller
## Setup
1. Flash the latest CiruitPython firmware to a RPi Pico
2. Install Thonny IDE
3. Connect the Pico to your PC, open Thonny IDE and select the CircuitPython interpreter on your Pico (Run->Select Interpreter)
4. With your Pico Connected, click Tools->Manage packages and install thbe following libraries:
   - adafruit_circuitpython_hid
   - adafruit_circuitpython_debouncer
   - adafruit_circuitpython_radial_controller
5. Create a new file named code.py, copy the contents of a corresponding file in this repo to it and save it to the Pico
6. Create a new file named boot.py, copy the contents of a corresponding file in this repo to it and save it to the Pico
7. Now (physically) reconnect the Pico, press the green play button in Thonny IDE and test all the buttons

The macropad should now work every time you plug it into your PC.
## Configuring The Keys
In [code.py](code.py), find a marked section with keycode assignments and change the respective keycodes to your liking:
```python
KEYCODES = (
    [Keycode.ONE], #col 1, row 1, key: '1'
    [Keycode.TWO], #col 2, row 1, key: '2'
    [Keycode.THREE], #col 3, row 1, key: '3'
    [Keycode.FOUR], #col 4, row 1, key: '4'
    [Keycode.FIVE], #col 1, row 2, key: '5'
    [Keycode.SIX], #col 2, row 2, key: '6'
    [Keycode.SEVEN], #col 3, row 2, key: '7'
    [Keycode.EIGHT], #col 4, row 2, key: '8'
    [Keycode.NINE], #col 1, row 3, key: '9'
    [Keycode.ZERO], #col 2, row 3, key: '0'
    [Keycode.A], #col 3, row 3, key: 'A'
    [Keycode.B], #col 4, row 3, key: 'B'
    [Keycode.C], #col 1, row 4, key: 'C'
    [Keycode.D], #col 2, row 4, key: 'D'
    [Keycode.CONTROL, Keycode.C], #col 3, row 4, key: 'CTRL'+'C'
    [Keycode.CONTROL, Keycode.V], #col 4, row 4, key: 'CTRL'+'V'
)
```
Save the file and restart the Pico.
