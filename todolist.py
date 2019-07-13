import wx

class ToDoList(wx.Frame):
	"""docstring for todolist"""
	def __init__(self, parent,title):
		super(ToDoList, self).__init__(parent,title=title,\
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
		#添加五个button
		#实现添加选项,对Button类添加事件
		liststr=["my day","important","plan","taxt"]
		number = 0
		self.button_list = [ None for i in range(len(liststr))]
		for strstr in liststr:
			self.button_list[number] = wx.Button(self.panel,-1,label=strstr,pos=(0,number*40),size=(170,40))
			number+=1
		self.button_add=wx.Button(self.panel,-1,label='+Add',\
			pos=(0,443),size=(170,40))
		#.Bind(wx.EVT_BUTTON,self.on_creat,self.button)
		#将控件添加到左侧布局内
		#.Add(self.lb2,2,wx.EXPAND | wx.ALL,0)

		for num in range(len(liststr)) :
			vbox1.Add(self.button_list[num],2,wx.EXPAND | wx.ALL,0)
		vbox1.Add(self.button_add,2,wx.EXPAND | wx.ALL,0)
		#添加左侧布局到整个布局上
		vbox.Add(vbox1,1,flag=wx.EXPAND|wx.LEFT)

		#第二个模块
		vbox2 = wx.BoxSizer(wx.VERTICAL)

		#上半部分
		#textctrl1 = wx.TextCtrl(panel,pos=(171,0)\
			#,size=(630,100),style=wx.TE_MULTILINE)
		self.todo_title = wx.StaticText(self.panel,pos=(171,0),label='title'\
			,size = (630,100))
		vbox2.Add(self.todo_title,1,flag=wx.EXPAND)

		#下半部分
		#textctrl2 = wx.TextCtrl(self.panel,pos=(191,101)\
		#	,size=(170,-1),style=wx.TE_MULTILINE)
		self.list_right_real=['1','2','3','4']
		self.lb3=wx.ListBox(self.panel,1,choices=self.list_right_real,\
			pos=(171,101),size=(630,424))
		vbox2.Add(self.lb3,1,flag=wx.EXPAND)


		vbox.Add(vbox2,1,border=10)

		self.Show()

app=wx.App()
todolist=ToDoList(None,"todolistnewm")
app.MainLoop()