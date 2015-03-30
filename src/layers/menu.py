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
from cocos.director import director
from cocos.text import Label
from cocos.layer import ScrollableLayer
from cocos.menu import Menu, MultipleMenuItem, MenuItem, ToggleMenuItem,\
    shake, shake_back, CENTER
import sound as soundex


class MainMenu(Menu):

    """Class for Main Menu

    It creates a main menu with default or extra options.

    """

    def __init__(self, title='SpaceWars', menu_items=[]):
        super(MainMenu, self).__init__()
        self.menu_items = []

        self.font_title = {
            'text': 'SpaceWars',
            'font_name': 'Orbitron',
            'font_size': 60,
            'color': (192, 192, 192, 255),
            'bold': True,
            'anchor_y': 'center',
            'anchor_x': 'center',
        }
        self.title_text = self.title = "SpaceWars"

        self.font_item = {
            'font_name': 'Titillium Web',
            'font_size': 32,
            'anchor_y': 'center',
            'anchor_x': 'center',
            'color': (32, 16, 32, 255),
        }

        self.font_item_selected = {
            'font_name': 'Titillium Web',
            'font_size': 40,
            'bold': False,
            'anchor_y': 'center',
            'anchor_x': 'center',
            'color': (255, 255, 255, 255),
        }

        if not menu_items:
            self.build_default_menu()

        for menu_item in menu_items:
            self.build_menu(menu_item)

        self.create_menu(self.menu_items, shake(), shake_back())

    def build_menu(self, menu_item=None):
        if menu_item:
            self.menu_items.append(menu_item)

    def build_default_menu(self):
        self.menu_items.append(MenuItem('New Game', self.new_game))
        self.menu_items.append(MenuItem('Options', self.options))
        self.menu_items.append(MenuItem('Credits', self.credits))
        self.menu_items.append(MenuItem('Quit', self.on_quit))

    def on_quit(self):
        print "Quit pressed"
        exit(0)

    def new_game(self):
        print "New game selected"

    def credits(self):
        print "Show me the credits!"
        self.parent.switch_to(1)

    def options(self):
        print "Choose your options"
        self.parent.switch_to(2)


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


class OptionsMenu(Menu):

    def __init__(self):
        super(OptionsMenu, self).__init__('SpaceWars')
        self.font_title['font_name'] = 'Bangers'
        self.font_title['font_size'] = 72
        # self.font_title['color'] = (204, 164, 164, 255)
        self.font_item['font_name'] = 'Bangers',
        self.font_item['color'] = (32, 16, 32, 255)
        self.font_item['font_size'] = 32
        self.font_item_selected['font_name'] = 'Bangers'
        # self.font_item_selected['color'] = (32, 16, 32, 255)
        self.font_item_selected['font_size'] = 46
        # you can also override the font size and the colors. see menu.py for
        # more info
        # example: menus can be vertical aligned and horizontal aligned
        self.menu_anchor_y = CENTER
        self.menu_anchor_x = CENTER
        items = []
        # self.volumes = ['Mute', '10', '20', '30',
        #                 '40', '50', '60', '70', '80', '90', '100']
        self.volumes = ['Mute', 'Sound in space?']
        items.append(MultipleMenuItem(
            'SFX volume: ',
            self.on_sfx_volume,
            self.volumes,
            int(soundex.sound_vol * len(self.volumes)))
        )
        items.append(MultipleMenuItem(
            'Music volume: ',
            self.on_music_volume,
            self.volumes,
            int(soundex.music_player.volume * len(self.volumes)))
        )
        items.append(
            ToggleMenuItem('Show FPS:', self.on_show_fps, director.show_FPS))
        items.append(MenuItem('Fullscreen', self.on_fullscreen))
        items.append(MenuItem('Back', self.on_quit))
        self.create_menu(items, shake(), shake_back())

    def on_fullscreen(self):
        director.window.set_fullscreen(not director.window.fullscreen)

    def on_quit(self):
        self.parent.switch_to(0)

    def on_show_fps(self, value):
        director.show_FPS = value

    def on_sfx_volume(self, idx):
        vol = idx / 10.0
        soundex.sound_volume(vol)

    def on_music_volume(self, idx):
        vol = idx / 10.0
        soundex.music_volume(vol)
