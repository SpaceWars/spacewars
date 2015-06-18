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

from cocos.actions import MoveTo
from cocos.scene import Scene
from configs import WIDTH, HEIGHT
from engine.enemy import EnemyFactory
from engine.gunfire import FireFactory
from game.sprites import SpaceShipSprite
from itertools import cycle
from layers.base_layers import BackgroundLayer
from pyglet import clock
import random


class GameScene(Scene):

    def __init__(self):
        super(GameScene, self).__init__()
        self.background = BackgroundLayer('backgrounds/bluespace.png')
        self.spaceship = SpaceShipSprite()
        EnemyFactory.populate_enemy("Aerolite", qnt=15)
        EnemyFactory.populate_enemy("Rohenian", qnt=15)
        self.aerolites = EnemyFactory.create_enemy("Aerolite", 5)
        self.rohenians = EnemyFactory.create_enemy("Rohenian", 10)
        self.__recharge()
        clock.schedule_interval(self.__set_direction, .8)

    def __recharge(self):
        FireFactory.create_bullets('hero', qnt=90)
        bullets = FireFactory().delivery_bullets(
            'hero', 90, target=self.spaceship)
        self.spaceship.bullets = cycle(bullets)

    def new_game(self):
        self.add(self.background, z=0)
        self.add(self.spaceship)

        for aero in self.aerolites:
            width = random.randint(0, WIDTH)
            aero.do(MoveTo((width, -aero.image.height), random.randint(7, 15)))
            self.add(aero)

        for rohenian in self.rohenians:
            width = random.randint(-WIDTH, 2 * WIDTH)
            rohenian.do(
                MoveTo((width, -rohenian.image.height), random.randint(5, 8)))
            self.add(rohenian)

        return self

    def __set_direction(self, *args):

        for rohenian in self.rohenians:
            if rohenian.position[1] < 0:
                rohenian.position = (random.randint(0, WIDTH), HEIGHT)
            width = random.randint(-WIDTH, WIDTH)
            rohenian.do(
                MoveTo((width, -rohenian.image.height), random.randint(5, 8)))
