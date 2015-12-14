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
]

tests_require = ['mock']


setup(
    name="spacewars",
    version='0.1.0',
    author='Matheus Fernandes, Luiz Oliveira',
    author_email='matheus.souza.fernandes@gmail.com, ziuloliveira@gmail.com',
    url='https://github.com/msfernandes/python-latex-template',
    entry_points={
        'console_scripts': [
            'spacewars = main:main',
        ]},
    description='A LaTeX generator',
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
        'Environment :: Console',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3',
        'Topic :: Utilities',
    ],
)
