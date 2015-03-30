import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))
from operator import setslice
from cocos.director import director
from cocos.layer import *
from cocos.scene import Scene
from cocos.scenes.transitions import *
from cocos.actions import *
from cocos.sprite import *
from cocos.menu import *
from cocos.text import *
import pyglet
import sound as soundex
from pyglet import gl, font
from pyglet.window import key


class OptionsMenu(Menu):

    def __init__(self):
        super(OptionsMenu, self).__init__('SpaceWars')
        # you can override the font that will be used for the title and the
        # items
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

        self.show_fullscreen = False

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
        items.append(
            ToggleMenuItem('Fullscreen:', self.on_fullscreen, self.show_fullscreen))
        items.append(MenuItem('Back', self.on_quit))
        self.create_menu(items, shake(), shake_back())

    def on_fullscreen(self, value):
        self.show_fullscreen = value
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


if __name__ == "__main__":
    director.init()
    main_window = OptionsMenu()
    main_scene = Scene(main_window)
    print """
    SpaceWars  Copyright (C) 2015 Luiz Fernando Oliveira, Carlos Oliveira, Matheus Souza Fernandes

    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.
    """
    director.run(main_scene)
