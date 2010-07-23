import wx


def dialogMessage(title, message):
	dlg = wx.MessageDialog(None, message, caption=title, style=wx.OK|wx.CENTRE )
	dlg.ShowModal()
	dlg.Destroy()


def dialogChoice(title, question, choices):
	#TODO add buttons based option
	dlg = wx.SingleChoiceDialog(None, question, title, choices, wx.CHOICEDLG_STYLE )
	if dlg.ShowModal() == wx.ID_OK:
		value = dlg.GetStringSelection()
	else:
		value = None
	dlg.Destroy()
	return value
