#!/usr/bin/python
# -*- encoding: utf-8 -*-

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


from cocos.layer import ScrollableLayer
from cocos.menu import *
from cocos.director import director
from cocos.text import Label
from cocos.scene import Scene
from pyglet.window import Window


class Credits(ScrollableLayer):

    """docstring for Credits"""

    is_event_handler = True

    def __init__(self, title='SpaceWars'):
        super(Credits, self).__init__('SpaceWars')
        width, height = director.get_window_size()
        # self.font_title['font_name'] = 'Bangers'
        # self.font_title['font_size'] = 72
        label = Label('SpaceWars',
                      font_name='Bangers',
                      font_size=72,
                      color=(192, 192, 192, 255),
                      position=((height / 4), width - 45))
        self.add(label)

        width -= 72

        for line in self.text().split('\n'):
            label = Label(line,
                          font_name='Bangers',
                          font_size=32,
                          position=((height / 4) - len(line), width))
            self.add(label)
            width -= 35
        # self.create_menu([], shake(), shake_back())

    def text(self):
        return """


Programmers
-----------

Luiz Fernando Gomes de Oliveira
Carlos Henrique Ferreira Oliveira
Mateus Souza Fernandes

Designers
---------


Testers
-------
    """

    def on_quit(self):
        self.parent.switch_to(0)

    def on_key_press(self, key, modifiers):
        self.parent.switch_to(0)

if __name__ == "__main__":
    director.init()
    main_window = Credits()
    main_scene = Scene(main_window)
    print """
    SpaceWars  Copyright (C) 2015 Luiz Fernando Oliveira, Carlos Oliveira, Matheus Souza Fernandes

    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.
    """
    director.run(main_scene)
