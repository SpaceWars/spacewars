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
from cocos.sprite import Sprite
from cocos.actions import MoveTo
from configs import WIDTH, HEIGHT
from pyglet import resource
import random
from engine.action import AeroliteAction, SpaceshipAction


class SpaceShipSprite(Sprite):

    def __init__(self):
        image = 'sprites/spaceship/center.png'
        super(SpaceShipSprite, self).__init__(image)

        self.position = (WIDTH / 2, - self.image.height)
        self.scale = 0.25
        self.velocity = (0, 0)
        self.do(MoveTo((WIDTH / 2, 100), 2))
        self.do(SpaceshipAction())

    def move_left(self):
        self.image = resource.image('data/sprites/spaceship/left4.png')

    def move_right(self):
        self.image = resource.image('data/sprites/spaceship/right4.png')

    def center_spaceship(self):
        self.image = resource.image('data/sprites/spaceship/center.png')


class Enemies(Sprite):

    """docstring for Enemies"""

    def __init__(self, arg):
        super(Enemies, self).__init__(arg)
        self.velocity = (0, 0)


class AeroliteSprite(Enemies):

    def __init__(self, width=WIDTH / 2, height=2 * HEIGHT):
        image = 'sprites/aerolite/aero1.png'
        super(AeroliteSprite, self).__init__(image)

        width = random.randint(0, WIDTH)
        self.scale = 0.15
        self.position = (width, HEIGHT + HEIGHT / 8)
        self.do(AeroliteAction())


class RohenianSprite(Enemies):

    def __init__(self):
        image = "sprites/rohenians/F5S1.png"
        super(RohenianSprite, self).__init__(image)

        width = random.randint(0, WIDTH)
        self.position = (width, HEIGHT)
        self.scale = 0.30


class Bullet(Sprite):

    """docstring for Bullet"""

    def __init__(self):
        image = "sprites/rohenians/fire.png"
        super(Bullet, self).__init__(image)
        self.scale = 0.25
