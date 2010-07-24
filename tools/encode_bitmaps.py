#!/usr/bin/env python

"""
This is a way to save the startup time when running img2py on lots of
files...
"""

import os, sys
from wx.tools import img2py


command_lines = [
	"-u -c -n Magnet32 ../resources/images/Magnet-32.png ../src/magnetism_core/images.py",
	"-a -u -c -n Magnet64 ../resources//images/Magnet-64.png ../src/magnetism_core/images.py",
	"-a -u -c -n Cogs ../resources//images/system-run.png ../src/magnetism_core/images.py",
]


def main(buildRoot=False):
	if buildRoot:
		path = os.getcwd()
		os.chdir(buildRoot)

	print "building resource file images.py"
	for line in command_lines:
		args = line.split()
		img2py.main(args)

	if buildRoot:
		os.chdir(path)


if __name__ == "__main__":
	main()
