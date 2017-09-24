#!/usr/bin/env python
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
from game.sprites import SpaceShipBullet, RoheniansBullet

hero = ['Spaceship', 'spaceship', 'hero', 'player']
rohenian = ['Rohenian', 'rohenian', 'enemies', 'ro']


class FireFactory(object):

    """Create Bullets. FireFactory can create SpaceShip and Rohenians bullets.

    To create Spaceship bullets: FireFactory.delivery_bullets('spaceship'). By
    default, it returns a list with 50 bullets.

    To create Rohenians bullets: FireFactory.delivery_bullets('rohenian'). By
    default, it returns a list with 50 bullets."""

    ammo = {'hero': [], 'enemies': []}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(FireFactory, cls).__new__(cls)
        return cls.instance

    @classmethod
    def clear(cls):
        for i in cls.ammo['hero']:
            i.stop()
            del i
        for i in cls.ammo['enemies']:
            i.stop()
            del i
        del cls.ammo
        cls.ammo = {'hero': [], 'enemies': []}

    @classmethod
    def create_bullets(cls, bullet_type, qnt=50):
        """ Populate a pool of objects, maybe of SpaceShipBullet or
        RoheniansBullet"""

        if bullet_type in hero:
            for x in range(0, qnt):
                cls.ammo['hero'].append(SpaceShipBullet())
        elif bullet_type in rohenian:
            for x in range(0, qnt):
                cls.ammo['enemies'].append(RoheniansBullet())

    @classmethod
    def delivery_bullets(cls, bullet_type, qnt=50, target=None):
        """ Returns a list of a specific bullet type. The bullet type is a
        mandatory parameter and can be 'spaceship like' or 'rohenian like'"""

        if len(cls.ammo[bullet_type]) < qnt:
            cls.create_bullets(
                bullet_type, int(qnt) - len(cls.ammo[bullet_type]))

        if bullet_type in hero:
            return_list = cls.ammo["hero"][:qnt]
            cls.ammo["hero"] = cls.ammo["hero"][qnt:]
        elif bullet_type in rohenian:
            return_list = cls.ammo["enemies"][:qnt]
            cls.ammo["enemies"] = cls.ammo["enemies"][qnt:]

        for i in return_list:
            i.father = target
            i.position = target.position
        return return_list

    @classmethod
    def many_ammo(cls):
        """ Returns a status of the pool of objets """

        ret = ''
        for key in cls.ammo:
            ret += "%s: %d\n" % (key, len(cls.ammo[key]))
        return ret

if __name__ == '__main__':
    print(FireFactory.many_ammo())
    FireFactory.create_bullets('hero', 300)
    print(FireFactory.many_ammo())
    FireFactory.create_bullets('ro', 30)
    FireFactory.delivery_bullets('hero', 150)
    print(FireFactory.many_ammo())
    FireFactory.create_bullets('enemies', 3)
    print(FireFactory.many_ammo())
