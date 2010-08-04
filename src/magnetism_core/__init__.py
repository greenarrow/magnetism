import os, traceback, wx
import scriptools, images


FILE_EXTENSION = "magnetism"
MAGNETISM_HOME_DIR = ".magnetism"
APP_NAME = "Magnetism"

magnetismHomePath = os.path.join( os.path.expanduser("~"), MAGNETISM_HOME_DIR )
scriptsPath = os.path.join(magnetismHomePath, "scripts")
iconsPath = os.path.join(magnetismHomePath, "icons")


class ScriptulFileError(Exception):
	pass


class Script():
	title = None
	filename = None
	iconFile = None
	bitmap = None
	code = None
	debug = False

	def __init__(self, filename):
		self.filename = filename
		lines = open(filename, "r").readlines()

		for i, l in enumerate(lines):
			if l.startswith("TITLE"):
				self.title = lines[i + 1].strip()

			elif l.startswith("ICON"):
				self.iconFile = lines[i + 1].strip()

				if len(self.iconFile) == 0 or not os.path.isfile( os.path.join(iconsPath, self.iconFile) ):
					self.bitmap = images.getCogsBitmap()

			elif l.startswith("CODE"):
				self.code = "".join( lines[ i + 1: ] )
				break

		if self.title == None or self.code == None:
			raise ScriptulFileError

	def getBitmap(self):
		return self.bitmap

	def loadBitmap(self):
		self.bitmap = wx.Bitmap( os.path.join(iconsPath, self.iconFile) )

	def run(self):
		try:
			code = "import magnetism_core.scriptools as magnetism\nscript = magnetism.ScriptMetaData(title=\"%s\")\n%s" % (self.title, self.code)
			if self.debug:
				print "DEBUG: Executing code:"
				print code
			exec code
		except:
			msg = "There was an error running the script:\n\n" + traceback.format_exc()
			scriptools.dialogMessage(title="Scriptul", message=msg, flags=wx.ICON_ERROR)

	def getExported(self):
		print "TODO: we need to look to see if script is using dialogs and create a [invisible] wx environment if so"
		return "#!/usr/bin/env python\nimport magnetism_core.scriptools as magnetism\n" + self.code

	def getCode(self):
		return self.code

	def setCode(self, code):
		self.code = code

	def save(self):
		text = "TITLE\n%s\nICON\n%s\nCODE\n%s" % (self.title, self.iconFile, self.code)
		f = open(self.filename, "w")
		f.write(text)
		f.close()





