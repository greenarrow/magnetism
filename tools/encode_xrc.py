#!/usr/bin/env python


def main():
	xml = open("../resources/magnetism.xrc").read()
	pycode = 'xml = \"\"\"%s\"\"\"' % xml
	open("../src/magnetism_core/xrcdata.py", "w").write(pycode)


if __name__ == "__main__":
	main()
