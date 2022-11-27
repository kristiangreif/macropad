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

KEYCODES = (
    [Keycode.ONE],
    [Keycode.TWO],
    [Keycode.THREE],
    [Keycode.FOUR],
    [Keycode.FIVE],
    [Keycode.SIX],
    [Keycode.SEVEN],
    [Keycode.EIGHT],
    [Keycode.NINE],
    [Keycode.ZERO],
    [Keycode.A],
    [Keycode.B],
    [Keycode.C],
    [Keycode.D],
    [Keycode.CONTROL, Keycode.C],
    [Keycode.CONTROL, Keycode.V],
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
