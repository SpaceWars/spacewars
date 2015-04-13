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
from pyglet.window import key
from cocos.layer import Layer
from cocos.scene import Scene
from layers.base_layers import BackgroundLayer
from game.sprites import SpaceShipSprite, AeroliteSprite, RohenianSprite
from configs import WIDTH


class GameScene(Layer):
    is_event_handler = True

    def __init__(self):
        super(GameScene, self).__init__()
        self.background = BackgroundLayer('backgrounds/bluespace.png')
        self.spaceship = SpaceShipSprite()
        self.aerolites = []
        self.rohenians = []
        for x in xrange(50, WIDTH, 100):
            self.aerolites.append(AeroliteSprite(width=x))
            self.rohenians.append(RohenianSprite())

    def new_game(self):
        scene = Scene()

        scene.add(self.background, z=0)
        scene.add(self)
        scene.add(self.spaceship)

        for aero in self.aerolites:
            scene.add(aero)

        for rohenian in self.rohenians:
            scene.add(rohenian)

        return scene

    def on_text_motion(self, keys):
        if keys == key.MOTION_LEFT:
            print 'Move Spaceship to left'
            self.spaceship.move_left()
        elif keys == key.MOTION_RIGHT:
            print 'Move Spaceship to rigth'
            self.spaceship.move_rigth()
