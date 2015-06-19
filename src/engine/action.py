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

from cocos import actions
from configs import WIDTH, HEIGHT
from engine.event import EventHandle
from cocos.actions import MoveTo
from pyglet import resource
from pyglet.window import key
from cocos.director import director
# from layers.menu import OptionsMenu


class SpaceshipAction(actions.Move):

    """ Defines the spaceship movement """

    def step(self, dt):
        self.max_left = self.target.image.width * self.target.scale / 2
        self.max_right = WIDTH - self.max_left

        # Run step function on the parent class.
        super(SpaceshipAction, self).step(dt)

        # Run step function on the parent class.
        joystick = EventHandle().joystick
        keyboard = EventHandle().keyboard
        super(SpaceshipAction, self).step(dt)
        self.error = 0.2
        self.speed = 200

        self.__set_velocity_with_keyboard(keyboard)

        if joystick is not None:
            self.__set_velocity_with_joystick(joystick)

            if EventHandle()['Home'] is True:
                director.pop()

        self.__set_movement_image()
        self.__bound_limits()
        self.target.cshape.center = self.target.position

    def __set_velocity_with_keyboard(self, keyboard):
        """ Determine velocity based on keyboard inputs. """

        velocity_x = self.speed * (keyboard[key.RIGHT] - keyboard[key.LEFT])
        velocity_y = self.speed * (keyboard[key.UP] - keyboard[key.DOWN])
        self.target.velocity = (velocity_x, velocity_y)

    def __set_velocity_with_joystick(self, joystick):
        """ Determine velocity based on joystick inputs """

        self.speed = ((joystick.z + 1) * 80) + self.speed
        if (abs(joystick.rx) > self.error) \
           or (abs(joystick.ry) > self.error):
            self.target.velocity = (
                self.speed * joystick.rx, self.speed * -joystick.ry)
        elif (abs(joystick.x) > self.error) \
                or (abs(joystick.y) > self.error):
            self.target.velocity = (
                self.speed * joystick.x, self.speed * -joystick.y)
        elif (abs(joystick.hat_x) > self.error) or \
             (abs(joystick.hat_y) > self.error):
            self.target.velocity = (
                self.speed * joystick.hat_x, self.speed * joystick.hat_y)

    def __set_bullet_time(self):
        bullet_time = self.target.bullets.next()
        bullet_time.stop()
        try:
            if bullet_time.sprite_move_action.done():
                bullet_time.sprite_move_action = actions.MoveTo(
                    (self.target.position[0], HEIGHT * 1.1), 5)
        except Exception:
            bullet_time.sprite_move_action = actions.MoveTo(
                (self.target.position[0], HEIGHT * 1.1), 5)
        bullet_time.position = self.target.position
        try:
            self.target.parent.remove(bullet_time)
        except Exception:
            pass
        self.target.parent.add(bullet_time)
        bullet_time.do(bullet_time.sprite_move_action)

    def __set_movement_image(self):
        """ Changes sprite image depending of spaceship movement """

        if self.target.velocity[0] > 0:
            self.target.image = resource.image(
                'data/sprites/spaceship/right4.png')
        elif self.target.velocity[0] < 0:
            self.target.image = resource.image(
                'data/sprites/spaceship/left4.png')
        else:
            self.target.image = resource.image(
                'data/sprites/spaceship/center.png')

    def __bound_limits(self):
        """ Check if the spaceship is inside a valid position (bottom) """

        if self.target.position[0] < self.max_left:
            self.target.position = (self.max_left, self.target.position[1])
        elif self.target.position[0] > self.max_right:
            self.target.position = (self.max_right, self.target.position[1])

        if self.target.position[1] < self.target.width / 2:
            self.target.position = (
                self.target.position[0], self.target.width / 2)
        elif self.target.position[1] > 200:
            self.target.position = (self.target.position[0], 200)

        for i in self.target.bullets_used:
            if i.position[1] > HEIGHT:
                self.target.parent.remove(i)
                self.target.bullets_used.remove(i)


class AeroliteAction(actions.Move):

    """ Defines the aerolite movement pattern """

    def step(self, dt):
        super(AeroliteAction, self).step(dt)

        velocity_x, velocity_y = self.target.velocity
        self.target.velocity = (
            30 * random.randint(-1, 1), random.randint(-80, -50))
        if self.target.position[1] < -self.target.image.height:
            self.target.position = (
                random.randint(0, WIDTH), HEIGHT + self.target.image.height)
        self.target.cshape.center = self.target.position


class RohinianAction(actions.Move):

    """ Defines the rohinian movement pattern """

    def step(self, dt):
        super(RohinianAction, self).step(dt)
        if self.target.position[1] < 0:
            self.target.position = (random.randint(0, WIDTH), HEIGHT)
            self.target.do(MoveTo((random.randint(0, WIDTH),
                                   - self.target.height),
                                  random.randint(4, 8)))
        self.target.cshape.center = self.target.position


class FireAction(actions.Move):

    """ Defines the fire bullet movement pattern """

    def step(self, dt):
        super(FireAction, self).step(dt)

        self.target.do(MoveTo((self.target.position[0], HEIGHT * 1.1), 2))
        self.target.cshape.center = self.target.position
