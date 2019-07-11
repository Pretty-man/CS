import sqlite
import wx
import ToDoListData

listname = namelist#string
todoname = nametodo#string

#创建一个新的todolist
bol = CreatList(newlistname)
if bol == "succeed":
	print("Succeed!")
else if bol == "existense":
	print("The list already exists!")
else:
	print("Error!")


#删除表 删除list
bol = DeleteList(listname)
if bol == "succeed":
	print("Succeed!")
else if bol == "inexistence":
	print("The list is inexist!")
else:
	print("Error!")



#返回listname list的所有todo
Listall = ListAll(listname);
print(Listall)


#存储数据
ToDoname=[False,nametodo,time.ctime()]
if SaveData(listname,ToDoname):
	print("Successful stotage!")
else:
	print("Illegal input!")


todoname = name
#返回数据
ToDoname = TakeOutData(listname,todoname)
print(ToDoname)


#改变状态 没做改为已经做
ChangeStateDo(listname,todoname)

#改变状态 已经做改为未做
ChangeStateUndo(listname,todoname)