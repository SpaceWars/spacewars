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
from cocos.actions import MoveTo, MoveBy, Repeat
from configs import WIDTH, HEIGHT
import random


class GameScene(Layer):
    is_event_handler = True

    def __init__(self):
        super(GameScene, self).__init__()
        self.background = BackgroundLayer('backgrounds/bluespace.png')
        self.spaceship = SpaceShipSprite()
        EnemyFactory.populate_enemy("Aerolite", qnt=15)
        EnemyFactory.populate_enemy("Rohenian", qnt=15)
        self.aerolites = EnemyFactory.create_enemy("Aerolite", 5)
        self.rohenians = EnemyFactory.create_enemy("Rohenian", 10)
        clock.schedule_interval(self.re_launch_aero, 15)
        clock.schedule_interval(self.re_launch_rohenian, 35)
        clock.schedule_interval(self.set_direction, .8)

    def re_launch_aero(self, *arg):
        print 'new wave Aerolite', arg
        for aero in self.aerolites:
            aero.position = (random.randint(0, WIDTH), HEIGHT + HEIGHT / 8)
            aero.do(
                MoveTo((random.randint(0, WIDTH), -aero.image.height), random.randint(7, 15)))
        director.scene = self.set_direction()

    def re_launch_rohenian(self, *arg):
        print 'new wave Rohenian', arg
        for rohenian in self.rohenians:
            rohenian.position = (random.randint(0, WIDTH), HEIGHT)
        director.scene = self.set_direction()

    def new_game(self):
        scene = Scene()

        scene.add(self.background, z=0)
        scene.add(self)
        scene.add(self.spaceship)

        for aero in self.aerolites:
            width = random.randint(0, WIDTH)
            aero.do(MoveTo((width, -aero.image.height), random.randint(7, 15)))
            scene.add(aero)

        for rohenian in self.rohenians:
            width = random.randint(-WIDTH, 2 * WIDTH)
            rohenian.do(MoveTo((0, rohenian.image.height), 20.5))
            scene.add(rohenian)

        return scene

    def set_direction(self, *args):
        scene = Scene()
        scene.add(self.background, z=0)
        scene.add(self)
        scene.add(self.spaceship)

        for rohenian in self.rohenians:
            print rohenian.position
            if rohenian.position[1] < -rohenian.image.height * 0.7:
                # self.rohenians.remove(rohenian)
                pass
            else:
                width = random.randint(-WIDTH, WIDTH)
                rohenian.do(
                    MoveBy((width, -rohenian.image.height), random.randint(8, 13)))
                scene.add(rohenian)
        print len(self.rohenians)

        for aero in self.aerolites:
            # width = random.randint(-WIDTH, WIDTH)
            # aero.do(MoveTo((width, -aero.image.height), 7.5))
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
            clock.unschedule(self.re_launch_aero)
            clock.unschedule(self.re_launch_rohenian)
            print len(self.aerolites)
        print key.symbol_string(keys)
