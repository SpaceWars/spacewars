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
from cocos.scene import Scene
from layers.base_layers import BackgroundLayer
from game.sprites import SpaceShipSprite
from engine.enemy import EnemyFactory
from engine.gunfire import FireFactory
from pyglet import clock
from cocos.director import director
from cocos.actions import MoveTo
from configs import WIDTH, HEIGHT
from engine.event import EventHandle
import random
from itertools import cycle


class GameScene(Scene):

    is_event_handler = True

    def __init__(self):
        super(GameScene, self).__init__()
        self.background = BackgroundLayer('backgrounds/bluespace.png')
        self.spaceship = SpaceShipSprite()
        EnemyFactory.populate_enemy("Aerolite", qnt=15)
        EnemyFactory.populate_enemy("Rohenian", qnt=15)
        self.aerolites = EnemyFactory.create_enemy("Aerolite", 5)
        self.rohenians = EnemyFactory.create_enemy("Rohenian", 10)
        self.recharge()
        clock.schedule_interval(self.set_direction, .8)

    def recharge(self):
        FireFactory.create_bullets('hero', qnt=100)
        bullets = FireFactory().delivery_bullets(
            'hero', 100, target=self.spaceship)
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

    def set_direction(self, *args):

        for rohenian in self.rohenians:
            if rohenian.position[1] < 0:
                rohenian.position = (random.randint(0, WIDTH), HEIGHT)
            width = random.randint(-WIDTH, WIDTH)
            rohenian.do(
                MoveTo((width, -rohenian.image.height), random.randint(5, 8)))

    def on_key_press(self, keys, mod):
        if keys == key.ESCAPE:
            clock.unschedule(self.set_direction)
            clock.unschedule(self.re_launch_aero)
            clock.unschedule(self.re_launch_rohenian)
            print len(self.aerolites)
            director.pop()
        elif keys == key.SPACE:
            print "FIRE!!!"

        print key.symbol_string(keys)
        print EventHandle().keyboard
