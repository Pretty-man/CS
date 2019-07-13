import wx

class ToDoList(wx.Frame):
	"""docstring for todolist"""
	def __init__(self, parent,title):
		super(ToDoList, self).__init__(parent,title=title,\
			size=(644,522))
		self.Center()
		#创建控件和布局的承载页面
		self.panel=wx.Panel(self)
		#创建整个布局
		self.vbox=wx.BoxSizer(wx.HORIZONTAL)

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
			self.button_list[number] = wx.Button(self.panel,-1,\
				label=strstr,pos=(0,number*40),size=(170,40))
			number+=1
		self.button_add=wx.Button(self.panel,-1,label='+Add',\
			pos=(0,443),size=(170,40))
		self.Bind(wx.EVT_BUTTON,self.on_creat,self.button_add)
		#self.Bind(wx.EVT_BUTTON,self.on_lift_title,self.button_add)
		#将控件添加到左侧布局内
		for num in range(len(liststr)) :
			vbox1.Add(self.button_list[num],2,wx.EXPAND | wx.ALL,0)
		vbox1.Add(self.button_add,2,wx.EXPAND | wx.ALL,0)
		#添加左侧布局到整个布局上
		self.vbox.Add(vbox1,1,flag=wx.EXPAND|wx.LEFT)

		#第二个模块
		vbox2 = wx.BoxSizer(wx.VERTICAL)
		#上半部分
		#textctrl1 = wx.TextCtrl(panel,pos=(171,0)\
			#,size=(630,100),style=wx.TE_MULTILINE)
		self.todo_title = wx.StaticText(self.panel,pos=(171,0),\
			label='title',size = (474,100))
		vbox2.Add(self.todo_title,1,flag=wx.EXPAND)
		#下半部分
		#textctrl2 = wx.TextCtrl(self.panel,pos=(191,101)\
		#	,size=(170,-1),style=wx.TE_MULTILINE)
		liststr_rdown = [None for  i in range(0)]
		number_rdowm = 0
		self.radio_list = [ None for i in range(len(liststr_rdown))]
		for  str_rdown in liststr_rdown:
			self.radio_list[number_rdowm] = wx.TextCtrl(self.panel,\
				-1,pos=(171,100),value=str_rdown)
			number_rdowm+=1
		for num_rdowm in range(len(liststr_rdown)):
			vbox2.Add(self.radio_list[num],2,wx.EXPAND | wx.ALL,0)
		self.button_add_rdowm = wx.Button(self.panel,-1,label="+Add"\
			,pos=(480,443),size=(170,40))
		self.Bind(wx.EVT_BUTTON,self.on_creat_rdown,self.button_add_rdowm)
		#页面覆盖
		for number_new in range(len(liststr)):
			self.Bind(wx.EVT_BUTTON,self.on_creat_newfile,self.button_list[number_new])
		vbox2.Add(self.button_add_rdowm,2,wx.EXPAND | wx.ALL)
		self.vbox.Add(vbox2,1,flag=wx.EXPAND|wx.LEFT)
		self.Show()

	def on_creat_newfile(self,event):
		#textctrl=wx.TextCtrl(self.panel,pos=(171,100),size=(455,340))
		vbox3 = wx.BoxSizer(wx.VERTICAL)
		liststr_rdown = [None for  i in range(0)]
		number_rdowm = 0
		self.radio_list = [ None for i in range(len(liststr_rdown))]
		for  str_rdown in liststr_rdown:
			self.radio_list[number_rdowm] = wx.TextCtrl(self.panel,\
				-1,pos=(171,100),label=str_rdown)
			number_rdowm+=1
		for num_rdowm in range(len(liststr_rdown)):
			vbox3.Add(self.radio_list[num],2,wx.EXPAND | wx.ALL,0)
		self.button_add_rdowm = wx.Button(self.panel,-1,label="+Add"\
			,pos=(480,443),size=(170,40))
		vbox3.Add(self.button_add_rdowm,2,wx.EXPAND | wx.ALL)
		self.Bind(wx.EVT_BUTTON,self.on_creat_rdown,self.button_add_rdowm)
		self.vbox.Add(vbox3,1,flag=wx.EXPAND|wx.LEFT)

	#添加左侧选项卡
	def on_creat(self,enent):
		enter = wx.TextEntryDialog(self,'enter the plan')
		if enter.ShowModal() == wx.ID_OK:
			return_value=enter.GetValue()
			self.button_list.append(wx.Button(self.panel,-1,\
				label=return_value,pos=(0,len(self.button_list)*40),size=(170,40)))
			return return_value

	#添加右侧选项卡
	def on_creat_rdown(self,event):
		enter = wx.TextEntryDialog(self,'enter the real thing')
		if enter.ShowModal() == wx.ID_OK:
			return_value_rdown=enter.GetValue()
			self.radio_list.append(wx.TextCtrl(self.panel,\
				-1,pos=(191,100+len(self.radio_list)*40),value=return_value_rdown))
			return return_value_rdown


app=wx.App()
todolist=ToDoList(None,"todolistnewm")
app.MainLoop()