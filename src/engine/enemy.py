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
from game.sprites import AeroliteSprite as Aerolite
from game.sprites import RohenianSprite as Rohenian

rohenian = ['Rohenian', 'rohenian', 'enemies', 'ro']
aerolite = ['Aerolite', 'aerolite', 'aero', 'pedra', 'meteoro']


class EnemyFactory(object):

    """ Create enemies. EnemyFactory can create Rohenian and Aerolites enemies.
    To create Rohenian enemy: EnemyFactory.create_enemy('Rohenian', [qnt=1])
    To create Aerolite enemy: EnemyFactory.create_enemy('Aerolite', [qnt=1])"""

    enemy_list = {"Rohenian": [], "Aerolite": []}

    def __new__(cls):
        # Singleton instance
        if not hasattr(cls, 'instance'):
            cls.instance = super(EnemyFactory, cls).__new__(cls)
        cls.is_empty = True
        return cls.instance

    @classmethod
    def populate_enemy(cls, enemy_type, qnt=1):
        """ Populate pool of objects """

        if enemy_type in rohenian:
            for x in range(0, qnt):
                cls.enemy_list["Rohenian"].append(
                    Rohenian())
            cls.is_empty = False
            return
        if enemy_type in aerolite:
            for x in range(0, qnt):
                cls.enemy_list["Aerolite"].append(
                    Aerolite())
            cls.is_empty = False
            return
        assert 0, "Bad enemy creation: " + enemy_type

    @classmethod
    def return_enemy_list(cls):
        return cls.enemy_list

    @classmethod
    def clear(cls):
        for i in cls.enemy_list['Rohenian']:
            i.stop()
            del i
        for i in cls.enemy_list['Aerolite']:
            i.stop()
            del i
        del cls.enemy_list
        cls.enemy_list = {"Rohenian": [], "Aerolite": []}

    @classmethod
    def create_enemy(cls, enemy_type, qnt=1):
        if len(cls.enemy_list[enemy_type]) < qnt:
            cls.populate_enemy(
                enemy_type, qnt - len(cls.enemy_list[enemy_type]))

        if enemy_type in rohenian:
            return_list = cls.enemy_list["Rohenian"][:qnt]
            cls.enemy_list["Rohenian"] = cls.enemy_list["Rohenian"][qnt:]
            if len(cls.enemy_list[enemy_type]) is 0:
                cls.is_empty = True
            return return_list
        if enemy_type in aerolite:
            return_list = cls.enemy_list["Aerolite"][:qnt]
            cls.enemy_list["Aerolite"] = cls.enemy_list["Aerolite"][qnt:]
            if len(cls.enemy_list[enemy_type]) is 0:
                cls.is_empty = True
            return return_list
        assert 0, "Bad enemy creation: " + enemy_type


if __name__ == '__main__':
    print(EnemyFactory.return_enemy_list())
    EnemyFactory.populate_enemy("Aerolite", qnt=5)
    EnemyFactory.populate_enemy("Rohenian", qnt=5)
    print(EnemyFactory.return_enemy_list())

    b = EnemyFactory.create_enemy("Aerolite", 10)
    print(len(b))
    print(EnemyFactory.return_enemy_list())
    a = EnemyFactory.create_enemy("Rohenian")
    print(a[0].say())
    print(EnemyFactory.return_enemy_list())
