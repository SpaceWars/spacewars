#!/usr/bin/python
# -*- coding:utf-8 -*-

from cocos.director import Director


class Director(Director):

    """Singleton for Director"""

    # _shared_state = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Director, cls).__new__(cls)
        return cls.instance

director = Director()
