#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
Copyright (C) 2015  Luiz Fernando Oliveira, Carlos Oliveira, Matheus Fernandes

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""
from cocos.director import director


class EventHandle(object):

    """ Class that hanle keyboard/joystick input events """

    keyboard = None
    joystick = None

    def __new__(cls):
        # Singleton instance
        if not hasattr(cls, 'instance'):
            cls.instance = super(EventHandle, cls).__new__(cls)
        return cls.instance

    def __getitem__(self, key):
        joypad_buttons = {
            0: 'A',
            1: 'B',
            2: 'X',
            3: 'Y',
            4: 'LB',
            5: 'RB',
            6: 'Select',
            7: 'Start',
            8: 'Home',
            9: 'L3',
            10: 'R3',
        }
        return joypad_buttons[key]

    def void(self, *kargs):
        pass


class JoypadMenuSuport(object):

    """ Adds support for Xbox One joystick """

    def on_joyaxis_motion(self, joystick, axis, value):
        if (axis is 'x') or (axis is 'hat_x'):
            return
        if (abs(value) > 0.1):
            print axis, value
        if axis is 'hat_y':
            value *= -1
        idx = self.selected_index
        if (value > 0.4):
            idx += 1
        if (value < -0.4):
            idx -= 1
        if idx < 0:
            idx = len(self.children) - 1
        elif idx > len(self.children) - 1:
            idx = 0
        self._select_item(idx)

    def on_joybutton_press(self, joystick, button):
        try:
            print EventHandle()[button]
            EventHandle().joystick.on_joyaxis_motion = EventHandle().void
            EventHandle().joystick.on_joybutton_press = EventHandle().void
            if EventHandle()[button] is 'B':
                director.pop()
            else:
                self._activate_item()
        except Exception:
            pass
