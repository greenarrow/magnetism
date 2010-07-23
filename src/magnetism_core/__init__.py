import os, traceback, wx
import scriptools


class ScriptulFileError(Exception):
	pass


class Script():
	title = None
	icon = 'system-run.png'
	code = None

	def __init__(self, filename):
		null, self.filename = os.path.split(filename)
		lines = open(filename, "r").readlines()
		
		for i, l in enumerate(lines):
			if l.startswith("TITLE"):
				self.title = lines[i + 1].strip()
			
			elif l.startswith("ICON"):
				value = lines[i + 1].strip()
				if len(value):
					self.icon = value
			
			elif l.startswith("CODE"):
				self.code = "import magnetism_core.scriptools as magnetism\n" + "\n".join( lines[ i + 1: ] )
				break
		
		if self.title == None or self.icon == None or self.code == None:
			raise ScriptulFileError

	def run(self):
		try:
			exec self.code
		except:
			msg = "There was an error running the script:\n\n" + traceback.format_exc()
			scriptools.dialogMessage(title="Scriptul", message=msg)


