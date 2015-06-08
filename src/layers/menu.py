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
from cocos.scenes.transitions import FadeBLTransition
from cocos.menu import (Menu, MultipleMenuItem, MenuItem, ToggleMenuItem,
                        shake, shake_back, CENTER)
from game.scenes import GameScene
from configs import FONT
import sound as soundex
from engine.event import EventHandle
from time import sleep


class JoypadMenuSuport(object):

    """docstring for JoypadMenuSuport"""

    def __init__(self):
        super(JoypadMenuSuport, self).__init__()

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
        print EventHandle()[button]
        EventHandle().joystick.on_joyaxis_motion = EventHandle().void
        EventHandle().joystick.on_joybutton_press = EventHandle().void
        self._activate_item()
        # return True


class MainMenu(Menu, JoypadMenuSuport):

    """Class for Main Menu

    It creates a main menu with default or extra options.

    """

    def __init__(self, title='SpaceWars', menu_items=[]):
        super(MainMenu, self).__init__()
        self.menu_items = []

        self.font_title = {
            'text': 'SpaceWars',
            'font_name': FONT['header'],
            'font_size': FONT['header_size'],
            'color': FONT['white'],
            'bold': True,
            'anchor_y': 'center',
            'anchor_x': 'center',
        }
        self.title_text = self.title = "SpaceWars"

        self.font_item = {
            'font_name': FONT['body'],
            'font_size': FONT['body_size'],
            'anchor_y': 'center',
            'anchor_x': 'center',
            'color': FONT['gray'],
        }

        self.font_item_selected = {
            'font_name': FONT['body'],
            'font_size': FONT['body_size_selected'],
            'bold': False,
            'anchor_y': 'center',
            'anchor_x': 'center',
            'color': FONT['white'],
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
        game_scene = GameScene()
        game_scene.parent = self.parent.parent
        director.push(FadeBLTransition(game_scene.new_game(), 1.5))

    def credits(self):
        print "Show me the credits!"
        self.parent.switch_to(1)

    def options(self):
        print "Choose your options"
        self.parent.switch_to(2)

    def draw(self):
        super(MainMenu, self).draw()
        EventHandle().joystick.on_joyaxis_motion = self.on_joyaxis_motion
        EventHandle().joystick.on_joybutton_press = self.on_joybutton_press


class Credits(ScrollableLayer, JoypadMenuSuport):

    """docstring for Credits"""

    is_event_handler = True

    def __init__(self, title='SpaceWars'):
        super(Credits, self).__init__('SpaceWars')
        width, height = director.get_window_size()
        label = Label('SpaceWars',
                      font_name=FONT['header'],
                      font_size=FONT['header_size'],
                      color=FONT['white'],
                      position=((height / 4), width - 45))
        self.add(label)

        for line in self.text().split('\n'):
            label = Label(line,
                          font_name=FONT['body'],
                          font_size=FONT['body_size_small'],
                          # position=((height / 4) - len(line), width))
                          position=((height / 7) - len(line), width - 450))
            self.add(label)
            width -= 50

    def text(self):
        return """Programmers
-----------
Luiz Fernando Gomes de Oliveira
Carlos Henrique Ferreira Oliveira
Mateus Souza Fernandes
"""

    def on_quit(self):
        print 'sair'
        self.parent.switch_to(0)

    def on_key_press(self, key, modifiers):
        self.parent.switch_to(0)

    def draw(self):
        super(Credits, self).draw()
        EventHandle().joystick.on_joybutton_press = self.on_key_press


class OptionsMenu(Menu, JoypadMenuSuport):

    def __init__(self):
        super(OptionsMenu, self).__init__('SpaceWars')

        self.font_title = {
            'text': 'SpaceWars',
            'font_name': FONT['header'],
            'font_size': FONT['header_size'],
            'color': FONT['white'],
            'bold': True,
            'anchor_y': 'center',
            'anchor_x': 'center',
        }

        self.font_item = {
            'font_name': FONT['body'],
            'font_size': FONT['body_size'],
            'anchor_y': 'center',
            'anchor_x': 'center',
            'color': FONT['gray'],
        }

        self.font_item_selected = {
            'font_name': FONT['body'],
            'font_size': FONT['body_size_selected'],
            'bold': False,
            'anchor_y': 'center',
            'anchor_x': 'center',
            'color': FONT['white'],
        }

        self.menu_anchor_y = CENTER
        self.menu_anchor_x = CENTER
        self.show_fullscreen = False
        items = []

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
        items.append(
            ToggleMenuItem('Fullscreen:', self.on_fullscreen,
                           self.show_fullscreen))
        items.append(MenuItem('Back', self.on_quit))

        self.create_menu(items, shake(), shake_back())

    def on_fullscreen(self, value):
        director.window.set_fullscreen(not director.window.fullscreen)
        self.show_fullscreen = value

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

    def draw(self):
        super(OptionsMenu, self).draw()
        EventHandle().joystick.on_joyaxis_motion = self.on_joyaxis_motion
        EventHandle().joystick.on_joybutton_press = self.on_joybutton_press
