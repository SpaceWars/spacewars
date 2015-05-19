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
from game.sprites import SpaceShipSprite
from engine.enemy import EnemyFactory
from pyglet import clock
from cocos.director import director
from cocos.actions import MoveTo
from configs import WIDTH
import random


class GameScene(Layer):
    is_event_handler = True

    def __init__(self):
        super(GameScene, self).__init__()
        self.background = BackgroundLayer('backgrounds/bluespace.png')
        self.spaceship = SpaceShipSprite()
        EnemyFactory.populate_enemy("Aerolite", qnt=50)
        EnemyFactory.populate_enemy("Rohenian", qnt=50)
        self.aerolites = EnemyFactory.create_enemy("Aerolite", 5)
        self.rohenians = EnemyFactory.create_enemy("Rohenian", 5)
        clock.schedule_interval(self.re_launch, 8)
        clock.schedule_interval(self.set_direction, .8)

    def re_launch(self, *arg):
        print 'new wave', arg
        self.aerolites += EnemyFactory.create_enemy("Aerolite", 5)
        self.rohenians += EnemyFactory.create_enemy("Rohenian", 5)
        director.scene = self.new_game()

    def new_game(self):
        scene = Scene()

        scene.add(self.background, z=0)
        scene.add(self)
        scene.add(self.spaceship)

        for aero in self.aerolites:
            width = random.randint(0, WIDTH)
            aero.do(MoveTo((width, -aero.image.height), 8))
            scene.add(aero)

        for rohenian in self.rohenians:
            width = random.randint(-WIDTH, 3 * WIDTH)
            rohenian.do(MoveTo((width, -rohenian.image.height), 8.5))
            scene.add(rohenian)

        return scene

    def set_direction(self, *args):
        scene = Scene()
        for rohenian in self.rohenians:
            print rohenian.position
            if rohenian.position[1] < 100:
                self.rohenians.remove(rohenian)
            else:
                width = random.randint(-WIDTH, 2 * WIDTH)
                rohenian.do(MoveTo((-width, -rohenian.image.height), 8.5))
                scene.add(rohenian)

        for aero in self.aerolites:
            scene.add(aero)

        return scene

    def on_text_motion(self, keys):
        if keys == key.MOTION_LEFT:
            # print 'Move Spaceship to left'
            self.spaceship.move_left()
        elif keys == key.MOTION_RIGHT:
            # print 'Move Spaceship to rigth'
            self.spaceship.move_rigth()

    def on_key_release(self, keys, mod):
        # print 'Centering spaceship'
        self.spaceship.center_spaceship()

    def on_key_press(self, keys, mod):
        if keys == key.ESCAPE:
            clock.unschedule(self.set_direction)
            clock.unschedule(self.re_launch)
            print len(self.aerolites)
        print key.symbol_string(keys)
