import wx


class ToDoList(wx.Frame):

    def __init__(self,parent, title):
        super(ToDoList, self).__init__(parent, title=title, size=(750,522))     
        self.SetTransparent(230)
        self.SetMaxSize((740,513))  
        #设置窗口最大尺寸
        self.SetMinSize((740,513))  
        #设置窗口最小尺寸

class MyPanel1(wx.Panel):

    def __init__(self, parent):    
        super(MyPanel1, self).__init__(parent)
        self.SetBackgroundColour("#C5E7F1")
        # text = wx.TextCtrl(self, style = wx.TE_MULTILINE, size = (250,150))
        self.button_add = wx.Button(self, -1, label="添加事项", \
                                    pos=(10, 400), size=(170, 50)) 
        font = wx.Font(15, wx.SCRIPT, wx.NORMAL, wx.BOLD,underline=False)         
        self.button_add.SetFont(font)  
        self.button_add.SetDefault()
        self.button_add.SetForegroundColour("#A09F69")         
        #设置按钮字体颜色        
        self.Bind(wx.EVT_BUTTON, self.on_creat, self.button_add)        
        self.button_add.SetBackgroundColour("#FEFEFE")       
        #设置按钮背景颜色
        """
        以下为添加图片
        """
        try:
        	
        	image_file = '1.jpg'            	
        	to_bmp_image = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()            
        	self.bitmap = wx.StaticBitmap(self, -1, to_bmp_image, (0, 0))             	
        	image_width = to_bmp_image.GetWidth()            
        	image_height = to_bmp_image.GetHeight()            
        	set_title = '%s %d x %d' % (image_file, to_bmp_image.GetWidth(), to_bmp_image.GetHeight())
        except IOError:
            print ('Image file %s not found' % image_file)
            raise Syste11

    def on_creat(self, event):
        # mylister=str_list("添加字符串")
        enter = wx.TextEntryDialog(self, '添加分类')
        if enter.ShowModal() == wx.ID_OK:
            return_value = enter.GetValue()
            listlist.append(return_value) 
            nb.AddPage(MyPanel2(nb), return_value)          
            return return_value


class MyPanel2(wx.Panel):
    
    def __init__(self, parent):
        super(MyPanel2, self).__init__(parent,wx.BG_STYLE_CUSTOM)

        liststr_rdown = [None for i in range(0)]
        number_rdowm = 0        
        self.radio_list = [None for i in range(len(liststr_rdown))]
        for str_rdown in liststr_rdown:
            self.radio_list[number_rdowm] = wx.CheckBox(self.panel, \
                                                        -1, pos=(171, 100), label=str_rdown)
            number_rdowm += 1
        self.button_add_rdowm = wx.Button(self, -1, label="添加" \
                                          , pos=(450, 400), size=(170, 50))
        font = wx.Font(15, wx.MODERN, wx.NORMAL, wx.BOLD)        
        #设置添加按钮的字体样式

        self.button_add_rdowm.SetFont(font) 
        self.button_add_rdowm.SetForegroundColour("#4AB2FA")
        #设置添加按钮上的字体颜色
        
        self.Bind(wx.EVT_BUTTON, self.on_creat_rdown, self.button_add_rdowm)
        self.button_del = wx.Button(self, -1, label="删除" \
                                    , pos=(450, 350), size=(170, 50))
        

        # self.Bind(wx.EVT_BUTTON, self.on_delrdown, self.button_del)
        font = wx.Font(15, wx.MODERN, wx.NORMAL,wx.BOLD) 
        #设置删除按钮的字体样式 
        self.button_del.SetFont(font)
        self.button_del.SetForegroundColour("#4AB2FA") 
        #设置按钮上的字体颜色
        self.button_add_rdowm.SetBackgroundColour("#FEFEFE")
        #添加按钮的背景
        self.button_del.SetBackgroundColour("#FEFEFE")
        #删除按钮的背景
        self.SetBackgroundColour("#FEFEFE")
        #设置页面背景颜色

    def on_creat_rdown(self, event):
        enter = wx.TextEntryDialog(self, '添加事项')
        if enter.ShowModal() == wx.ID_OK:
            return_value_rdown = enter.GetValue()
            self.radio_list.append(wx.CheckBox(self,-1, pos=(191, 100 + len(self.radio_list) * 40),\
            label=return_value_rdown))
            return return_value_rdown
    # def on_delrdown():
    	
app = wx.App()
set_size=wx.Size(10,10)
listlist = ["我的一天", "重要的事", "计划", "任务"]
lalalala = ToDoList(None, '简易备忘录')
nb = wx.Notebook(lalalala, style=wx.NB_LEFT)
nb.SetPadding(set_size)
nb.AddPage(MyPanel1(nb), "+新的事件")
for strstr in listlist:    
    nb.AddPage(MyPanel2(nb), strstr)
lalalala.Centre()
lalalala.Show(True)
app.MainLoop()