import sqlite3
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
def AllListName(): #显示所有标签（表）的名字
    try:
        conn=sqlite3.connect('test.db')
        c=conn.cursor()
        c.execute("select name from sqlite_master where type='table' order by name")
        print(c.fetchall())
    except sqlite3.Error as e:
        print(e)
    conn.commit()
    conn.close()
def Creatlist(newlistname):#创建新的标签（表）
    for c in newlistname:
        if c==' ':
            return false
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('select table from test')
    res=c.fetchall()
    for line in res: #判断要创建的标签是否已经存在（标签名字是否重复）
        if line==newlistname:
            conn.close()
            return False
    c.execute('''create table if not exists {} 
           (State INT PRIMARY KEY     NOT NULL,
           nametodo           TEXT    NOT NULL,
           time               TEXT    NOT NULL,);'''.format(newlistname))
    conn.commit()
    conn.close()
    return True #新标签创建成功则返回True
def DeleteList(listname): #删除标签
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('select table from test')
    res = c.fetchall()
    f=0
    for line in res: #判断要删除的标签名是否存在
        if line == listname:
            f=1
    if f==0:
        conn.close()
        return False #不存在则返回False
    c.execute("drop table {}".format(listname)) #存在则执行删除语句并返回True 
    #c.execute("DELETE from ToDoList where ID=2;")
    conn.commit()
    conn.close()
    return True
def ListAll(listname): #查看某个标签中事件的状态（完成or未完成）、事件的名字
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    cursor = c.execute("SELECT State, nametodo, time  from {}".format(listname))
    conn.commit()
    conn.close()
    return cursor
def SaveData(listname,ToDoname): #将用户输入的事件的状态、事件的名字保存到数据库中
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    sql='''insert into {} (State, nametodo, time) values (?,?,?)'''.format(listname)
    para = (ToDoname[0],ToDoname[1],ToDoname[2])
    c.execute(sql,para)
    #c.execute('insert into listname values(%s)'%ToDoname)
    conn.commit()
    conn.close()
def TakeOutData(listname,todoname): #根据用户输入的事件名字查看事件的状态
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    cursor=c.execute("select State, nametodo, time  from {} where nametodo={}".format(listname,todoname))
    conn.commit()
    conn.close()
    return cursor
def ChangeStateDo(listname,todoname): #根据用户输入的事情名字，把事情的状态变为已完成
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("UPDATE {} set State = 1 where nametodo={}".format(listname,todoname))
    conn.commit()
    conn.close()
def ChangeStateUndo(listname,todoname): #根据用户输入的事情名字，把事情的状态变为未完成
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("UPDATE {} set State = 0 where nametodo={}".format(listname,todoname))
    conn.commit()
    conn.close()
bol=Creatlist(newlistname)
bol=DeleteList(listname)
Listall=ListAll(listname)
SaveData(listname,ToDoname)
ToDoname=TakeOutData(listname,todoname)
ChangeStateDo(listname,todoname)
ChangeStateUndo(listname,todoname)
AllListName()
