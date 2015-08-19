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
import cocos.collision_model as collision
import random

from cocos.actions import MoveTo
from cocos.scene import Scene
from configs import WIDTH
from engine.action import FireAction
from engine.enemy import EnemyFactory
from engine.gunfire import FireFactory
from game.sprites import SpaceShipSprite
from layers.base_layers import BackgroundLayer
from pyglet import clock
from cocos.director import director
from cocos import text
from configs import FONT


class GameScene(Scene):

    def __init__(self):
        super(GameScene, self).__init__()
        self.background = BackgroundLayer('backgrounds/bluespace.png')
        self.spaceship = SpaceShipSprite()
        EnemyFactory.populate_enemy("Aerolite", qnt=15)
        EnemyFactory.populate_enemy("Rohenian", qnt=15)
        self.aerolites = EnemyFactory.create_enemy("Aerolite", 10)
        self.rohenians = EnemyFactory.create_enemy("Rohenian", 5)
        self.isrecharged = False
        self.__recharge()

        self.collision_manager = collision.CollisionManagerBruteForce()
        self.__collision_manager_add()

        self.schedule(self.check_collisions)

        clock.schedule_interval(self.__check_buttons, .15)

        self.show_bullets_string()
        self.show_hp_string()

        self.new_game()

    def show_bullets_string(self):
        self.bullets_string = text.Label(
            '',
            font_name=FONT['body'],
            font_size=16,
            anchor_x='center', anchor_y='center',
            position=(WIDTH - 16 * 5, 40),
            color=(225, 225, 225, 225),
        )
        self.bullets_string.element.text = "Bullets: %03d" % len(
            self.spaceship.bullets)

    def show_hp_string(self):
        self.hp_string = text.Label(
            '',
            font_name=FONT['body'],
            font_size=16,
            anchor_x='center', anchor_y='center',
            position=(80, 40),
            color=(225, 225, 225, 225),
        )
        self.hp_string.element.text = "Health: 100%"

    def check_collisions(self, dt):
        if self.spaceship.health < 0:
            director.pop()
        else:
            health = self.spaceship.health / 5
            self.hp_string.element.text = "Health: " + str(health * 100) + "%"

        ship_collisions = self.collision_manager.objs_colliding(self.spaceship)
        if ship_collisions:
            self.__spaceship_rohinian_collision(ship_collisions)
            self.__spaceship_aerolite_collision(ship_collisions)

        self.__bullet_collisions()

    def __bullet_collisions(self):
        for bullet in self.spaceship.bullets_used:
            collisions = self.collision_manager.objs_colliding(bullet)
            self.__bullet_rohinian_collision(collisions, bullet)
            self.__bullet_aerolite_collision(collisions, bullet)

    def __bullet_rohinian_collision(self, collisions, bullet):
        for rohenian in self.rohenians:
            if rohenian in collisions:
                try:
                    self.remove(rohenian)
                    self.rohenians.remove(rohenian)
                    del rohenian
                    self.remove(bullet)
                    self.spaceship.bullets_used.remove(bullet)
                    del bullet
                except:
                    pass

    def __bullet_aerolite_collision(self, collisions, bullet):
        for aerolite in self.aerolites:
            if aerolite in collisions:
                try:
                    self.remove(aerolite)
                    self.aerolites.remove(aerolite)
                    del aerolite
                    self.remove(bullet)
                    self.spaceship.bullets_used.remove(bullet)
                    del bullet
                except:
                    pass

    def __spaceship_rohinian_collision(self, collisions):
        for rohenian in self.rohenians:
            if rohenian in collisions:
                self.spaceship.crash()

    def __spaceship_aerolite_collision(self, collisions):
        for aerolite in self.aerolites:
            if aerolite in collisions:
                self.spaceship.crash(aerolite.dmg)

    def new_game(self):
        """ Create a new game scene, and add some elements in scene, like the
        rohenians, aerolites and spaceship. """

        self.add(self.background, z=0)
        self.add(self.spaceship, z=3)
        self.add(self.bullets_string, z=4)
        self.add(self.hp_string, z=4)

        for aero in self.aerolites:
            # Set a randomic  initial position to aerolites
            width = random.randint(0, WIDTH)
            aero.do(MoveTo((width, -aero.image.height), random.randint(7, 15)))
            self.add(aero, z=1)

        for rohenian in self.rohenians:
            # Set a randomic  initial position to rohinians
            width = random.randint(-WIDTH, 2 * WIDTH)
            rohenian.do(
                MoveTo((width, -rohenian.image.height), random.randint(5, 8)))
            self.add(rohenian, z=1)

        return self

    def __check_buttons(self, *args):
        from engine.event import EventHandle
        from pyglet.window import key

        joystick = EventHandle().joystick
        keyboard = EventHandle().keyboard
        if not len(self.rohenians):
            print 'new game!'
            # self.end()

        if joystick is not None:
            if EventHandle()['Select'] is True:
                director.show_FPS = not director.show_FPS
                print director.show_FPS
            elif EventHandle()['Start'] is True:
                print "Show Options"
            elif EventHandle()['R3'] is True:
                self.__recharge()
                self.isrecharged = True
                self.bullets_string.element.text = "Bullets: %03d" % len(
                    self.spaceship.bullets)
            elif (True in joystick.buttons) or (joystick.rz != -1):
                self.__set_bullet_time()

        if keyboard[key.SPACE]:
            self.__set_bullet_time()
        elif keyboard[key.ENTER]:
            print "Show Options"

    def __set_bullet_time(self):
        try:
            bullet_time = self.spaceship.bullets.pop()
        except IndexError:
            return
            # self.__recharge()
            bullet_time = self.spaceship.bullets.pop()
        self.spaceship.bullets_used.append(bullet_time)
        bullet_time.stop()
        bullet_time.position = self.spaceship.position
        try:
            self.remove(bullet_time)
        except Exception:
            pass
        self.add(bullet_time, z=2)
        bullet_time.do(FireAction())
        self.bullets_string.element.text = "Bullets: %03d" % len(
            self.spaceship.bullets)

    def __recharge(self):
        """ Recharge the spaceship weapon, requesting new bullets to the
        engine.gunfire.FireFactory"""
        if self.isrecharged:
            return
        FireFactory.create_bullets('hero', qnt=200)
        bullets = FireFactory().delivery_bullets(
            'hero', 100, target=self.spaceship)
        self.spaceship.bullets += bullets
        print 'Recharged'

    def __collision_manager_add(self):
        """ Add sprites into collision manager to listen to collisions """

        self.collision_manager.add(self.spaceship)

        for rohenian in self.rohenians:
            self.collision_manager.add(rohenian)

        for aerolite in self.aerolites:
            self.collision_manager.add(aerolite)

        for bullet in self.spaceship.bullets:
            self.collision_manager.add(bullet)
