#!/usr/bin/python
# -*- coding:utf-8 -*-

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

# from game.sprites import Bullets

from cocos.sprite import Sprite


class Bullets(Sprite):

    """docstring for Bullet"""

    def __init__(self):
        pass


hero = ['Spaceship', 'spaceship', 'hero', 'player']
rohenian = ['Rohenian', 'rohenian', 'enemies', 'ro']


class FireFactory(object):

    """docstring for FireFactory"""

    ammo = {'hero': [], 'enemies': []}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(FireFactory, cls).__new__(cls)
        return cls.instance

    @classmethod
    def create_bullets(cls, bullet_type, qnt=50):
        if bullet_type in hero:
            for x in xrange(0, qnt):
                cls.ammo['hero'].append(Bullets())
        elif bullet_type in rohenian:
            for x in xrange(0, qnt):
                cls.ammo['enemies'].append(Bullets())

    @classmethod
    def delivery_bullets(cls, bullet_type, qnt=50):
        if len(cls.ammo[bullet_type]) < qnt:
            cls.create_bullets(
                bullet_type, qnt - len(cls.ammo[bullet_type]))

        if bullet_type in hero:
            return_list = cls.ammo["hero"][:qnt]
            cls.ammo["hero"] = cls.ammo["hero"][qnt:]
            return return_list
        elif bullet_type in rohenian:
            return_list = cls.ammo["enemies"][:qnt]
            cls.ammo["enemies"] = cls.ammo["enemies"][qnt:]
            return return_list

    @classmethod
    def many_ammo(cls):
        ret = ''
        for key in cls.ammo:
            ret += "%s: %d\n" % (key, len(cls.ammo[key]))
        return ret

if __name__ == '__main__':
    print FireFactory.many_ammo()
    FireFactory.create_bullets('hero', 300)
    print FireFactory.many_ammo()
    FireFactory.create_bullets('ro', 30)
    FireFactory.delivery_bullets('hero', 150)
    print FireFactory.many_ammo()
    FireFactory.create_bullets('enemies', 3)
    print FireFactory.many_ammo()
