#!/usr/bin/env python3

from setuptools import setup

setup (name = 'gites',
	   version = '0.0.1',
	   packages = ['gites'],
	   entry_points = {
		   'console_scripts': [
			   'gites = gites.cli:main'
			   ]
		   })
