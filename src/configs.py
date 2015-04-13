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
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'src/data')

FONT = {'header': 'Orbitron',
        'header_size': 60,
        'body': 'Titillium Web',
        'body_size': 32,
        'body_size_small': 20,
        'body_size_selected': 46,
        'gray': (32, 16, 32, 255),
        'white': (255, 255, 255, 255)}

WIDTH = 800
HEIGHT = 600
