#!/usr/bin/python
# -*- encoding: utf-8 -*-

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


from cocos.layer import ScrollableLayer
from cocos.director import director
from cocos.text import Label
from cocos.scene import Scene
from pyglet.window import Window
from pyglet.window import key as Key


class Credits(ScrollableLayer):

    """docstring for Credits"""

    is_event_handler = True

    def __init__(self):
        super(Credits, self).__init__()
        width, height = director.get_window_size()
        self.keyboard = Key.KeyStateHandler()

        for line in self.text().split('\n'):
            label = Label(line,
                          font_name='Bangers',
                          font_size=32,
                          position=((height / 4) - len(line), width))
            self.add(label)
            width -= 35

    def text(self):
        return """
Credits:

Programmers
-----------

Luiz Fernando Gomes de Oliveira
Carlos Oliveira
Mateus Souza Fernandes

Designers
---------


Testers
-------
    """

    def on_quit(self):
        print "Quit pressed"

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
