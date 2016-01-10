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
import random

from cocos.actions import Blink, Show
from cocos.sprite import Sprite
from configs import WIDTH, HEIGHT
from engine.action import AeroliteAction, SpaceshipAction, RohinianAction
from pyglet import resource
import cocos.collision_model as collision
from os import path

global real_path
real_path = path.dirname(path.realpath(__file__))
real_path = real_path.split('/game')[0]
real_path += '/data/'


class SpaceShipSprite(Sprite):

    """ Apresentation layer to Spaceship """

    def __init__(self):
        image = 'sprites/spaceship/center.png'
        super(SpaceShipSprite, self).__init__(image)

        self.health = 5
        self.position = (WIDTH / 2, - self.image.height)
        self.scale = 0.25
        self.velocity = (0, 0)
        self.do(SpaceshipAction())
        self.bullets_used = []
        self.bullets = []
        self.cshape = collision.AARectShape(self.position,
                                            self.width * self.scale,
                                            self.height * self.scale)

    def move_left(self):
        """ Change image of sprite when the spaceship moves to the left """

        self.image = resource.image('data/sprites/spaceship/left4.png')

    def move_right(self):
        """ Change image of sprite when the spaceship moves to the right """

        self.image = resource.image('data/sprites/spaceship/right4.png')

    def center_spaceship(self):
        """ Change image of sprite when the spaceship back to the
        center position """

        self.image = resource.image('data/sprites/spaceship/center.png')

    def crash(self, dmg=0.02):
        self.health -= dmg
        self.do(Blink(10, 1) + Show())

    @classmethod
    def get_position(cls):
        """ Return the position of the sprite """

        return cls.position


class Enemy(Sprite):

    """ Gereneric representation for spaceship enemies. """

    def __init__(self, arg):
        super(Enemy, self).__init__(arg)
        self.velocity = (0, 0)
        self.dmg = 0.02


class AeroliteSprite(Enemy):

    """ Apresentation layer to Aerolite """

    def __init__(self, width=WIDTH / 2, height=2 * HEIGHT):
        image = 'sprites/aerolite/aero1.png'
        super(AeroliteSprite, self).__init__(image)

        width = random.randint(0, WIDTH)
        self.scale = 0.15
        self.dmg = 0.04
        self.position = (width, HEIGHT + HEIGHT / 8)
        self.cshape = collision.AARectShape(self.position,
                                            self.width * self.scale * 0.5,
                                            self.height * self.scale * 0.5)
        self.do(AeroliteAction())


class RohenianSprite(Enemy):

    """ Apresentation layer to Rohenian """

    def __init__(self):
        image = "sprites/rohenians/F5S1.png"
        super(RohenianSprite, self).__init__(image)

        width = random.randint(0, WIDTH)
        self.position = (width, HEIGHT)
        self.scale = 0.30
        self.cshape = collision.AARectShape(self.position,
                                            self.width * self.scale * 0.5,
                                            self.height * self.scale * 0.5)
        self.do(RohinianAction())


class Bullet(Sprite):

    """ Gereneric representation for spaceship and rohenians bullets. """

    dmg = 0.0
    sprite_move_action = None

    def __init__(self, image, dmg=0.1):
        super(Bullet, self).__init__(image)
        self.scale = 0.25
        self.dmg = dmg
        self.cshape = collision.AARectShape(self.position,
                                            self.width,
                                            self.height)

    def info(self):
        """ Return some informations from the current bullet. """

        info = "Dmg: %f\nFather: %s\nPosition: %s" % (self.dmg,
                                                      self.father,
                                                      self.position)
        return info + '\n-------------------\n'


class SpaceShipBullet(Bullet):

    """ Apresentation layer to the Spaceship bullet """

    def __init__(self, father=None, dmg=10):
        self.imagem = "sprites/spaceship/fire.png"
        super(SpaceShipBullet, self).__init__(self.imagem, dmg)
        self.velocity = (0, 300)


class RoheniansBullet(Bullet):

    """ Apresentation layer to the Rohenian bullet """

    def __init__(self, dmg=1):
        self.imagem = "sprites/rohenians/fire.png"
        super(RoheniansBullet, self).__init__(self.imagem, dmg)
