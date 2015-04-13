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
from cocos.sprite import Sprite
from cocos.actions import MoveTo
from configs import WIDTH


class SpaceShipSprite(Sprite):

    def __init__(self):
        image = 'sprites/spaceship/center.png'
        super(SpaceShipSprite, self).__init__(image)

        self.position = (WIDTH / 2, - self.image.height)
        self.scale = 0.35
        self.do(MoveTo((WIDTH / 2, 100), 2))
