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
from cocos import actions
from engine.event import EventHandle
from configs import WIDTH, HEIGHT
import random


class SpaceshipAction(actions.Move):

    # step() is called every frame.
    # dt is the number of seconds elapsed since the last call.

    def step(self, dt):
        max_left = self.target.image.width * self.target.scale / 2
        max_right = WIDTH - self.target.image.width * self.target.scale / 2

        # Run step function on the parent class.
        super(SpaceshipAction, self).step(dt)

        # Determine velocity based on keyboard inputs.
        keyboard = EventHandle().keyboard
        velocity_x = 0
        velocity_y = 0
        velocity_x = 200 * (keyboard[key.RIGHT] - keyboard[key.LEFT])

        if self.target.position[0] < max_left:
            self.target.position = (max_left, 100)

        if self.target.position[0] > max_right:
            self.target.position = (max_right, 100)

        # Set the object's velocity.
        self.target.velocity = (velocity_x, velocity_y)
        if keyboard[key.LEFT]:
            self.target.move_left()
        elif keyboard[key.RIGHT]:
            self.target.move_right()
        else:
            self.target.center_spaceship()

        if keyboard[key.SPACE]:
            print "FIRE THIS MODAFOCKA!!!", dt, self.target.position, max_right


class AeroliteAction(actions.Move):

    def step(self, dt):
        super(AeroliteAction, self).step(dt)

        velocity_x, velocity_y = self.target.velocity
        self.target.velocity = (
            30 * random.randint(-1, 1), random.randint(-80, -50))
        if self.target.position[1] < -self.target.image.height:
            self.target.position = (
                random.randint(0, WIDTH), HEIGHT + self.target.image.height)
