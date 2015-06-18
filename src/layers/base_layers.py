#!/usr/bin/python
# -*- coding:utf-8 -*-

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
from cocos.layer import Layer
from pyglet import resource
from pyglet.gl import glPushMatrix, glPopMatrix


class BackgroundLayer(Layer):

    def __init__(self, background):
        super(BackgroundLayer, self).__init__()
        self.image = resource.image(background)

    def draw(self):
        glPushMatrix()
        self.transform()
        self.image.blit(0, 0)
        glPopMatrix()
