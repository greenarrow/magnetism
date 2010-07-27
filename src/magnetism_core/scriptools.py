import wx
import images


BUTTONS = 1
LIST = 2


class ButtonChoiceDialog(wx.Dialog):
	result = None

	def __init__(self, parent, id, title, choices):
		wx.Dialog.__init__(self, parent, id, title)

		vbox = wx.BoxSizer(wx.VERTICAL)

		for choice in choices:
			button = wx.Button( self, -1, choice)
			self.Bind( wx.EVT_BUTTON, self.OnButton, id=button.GetId() )
			vbox.Add(button, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)

		cancelButton = wx.Button(self, -1, 'Cancel')
		self.Bind( wx.EVT_BUTTON, self.OnCancel, id=cancelButton.GetId() )
		vbox.Add(cancelButton, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
		self.SetSizer(vbox)

	def GetStringSelection(self):
		return self.result

	def OnButton(self, event):
		self.result = event.GetEventObject().GetLabel()
		self.Close()

	def OnCancel(self, event):
		self.result = None
		self.Close()


def setIcon(dialog):
	icon = wx.EmptyIcon()
	icon.CopyFromBitmap( images.getMagnet32Bitmap() )
	dialog.SetIcon(icon)


def dialogMessage(message, title="", flags=0):
	dlg = wx.MessageDialog(None, message, caption=title, style=wx.OK|wx.CENTRE|flags )
	setIcon(dlg)
	dlg.ShowModal()
	dlg.Destroy()


def dialogChoice(choices, title="", question="", mode=BUTTONS):
	if mode == BUTTONS:
		dlg = ButtonChoiceDialog(None, -1, title, choices)
		setIcon(dlg)
		dlg.ShowModal()
		value = dlg.GetStringSelection()
		dlg.Destroy()
		return value
	elif mode == LIST:
		dlg = wx.SingleChoiceDialog(None, question, title, choices, wx.CHOICEDLG_STYLE )
		setIcon(dlg)
		if dlg.ShowModal() == wx.ID_OK:
			value = dlg.GetStringSelection()
		else:
			value = None
		dlg.Destroy()
		return value
	else:
		dialogMessage(title=magnetism.APP_NAME, message="Invalid mode for dialogChoice", flags=wx.ICON_ERROR)


def dialogTextEntry(title="", question="", value=""):
	dlg = wx.TextEntryDialog(None, question, title, 'Python')
	setIcon(dlg)
	dlg.SetValue(value)

	if dlg.ShowModal() == wx.ID_OK:
		value = dlg.GetValue()
	else:
		value = None

	dlg.Destroy()
	return value



