import wx

class Todolist(wx.Frame):
	"""docstring for todolist"""
	def __init__(self, parent,title):
		super(Todolist, self).__init__(parent,title=title,\
			size=(800,522))
		self.Center()

		#创建控件和布局的承载页面
		self.panel=wx.Panel(self)

		#创建整个布局
		vbox=wx.BoxSizer(wx.HORIZONTAL)

		#第一个模块
		#垂直添加第一个模块
		vbox1=wx.BoxSizer(wx.VERTICAL)
		vbox2 = wx.BoxSizer(wx.VERTICAL)
		#创建列表与LiseBox类
		self.list=['my day','important','plan','taxt']
		self.lb2=wx.ListBox(self.panel,1,choices=self.list,\
			pos=(0,0),size=(170,463),style=wx.LB_SINGLE)
		#对ListBox类添加事件，是右上响应左侧变化
		self.Bind(wx.EVT_LISTBOX,self.on_listbox,self.lb2)
		#实现添加选项,对Button类添加事件
		self.button=wx.Button(self.panel,-1,label='+Add',\
			pos=(50,463),size=(120,20))
		self.Bind(wx.EVT_BUTTON,self.on_creat,self.button)
		#将控件添加到左侧布局内
		vbox1.Add(self.lb2,2,wx.EXPAND | wx.ALL,0)
		vbox1.Add(self.button,2,wx.EXPAND | wx.ALL,0)
		#添加左侧布局到整个布局上
		vbox.Add(vbox1,1,flag=wx.EXPAND|wx.LEFT)

		#第二个模块
		vbox2 = wx.BoxSizer(wx.VERTICAL)

		#上半部分
		#textctrl1 = wx.TextCtrl(panel,pos=(171,0)\
			#,size=(630,100),style=wx.TE_MULTILINE)
		self.todo_title = wx.StaticText(self.panel,label='title',pos=(171,0)\
			,size = (630,100))
		vbox2.Add(self.todo_title,1,flag=wx.EXPAND)

		#下半部分
		textctrl2 = wx.TextCtrl(self.panel,pos=(171,101)\
			,size=(630,463),style=wx.TE_MULTILINE)
		vbox2.Add(textctrl2,1,flag=wx.EXPAND)


		vbox.Add(vbox2,1,border=10)

		self.Show()

	def on_listbox(self,event):
		'''在右上显示左侧选项，一一对应'''
		#panel=wx.Panel(self)
		self.todo_title.SetLabelText(event.GetString())
		#textctrl2 = wx.TextCtrl(self.panel,pos=(171,101)\
		# 	,size=(630,463),style=wx.TE_MULTILINE)

	def on_creat(self,event):
		'''该方法获得在窗口内输入的值并返回，返回的
			即为用户输入的字符串'''
		awindow=wx.TextEntryDialog(None,\
			"enter/change the thing you want to do")
		if awindow.ShowModal()==wx.ID_OK:
			return_value=awindow.GetValue()
			self.list.append(return_value)
			return return_value



app=wx.App()
todolist=Todolist(None,"todolistnewm")
app.MainLoop()