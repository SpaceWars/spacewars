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
from itertools import cycle
import cocos.collision_model as collision
import random

from cocos.actions import MoveTo
from cocos.scene import Scene
from configs import WIDTH, HEIGHT
from engine.enemy import EnemyFactory
from engine.gunfire import FireFactory
from game.sprites import SpaceShipSprite
from layers.base_layers import BackgroundLayer
from pyglet import clock


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

        self.collision_manager = collision.CollisionManagerBruteForce()
        self.__collision_manager_add()

        self.schedule(self.check_collisions)

        clock.schedule_interval(self.__set_direction, .8)

    def check_collisions(self, dt):
        # print self.collision_manager.known_objs()
        collisions = self.collision_manager.objs_colliding(self.spaceship)
        if collisions:
            # print "COLIDIU PORRAAAA"
            for rohenian in self.rohenians:
                if rohenian in collisions:
                    print "COLIDIU COM UM ROHINIANO!!!"
                    print rohenian

            for aerolite in self.aerolites:
                if aerolite in collisions:
                    print "COLIDIU COM UM AEROLITOOO!!!"
                    print aerolite

    def new_game(self):
        """ Create a new game scene, and add some elements in scene, like the
        rohenians, aerolites and spaceship. """

        self.add(self.background, z=0)
        self.add(self.spaceship, z=2)

        for aero in self.aerolites:
            # Set a randomic  initial position to aerolites
            width = random.randint(0, WIDTH)
            aero.do(MoveTo((width, -aero.image.height), random.randint(7, 15)))
            self.add(aero, z=2)

        for rohenian in self.rohenians:
            # Set a randomic  initial position to rohinians
            width = random.randint(-WIDTH, 2 * WIDTH)
            rohenian.do(
                MoveTo((width, -rohenian.image.height), random.randint(5, 8)))
            self.add(rohenian, z=2)

        return self

    def __recharge(self):
        """ Recharge the spaceship weapon, requesting new bullets to the
        engine.gunfire.FireFactory"""

        FireFactory.create_bullets('hero', qnt=90)
        bullets = FireFactory().delivery_bullets(
            'hero', 90, target=self.spaceship)
        self.spaceship.bullets = cycle(bullets)

    def __set_direction(self, *args):
        """ To difficult the game, the rohinians change their directions
        randomly, in this method. """

        for rohenian in self.rohenians:
            if rohenian.position[1] < 0:
                rohenian.position = (random.randint(0, WIDTH), HEIGHT)
            width = random.randint(-WIDTH, WIDTH)
            rohenian.do(
                MoveTo((width, -rohenian.image.height), random.randint(5, 8)))

    def __collision_manager_add(self):
        """ Add sprites into collision manager to listen to collisions """

        self.collision_manager.add(self.spaceship)

        for rohenian in self.rohenians:
            self.collision_manager.add(rohenian)

        for aerolite in self.aerolites:
            self.collision_manager.add(aerolite)
