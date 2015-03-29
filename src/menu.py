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

from cocos.menu import Menu, MenuItem


class MainMenu(Menu):

    """Class for Main Menu

    It creates a main menu with default or extra options.

    """

    def __init__(self, title='SpaceWars', menu_items=[]):
        super(MainMenu, self).__init__()
        self.menu_items = []
        self.font_title = {
            'text': 'SpaceWars',
            'font_name': 'Bangers',
            'font_size': 56,
            'color': (192, 192, 192, 255),
            'bold': False,
            'italic': False,
            'anchor_y': 'center',
            'anchor_x': 'center',
            'dpi': 96,
            'x': 0, 'y': 0,
        }
        self.title_text = self.title = "SpaceWars"

        self.font_item = {
            'font_name': 'Bangers',
            'font_size': 32,
            'bold': False,
            'italic': False,
            'anchor_y': 'center',
            'anchor_x': 'center',
            'color': (192, 192, 192, 255),
            'dpi': 96,
        }

        self.font_item_selected = {
            'font_name': 'Bangers',
            'font_size': 42,
            'bold': False,
            'italic': False,
            'anchor_y': 'center',
            'anchor_x': 'center',
            'color': (255, 255, 255, 255),
            'dpi': 96,
        }

        if not menu_items:
            self.build_default_menu()

        for menu_item in menu_items:
            self.build_menu(menu_item)

        self.create_menu(self.menu_items)

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
