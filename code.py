# SPDX-FileCopyrightText: Copyright (c) 2021 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

import board
import digitalio
import rotaryio
import usb_hid
import keypad
import adafruit_radial_controller
from adafruit_debouncer import Debouncer
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

#Macropad keycode configuration
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

km = keypad.KeyMatrix(
    row_pins=(board.GP19, board.GP18, board.GP17, board.GP16),
    column_pins=(board.GP27, board.GP20, board.GP21, board.GP26),
)

kbd = Keyboard(usb_hid.devices)

switch = digitalio.DigitalInOut(board.GP13)
switch.pull = digitalio.Pull.DOWN
debounced_switch = Debouncer(switch)

encoder = rotaryio.IncrementalEncoder(board.GP14, board.GP15)
radial_controller = adafruit_radial_controller.RadialController(usb_hid.devices)

last_position = 0
DEGREE_TENTHS_MULTIPLIER = 100

while True:
    debounced_switch.update()
    if debounced_switch.rose:
        radial_controller.press()
    if debounced_switch.fell:
        radial_controller.release()

    position = encoder.position
    delta = position - last_position
    if delta != 0:
        radial_controller.rotate(delta * DEGREE_TENTHS_MULTIPLIER)
        last_position = position
        
    event = km.events.get()
    if event:
        key_number = event.key_number
        
        if event.pressed:
            kbd.press(*KEYCODES[key_number])

        if event.released:
            kbd.release(*KEYCODES[key_number])
