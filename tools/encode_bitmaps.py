#!/usr/bin/env python

"""
This is a way to save the startup time when running img2py on lots of
files...
"""

import sys
from wx.tools import img2py


command_lines = [
	"-u -c -n Magnet32 ../resources/images/Magnet-32.png ../src/magnetism_core/images.py",
	"-a -u -c -n Magnet64 ../resources//images/Magnet-64.png ../src/magnetism_core/images.py",
	"-a -u -c -n Cogs ../resources//images/system-run.png ../src/magnetism_core/images.py",
]


def main():
	for line in command_lines:
		args = line.split()
		img2py.main(args)


if __name__ == "__main__":
	main()
