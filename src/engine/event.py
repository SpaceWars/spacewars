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
