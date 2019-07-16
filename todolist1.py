import wx


class ToDoList(wx.Frame):
   

   def __init__(self, parent, title):
      super(ToDoList, self).__init__(parent, title = title, size = (644,522))

class MyPanel1(wx.Panel):
   def __init__(self, parent):
      super(MyPanel1, self).__init__(parent)
      #text = wx.TextCtrl(self, style = wx.TE_MULTILINE, size = (250,150))
      self.button_add=wx.Button(self,-1 ,label="+Add",\
         pos=(100,200),size=(170,40))
      self.Bind(wx.EVT_BUTTON,self.on_creat,self.button_add)

   def on_creat(self,event):
      # mylister=str_list("添加字符串")
      enter = wx.TextEntryDialog(self,'enter the real thing')
      if enter.ShowModal() == wx.ID_OK:
         return_value=enter.GetValue()
         listlist.append(return_value)
         nb.AddPage(MyPanel2(nb),return_value)
         return return_value

class MyPanel2(wx.Panel):
   def __init__(self, parent):
      super(MyPanel2, self).__init__(parent)
      liststr_rdown = [None for  i in range(0)]
      number_rdowm = 0
      self.radio_list = [ None for i in range(len(liststr_rdown))]
      for  str_rdown in liststr_rdown:
         self.radio_list[number_rdowm] = wx.CheckBox(self.panel,\
            -1,pos=(171,100),label=str_rdown)
         number_rdowm+=1
      self.button_add_rdowm = wx.Button(self,-1,label="+Add"\
         ,pos=(450,400),size=(170,40))
      self.Bind(wx.EVT_BUTTON,self.on_creat_rdown,self.button_add_rdowm)
      
   def on_creat_rdown(self,event):
      enter = wx.TextEntryDialog(self,'enter the real thing')
      if enter.ShowModal() == wx.ID_OK:
         return_value_rdown=enter.GetValue()
         self.radio_list.append(wx.CheckBox(self,\
            -1,pos=(191,100+len(self.radio_list)*40),label=return_value_rdown))
         return return_value_rdown

ex = wx.App()
listlist=["my day", "important", "plan", "task"]
lalalala=ToDoList(None,'todolist')
nb = wx.Notebook(lalalala,style=wx.NB_LEFT)
nb.AddPage(MyPanel1(nb),"+Add")  
for strstr in listlist:
    nb.AddPage(MyPanel2(nb),strstr)
lalalala.Centre()
lalalala.Show(True)
ex.MainLoop()