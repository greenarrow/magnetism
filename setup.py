#!/usr/bin/env python

from distutils.core import setup

setup(	name='Magnetism',
		version='0.1',
		description='',
		author='Stefan Blanke',
		author_email='greenarrow@',
		url='',

		packages=['magnetism_core'],
		scripts=['src/magnetism'],

		package_dir={'magnetism_core': 'src/magnetism_core'},
)
