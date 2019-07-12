import wx

class Todolist(wx.Frame):
	"""docstring for todolist"""
	def __init__(self, parent,title):
		super(Todolist, self).__init__(parent,title=title,\
			size=(800,500))
		self.Center()
		panel=wx.Panel(self)

		vbox=wx.BoxSizer(wx.HORIZONTAL)

		#第一个模块
		vbox1=wx.BoxSizer(wx.VERTICAL)
		self.list=['my day','important','plan','taxt']
		lb2=wx.ListBox(panel,1,choices=self.list,\
			pos=(0,0),size=(170,563),style=wx.LB_SINGLE)
		vbox1.Add(lb2,2,wx.EXPAND | wx.ALL,0)
		#添加新的块
		vbox.Add(vbox,1,flag=wx.EXPAND|wx.LEFT)

		# vbox.Add(10,-1)

		#第二个模块
		vbox2=wx.BoxSizer(wx.VERTICAL)
		textctrl1 = wx.TextCtrl(panel,pos=(171,0),size=(630,100),style=wx.TE_MULTILINE)
		textctrl2 = wx.TextCtrl(panel,pos=(171,101),size=(630,463),style=wx.TE_MULTILINE)
		vbox2.Add(textctrl2,1,flag=wx.EXPAND)

		vbox2.Add(textctrl1,1,flag=wx.EXPAND)
		vbox.Add(vbox2,1,border=10)

		self.Show()


app=wx.App()
todolist=Todolist(None,"todolistnewm")
app.MainLoop()