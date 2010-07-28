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
	iconFile = None
	bitmap = None
	code = None
	debug = False

	def __init__(self, filename):
		null, self.filename = os.path.split(filename)
		lines = open(filename, "r").readlines()

		for i, l in enumerate(lines):
			if l.startswith("TITLE"):
				self.title = lines[i + 1].strip()

			elif l.startswith("ICON"):
				value = lines[i + 1].strip()
				filename = os.path.join(iconsPath, value)

				if len(value) and os.path.isfile(filename):
					self.iconFile = filename
				else:
					self.bitmap = images.getCogsBitmap()

			elif l.startswith("CODE"):
				self.code = "import magnetism_core.scriptools as magnetism\nscript = magnetism.ScriptMetaData(title=\"%s\")\n" % self.title
				self.code += "".join( lines[ i + 1: ] )
				break

		if self.title == None or self.code == None:
			raise ScriptulFileError

	def getBitmap(self):
		return self.bitmap

	def loadBitmap(self):
		self.bitmap = wx.Bitmap(self.iconFile)

	def run(self):
		try:
			if self.debug:
				print "DEBUG: Executing code"
				print self.code
			exec self.code
		except:
			msg = "There was an error running the script:\n\n" + traceback.format_exc()
			scriptools.dialogMessage(title="Scriptul", message=msg, flags=wx.ICON_ERROR)




