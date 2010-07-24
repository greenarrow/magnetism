#!/usr/bin/env python


import os


def main(buildRoot=False):
	if buildRoot:
		path = os.getcwd()
		os.chdir(buildRoot)

	print "building resource file xrcdata.py"
	xml = open("../resources/magnetism.xrc").read()
	pycode = 'xml = \"\"\"%s\"\"\"' % xml
	open("../src/magnetism_core/xrcdata.py", "w").write(pycode)

	if buildRoot:
		os.chdir(path)


if __name__ == "__main__":
	main()
