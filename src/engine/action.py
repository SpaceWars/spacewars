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
from pyglet import resource


class SpaceshipAction(actions.Move):

    # step() is called every frame.
    # dt is the number of seconds elapsed since the last call.

    def step(self, dt):
        max_left = self.target.image.width * self.target.scale / 2
        max_right = WIDTH - self.target.image.width * self.target.scale / 2

        # Run step function on the parent class.
        #     super(SpaceshipAction, self).step(dt)

        # Determine velocity based on keyboard inputs.
        #     keyboard = EventHandle().keyboard
        #     velocity_x = 0
        #     velocity_y = 0
        #     velocity_x = 200 * (keyboard[key.RIGHT] - keyboard[key.LEFT])

        # Set the object's velocity.
        #     self.target.velocity = (velocity_x, velocity_y)
        #     if keyboard[key.LEFT]:
        #         self.target.move_left()
        #     elif keyboard[key.RIGHT]:
        #         self.target.move_right()
        #     else:
        #         self.target.center_spaceship()

        #     if keyboard[key.SPACE]:
        # print "FIRE THIS MODAFOCKA!!!", dt, self.target.position, max_right

        # Run step function on the parent class.
        joystick = EventHandle().joystick
        keyboard = EventHandle().keyboard
        super(SpaceshipAction, self).step(dt)
        error = 0.2
        speed = 200

        # Determine velocity based on keyboard inputs.
        velocity_x = speed * (keyboard[key.RIGHT] - keyboard[key.LEFT])
        velocity_y = speed * (keyboard[key.UP] - keyboard[key.DOWN])
        self.target.velocity = (velocity_x, velocity_y)
        if keyboard[key.SPACE]:
            if len(self.target.bullets):
                print "FIRE THIS MODAFOCKA!!!", dt, self.target.position, max_right, self.target.parent
                self.target.parent.add(self.target.bullets[0])
                self.target.bullets[0].position = self.target.position
                self.target.bullets[0].do(actions.Move(10))
                self.target.bullets.remove(self.target.bullets[0])
            else:
                self.target.parent.recharge()

        if joystick is not None:
            speed = ((joystick.rz + 1) * 80) + speed
            if (abs(joystick.rx) > error) or (abs(joystick.ry) > error):
                self.target.velocity = (
                    speed * joystick.rx, speed * -joystick.ry)
            elif (abs(joystick.x) > error) or (abs(joystick.y) > error):
                self.target.velocity = (
                    speed * joystick.x, speed * -joystick.y)
            elif (abs(joystick.hat_x) > error) or (abs(joystick.hat_y) > error):
                self.target.velocity = (
                    speed * joystick.hat_x, speed * joystick.hat_y)
            if (True in joystick.buttons) or (joystick.z != -1) or (joystick.rz != -1):
                print "FIRE THIS MODAFOCKA!!!", joystick.buttons
                self.target.parent.add(self.target.bullets[0])
                self.target.bullets[0].velocity = (0, 50)
                self.target.bullets[0].position = self.target.position
                self.target.bullets[0].do(actions.Move())
                self.target.bullets = self.target.bullets[:0]

        # Set the object's velocity.
        if self.target.velocity[0] > 0:
            self.target.image = resource.image(
                'data/sprites/spaceship/right4.png')
        elif self.target.velocity[0] < 0:
            self.target.image = resource.image(
                'data/sprites/spaceship/left4.png')
        else:
            self.target.image = resource.image(
                'data/sprites/spaceship/center.png')

        if self.target.position[0] < max_left:
            self.target.position = (max_left, self.target.position[1])

        if self.target.position[0] > max_right:
            self.target.position = (max_right, self.target.position[1])

        if self.target.position[1] < self.target.width / 2:
            self.target.position = (
                self.target.position[0], self.target.width / 2)

        if self.target.position[1] > 150:
            self.target.position = (self.target.position[0], 150)


class AeroliteAction(actions.Move):

    def step(self, dt):
        super(AeroliteAction, self).step(dt)

        velocity_x, velocity_y = self.target.velocity
        self.target.velocity = (
            30 * random.randint(-1, 1), random.randint(-80, -50))
        if self.target.position[1] < -self.target.image.height:
            self.target.position = (
                random.randint(0, WIDTH), HEIGHT + self.target.image.height)


class FireAction(actions.Move):

    """docstring for FireAction"""

    def step(self, dt):
        super(FireAction, self).step(dt)

        velocity_x, velocity_y = self.target.velocity
