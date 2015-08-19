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
    joystick_device = None

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
        try:
            return joypad_buttons[key]
        except KeyError:
            joypad_buttons = {
                'A': 0,
                'B': 1,
                'X': 2,
                'Y': 3,
                'LB': 4,
                'RB': 5,
                'Select': 6,
                'Start': 7,
                'Home': 8,
                'L3': 9,
                'R3': 10,
            }
            return self.joystick.buttons[joypad_buttons[key]]

    def void(self, *kargs):
        pass


class JoypadMenuSuport(object):

    """ Adds support for Xbox One joystick """

    def on_joyaxis_motion(self, joystick, axis, value):
        if len(director.scene_stack) != 0:
            return
        if (axis is 'x') or (axis is 'hat_x'):
            return
        if (abs(value) > 0.1):
            # print axis, value
            pass
        if axis is 'hat_y':
            value *= -1
        idx = self.selected_index
        if (value == 1):
            idx += 1
        if (value == -1):
            idx -= 1
        if idx < 0:
            idx = len(self.children) - 1
        elif idx > len(self.children) - 1:
            idx = 0
        self._select_item(idx)

    def on_joybutton_press(self, joystick, button):
        if len(director.scene_stack) != 0:
            return
        try:
            # print EventHandle()[button]
            EventHandle().joystick.on_joyaxis_motion = EventHandle().void
            EventHandle().joystick.on_joybutton_press = EventHandle().void
            if EventHandle()[button] is 'B':
                self.on_quit()
            else:
                self._activate_item()
        except Exception:
            pass
