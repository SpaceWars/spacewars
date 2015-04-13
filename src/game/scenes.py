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
from cocos.layer import Layer
from cocos.scene import Scene
from layers.base_layers import BackgroundLayer
from game.sprites import *
from configs import WIDTH, HEIGHT


class GameScene(Layer):

    def __init__(self):
        super(GameScene, self).__init__()

    @classmethod
    def new_game(cls):
        scene = Scene()

        game_scene = GameScene()
        scene.add(BackgroundLayer('backgrounds/bluespace.png'), z=0)
        scene.add(game_scene)

        spaceship = SpaceShipSprite()
        scene.add(spaceship)
        aerolites = []
        for x in xrange(50, WIDTH, 100):
            aerolites.append(AeroliteSprite(width=x))
        for aero in aerolites:
            scene.add(aero)

        return scene
