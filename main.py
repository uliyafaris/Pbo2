import wx
import helloWx

class  subClass(helloWx.MyFrame1):
	def __init__(self, parent):
		helloWx.MyFrame1.__init__(self, parent)
	def m_button1OnButtonClick( self, event ):
		print('Nama : Uliya istiq f')
		print('Nim : 192410101012')

app = wx.App()
frame = subClass(parent = None)
frame.Show()
app.MainLoop()
