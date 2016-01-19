#!/usr/bin/env python
"""
SpaceWars
===================
A nice game
"""
from setuptools import setup, find_packages

install_requires = [
    'cocos2d==0.6.0',
    'pyglet==1.2.4',
    'six==1.9.0',
    'future>=0.15.0',
    'Sphinx==1.3.3',
    'sphinx-rtd-theme==0.1.9',
]

tests_require = ['mock']


setup(
    name="SpaceWars",
    version='0.1.2',
    author='Matheus Fernandes, Luiz Oliveira, Carlos Oliveira',
    author_email='matheus.souza.fernandes@gmail.com, ziuloliveira@gmail.com',
    url='git@github.com:SpaceWars/spacewars.git',
    entry_points={
        'console_scripts': [
            'spacewars = main:main',
        ]},
    description='A game',
    long_description=__doc__,
    license='GPLv3',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    package_data={'src':
                  [
                      'data/backgrounds/*',
                      'data/fonts/*',
                      'data/sound/*.wav',
                      'data/sprites/aerolite/*',
                      'data/sprites/alienbomb/*',
                      'data/sprites/planets/*',
                      'data/sprites/rohenians/*',
                      'data/sprites/spaceship/*',
                  ]},
    zip_safe=True,
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        'Environment :: Cocos2D',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3',
        'Topic :: Utilities',
    ],
)
