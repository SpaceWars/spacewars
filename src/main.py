#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
Copyright (C) 2015  Luiz Fernando Oliveira, Carlos Oliveira, Matheus Souza Fernandes

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""
import signal

from cocos.layer import Layer, MultiplexLayer
from cocos.director import director
from cocos.text import Label
from cocos.scene import Scene
from cocos.scenes.transitions import *
from pyglet.window import key as Key

from menu import MainMenu
from credits import Credits
from option import OptionsMenu


class Title(Layer):

    def __init__(self):
        super(Title, self).__init__()
        label = Label('SpaceWars',
                      font_name='Bangers',
                      font_size=32,
                      position=((height / 4) - len(line), width))
        self.add(label)


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
            pass

    def on_quit(self):
        self.parent.switch_to(0)


def signal_handler(signal_received, frame):
    if signal_received is signal.SIGINT:
        # erase the ^C on Terminal
        print "\r  "
        exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    director.init()
    scene = Scene()
    scene.add(MultiplexLayer(
        MainMenu(),
        Credits(),
        OptionsMenu(),
    ),
        z=1)
    print """
    SpaceWars  Copyright (C) 2015 Luiz Fernando Oliveira, Carlos Oliveira, Matheus Souza Fernandes

    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.
    """
    director.run(scene)
