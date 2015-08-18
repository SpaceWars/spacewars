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
import signal

from cocos.director import director
from cocos.layer import MultiplexLayer
from cocos.scene import Scene
from configs import WIDTH, HEIGHT
from engine.event import EventHandle
from layers.base_layers import BackgroundLayer
from layers.menu import MainMenu, Credits, OptionsMenu
from pyglet import input
from pyglet import resource, font
from pyglet.window import key
from pyglet import clock
from os import listdir


def connect_joystick(*args):
    if EventHandle().joystick_device is not None:
        devices = listdir('/dev/input')
        if 'js0' not in devices:
            print("%s disconnected " % (EventHandle().joystick_device.name))
            input.evdev._devices = {}
            EventHandle().joystick = None
            EventHandle().joystick_device = None
        return
        if 'js1' not in devices:
            print("Only 1 joystick is supported for now")
    try:
        # Check if joystick is connected
        EventHandle().joystick = input.get_joysticks()[0]
        EventHandle().joystick.open()
        EventHandle().joystick.z = EventHandle().joystick.rz = -1
        EventHandle().joystick_device = input.get_devices()[0]
        print "%s connected" % EventHandle().joystick_device.name
    except Exception:
        pass


def signal_handler(signal_received, frame):
    """ Handle Ctrl + C signal """
    if signal_received is signal.SIGINT:
        # erase the ^C on Terminal
        print "\r  "
        exit(0)

if __name__ == "__main__":
    # Add pyglet resources directories
    resource.path.append('data')
    resource.reindex()
    font.add_directory('data/fonts')

    signal.signal(signal.SIGINT, signal_handler)

    keyboard = key.KeyStateHandler()
    EventHandle().keyboard = keyboard

    director.init(width=WIDTH, height=HEIGHT, caption='SpaceWars')
    director.window.push_handlers(keyboard)

    # observer to joystick
    clock.schedule_interval(connect_joystick, .1)

    # Create a initial menu scene
    scene = Scene()
    scene.add(BackgroundLayer('backgrounds/space_background.png'), z=0)
    scene.add(MultiplexLayer(MainMenu(),
                             Credits(),
                             OptionsMenu()), z=1)
    print """
    SpaceWars  Copyright (C) 2015 Luiz Fernando Oliveira, Carlos Oliveira,
    Matheus Souza Fernandes

    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.
    """
    director.run(scene)
