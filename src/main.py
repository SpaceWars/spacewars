#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
Copyright (C) 2015  SpaceWars Inc.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from cocos.layer import Layer
from cocos.director import director
from cocos.text import Label
from cocos.scene import Scene
from pyglet.window import key as Key
import signal


class MainWindow(Layer):

    is_event_handler = True

    def __init__(self):
        super(MainWindow, self).__init__()
        self.keyboard = Key.KeyStateHandler()
        director.window.push_handlers(self.keyboard)

    def on_key_press(self, key, modifiers):
        pass

    def on_key_release(self, key, modifiers):
        if self.keyboard[Key.ENTER]:
            label = Label('SpaceWars',
                          font_name='Times New Roman',
                          font_size=32)
            self.add(label)


def signal_handler(signal_received, frame):
    if signal_received is signal.SIGINT:
        # erase the ^C on Terminal
        print "\r  "
        exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    director.init()
    main_window = MainWindow()
    main_scene = Scene(main_window)
    print """
    SpaceWars  Copyright (C) 2015  SpaceWars Inc.

    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details."""
    director.run(main_scene)
