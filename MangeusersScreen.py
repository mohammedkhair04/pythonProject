# This code was written by Ahmed Abu-Awwad 202210704

from tkinter import *
import HeadScreens
import MainScreen
import clsUserCode
import LoginScreen as login
from tkinter import messagebox
from tkinter import ttk


class Window(Tk):
    def __init__(self, title, geometry, resizable, bg='#EEF5FF'):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.resizable(resizable, resizable)
        self.config(background=bg)
        self.iconbitmap('logo.ico')

        self.headFrame = HeadScreens.clsHeadFrame(self, xy=[0, 0], wh=[1032, 125], bg='#B4D4FF', contentTitle='Mange users Screen')
        self.listFrame = ListFrame(self, xy=[0, 150], wh=[270, 500], bg='#B4D4FF')
        self.mainFrame = MainFrame(self, xy=[300, 150], wh=[730, 500], bg='#B4D4FF')

        self.listFrame.btnBackMain['command'] = self.GoToMainScreen

        self.headFrame.btnLogout.place(x=940, y=45)
        self.headFrame.btnLogout['command'] = self.Logout

        self.listFrame.btnshow['command'] = self.ShowUsersListPage
        self.listFrame.btnAdd['command'] = self.AddNewUserPage
        self.listFrame.btnDel['command'] = self.DeletaUserPage
        self.listFrame.btnUpdate['command'] = self.UpdateUserPage
        self.listFrame.btnFind['command'] = self.FindUserPage

        self.mainloop()

    def Logout(self):
        self.destroy()
        app = login.LoginScreen(title='Bank information editor', geometry='555x394+500+200', resizable=False)
    def GoToMainScreen(self):
        self.destroy()
        app = MainScreen.Window(title='Bank information editor', geometry='1032x679+200+50', resizable=False)

    def ShowUsersListPage(self):
        self.headFrame.Title('Show Users List Screen')
        self.mainFrame.ShowUsersList('show')
    def AddNewUserPage(self):
        self.headFrame.Title('Add New User Screen')
        self.mainFrame.AddNewUser('add')

    def DeletaUserPage(self):

        self.headFrame.Title('Delete User Screen')
        self.mainFrame.DeletaUser('delete')
    def UpdateUserPage(self):
        self.headFrame.Title('Update User Screen')
        self.mainFrame.UpdateUser('update')

    def FindUserPage(self):
        self.headFrame.Title('Find User Screen')
        self.mainFrame.FindUser('find')


class MainFrame(Frame):
    login = False
    ScreenName = ''

    def __init__(self,container,xy,wh,bg):
        super().__init__(container,background=bg)

        self.config(highlightbackground='#176B87', highlightthickness=5,width=wh[0],height=wh[1])
        self.place(x=xy[0],y=xy[1])

    def delete_all_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

    def getSelectAll(self):
        self.chkShow.select()
        self.chkAdd.select()
        self.chkDelete.select()
        self.chkUpdate.select()
        self.chkFind.select()
        self.chkMange.select()

    def getDeleteBtn(self):
        self.btnDel = Button(self, text='Delete', bg='#B4D4FF', width=10, fg='#176B87',command=self.DeleteUser)
        self.btnDel.place(x=400, y=30)

    def getUpdateBtn(self):
        def getUpdateScreen():
            update = UpdateScreen(self.username.get())
        self.btnUpdate = Button(self, text='Update', bg='#B4D4FF', width=10, fg='#176B87',command=getUpdateScreen)
        self.btnUpdate.place(x=400, y=30)

    def DeleteUserCard(self):
        self.lblFullname.destroy()
        self.lblEmail.destroy()
        self.lblPhone.destroy()
        self.lblPassword.destroy()
        self.lblPassword.destroy()

    def GetUserCard(self):


        self.CurrentUser = clsUserCode.clsUser.Find(self.CurrentUsername)

        self.lblFullname = Label(self,text=f'Fullname: {self.CurrentUser.GetFirstName()} {self.CurrentUser.GetLastName()}',bg='#B4D4FF', fg='#176B87', font=('helvetica', 14, 'bold'))
        self.lblFullname.place(x=25, y=90)

        self.lblEmail = Label(self, text=f'Email       : {self.CurrentUser.GetEmail()}', bg='#B4D4FF', fg='#176B87',font=('helvetica', 14, 'bold'))
        self.lblEmail.place(x=25, y=150)

        self.lblPhone = Label(self, text=f'Phone     : {self.CurrentUser.GetPhone()}', bg='#B4D4FF', fg='#176B87',font=('helvetica', 14, 'bold'))
        self.lblPhone.place(x=25, y=210)

        self.lblPassword = Label(self, text=f'Password: {self.CurrentUser.Getpassword()}', bg='#B4D4FF', fg='#176B87',font=('helvetica', 14, 'bold'))
        self.lblPassword.place(x=25, y=270)

        self.lblPermissions = Label(self, text=f'Permissions: {self.CurrentUser.Getpermission()}', bg='#B4D4FF',fg='#176B87', font=('helvetica', 14, 'bold'))
        self.lblPermissions.place(x=25, y=330)

    def Search(self):
        self.CurrentUsername = self.username.get()

        if self.CurrentUsername == '':
            messagebox.showinfo('Waring','Please enter username')


        else:
            if clsUserCode.clsUser.IsExist(self.CurrentUsername):


                self.GetUserCard()


                if self.ScreenName == 'delete':
                    self.getDeleteBtn()
                elif self.ScreenName == 'update':
                    self.getUpdateBtn()



            else:
                messagebox.showinfo('Waring', 'Please enter a valid username')

    def DeleteUser(self):
        result = messagebox.askquestion('Deleting','Are you sure ?')

        if result == 'yes':
            self.CurrentUser.Delete()
            self.DeleteUserCard()
            self.GetUserCard()

    def GetPermissions(self):
        return (self.chkshowvar.get(),self.chkAddvar.get(),self.chkDeletevar.get(),self.chkUpdatevar.get(),self.chkFindvar.get(),self.chkMangevar.get())

    def CalculatePermission(self):
        permission = 0
        PermissionValue = (1,2,4,8,16,32)
        Permissions = self.GetPermissions()
        if Permissions.count(1) == len(Permissions):
            return -1
        for i in range(len(Permissions)):
            if Permissions[i]:
                permission+=PermissionValue[i]
        return permission

    def AddNew(self):
        permission = self.CalculatePermission()
        NewUser = clsUserCode.clsUser(self.Firstname.get(), self.Lastname.get(), self.Email.get(), self.Phone.get(), self.Username.get(), self.Password.get(), permission=permission)

        NewUser.AddNew()

        try:
            if NewUser.IsExist(self.Username.get()):
                messagebox.showinfo('Message','User added successfully')
        except ValueError:
            messagebox.showerror('Waring', 'You have error in file')


    def ShowUsersList(self,screenname):
        self.ScreenName = screenname
        self.delete_all_widgets()

        table = ttk.Treeview(self,height=23)
        table['columns'] = ['Username', 'Firstname', 'Lastname', 'Email', 'Phone','Password','Permission']

        table.column("#0", width=0, stretch=NO)
        table.column("Username",anchor=CENTER, width=100)
        table.column("Firstname", anchor=CENTER, width=100)
        table.column("Lastname", anchor=CENTER, width=100)
        table.column("Email", anchor=CENTER, width=140)
        table.column("Phone", anchor=CENTER, width=100)
        table.column("Password", anchor=CENTER, width=100)
        table.column("Permission", anchor=CENTER, width=75)

        table.heading("#0", text="", anchor=CENTER)
        table.heading("Username", text="Username", anchor=CENTER)
        table.heading("Firstname", text="Firstname", anchor=CENTER)
        table.heading("Lastname", text="Lastname", anchor=CENTER)
        table.heading("Email", text="Email", anchor=CENTER)
        table.heading("Phone", text="Phone", anchor=CENTER)
        table.heading("Password", text="Password", anchor=CENTER)
        table.heading("Permission", text="Permission", anchor=CENTER)

        table.place(x=1,y=1)

        data = clsUserCode.clsUser.LoadDataOnTuple()

        for lineNumber in range(len(data)):
            line = data[lineNumber]
            table.insert(parent='', index='end', iid=lineNumber, text='',values=(line[4], line[0], line[1], line[2], line[3], line[5], line[6]))

    def AddNewUser(self,screenname):
        self.ScreenName = screenname

        self.delete_all_widgets()

        self.lblusername = Label(self, text='Username:', bg='#B4D4FF', fg='#176B87',font=('helvetica', 14, 'bold'))
        self.lblusername.place(x=25, y=25)
        self.Username = Entry(self, bg='#86B6F6', state='normal')
        self.Username.place(x=130, y=33)

        self.lblFirstname = Label(self, text='Firstname:', bg='#B4D4FF', fg='#176B87',font=('helvetica', 14, 'bold'))
        self.lblFirstname.place(x=25, y=90)
        self.Firstname = Entry(self, bg='#86B6F6', state='normal')
        self.Firstname.place(x=130, y=95)

        self.lblLastname = Label(self, text='Lastname:', bg='#B4D4FF', fg='#176B87',font=('helvetica', 14, 'bold'))
        self.lblLastname.place(x=300, y=90)
        self.Lastname = Entry(self, bg='#86B6F6', state='normal')
        self.Lastname.place(x=405, y=95)

        self.lblEmail = Label(self, text='Email:', bg='#B4D4FF', fg='#176B87', font=('helvetica', 14, 'bold'))
        self.lblEmail.place(x=25, y=150)
        self.Email = Entry(self, bg='#86B6F6', state='normal')
        self.Email.place(x=130, y=155)

        self.lblPhone = Label(self, text='Phone:', bg='#B4D4FF', fg='#176B87', font=('helvetica', 14, 'bold'))
        self.lblPhone.place(x=300, y=150)
        self.Phone = Entry(self, bg='#86B6F6', state='normal')
        self.Phone.place(x=405, y=155)

        self.lblPassword = Label(self, text='Password:', bg='#B4D4FF', fg='#176B87',font=('helvetica', 14, 'bold'))
        self.lblPassword.place(x=25, y=210)
        self.Password = Entry(self, bg='#86B6F6', state='normal')
        self.Password.place(x=130, y=215)

        self.lblPermissions = Label(self, text='Permissions:', bg='#B4D4FF', fg='#176B87',font=('helvetica', 14, 'bold'))
        self.lblPermissions.place(x=25, y=300)

        self.rdiSelectAll = Radiobutton(self, text='Select All', bg='#B4D4FF', fg='#176B87',font=('helvetica', 8, 'bold'), command=self.getSelectAll)
        self.rdiSelectAll.place(x=170, y=305)


        self.chkshowvar = IntVar()
        self.chkShow = Checkbutton(self, text='Show client list', bg='#B4D4FF', fg='#176B87',font=('helvetica', 8, 'bold'), variable=self.chkshowvar)
        self.chkShow.place(x=40, y=350)

        self.chkAddvar = IntVar()
        self.chkAdd = Checkbutton(self, text='Add new client', bg='#B4D4FF', fg='#176B87',font=('helvetica', 8, 'bold'), variable=self.chkAddvar)
        self.chkAdd.place(x=170, y=350)

        self.chkDeletevar = IntVar()
        self.chkDelete = Checkbutton(self, text='Delete client', bg='#B4D4FF', fg='#176B87',font=('helvetica', 8, 'bold'), variable=self.chkDeletevar)
        self.chkDelete.place(x=40, y=390)

        self.chkUpdatevar = IntVar()
        self.chkUpdate = Checkbutton(self, text='Update client', bg='#B4D4FF', fg='#176B87',font=('helvetica', 8, 'bold'), variable=self.chkUpdatevar)
        self.chkUpdate.place(x=170, y=390)

        self.chkFindvar = IntVar()
        self.chkFind = Checkbutton(self, text='Find client', bg='#B4D4FF', fg='#176B87', font=('helvetica', 8, 'bold'),variable=self.chkFindvar)
        self.chkFind.place(x=40, y=430)

        self.chkMangevar = IntVar()
        self.chkMange = Checkbutton(self, text='Mange users', bg='#B4D4FF', fg='#176B87', font=('helvetica', 8, 'bold'),variable=self.chkMangevar)
        self.chkMange.place(x=170, y=430)

        self.BtnAddNew = Button(self, text='Add', bg='#B4D4FF', width=15, height=3, fg='#176B87',font=('helvetica', 8, 'bold'),command=self.AddNew)
        self.BtnAddNew.place(x=570, y=420)
    def DeletaUser(self,screenname):
        self.ScreenName = screenname

        self.FindUser(screenname)

    def UpdateUser(self,screenname):
        self.ScreenName = screenname
        self.FindUser(screenname)


    def FindUser(self,screenname):
        self.ScreenName = screenname

        self.delete_all_widgets()

        self.lblusername = Label(self, text='Username:', bg='#B4D4FF', fg='#176B87', font=('helvetica', 14, 'bold'))
        self.lblusername.place(x=25, y=25)
        self.username = Entry(self, bg='#86B6F6', state='normal')
        self.username.place(x=130, y=33)

        self.btnSearch = Button(self,text='Search',bg='#B4D4FF',width=10,fg='#176B87',command=self.Search)
        self.btnSearch.place(x=270,y=30)


class ListFrame(Frame):
    login = False
    def __init__(self,container,xy,wh,bg):
        super().__init__(container,background=bg)

        self.config(highlightbackground='#176B87', highlightthickness=5,width=wh[0],height=wh[1])
        self.place(x=xy[0],y=xy[1])


        self.btnshow = Button(self, text='Show user list', bg='#B4D4FF', width=32, height=3, fg='#176B87',font=('helvetica', 9, 'bold'))
        self.btnshow.place(x=10, y=20)

        self.btnAdd = Button(self, text='Add new user', bg='#B4D4FF', width=32, height=3, fg='#176B87',font=('helvetica', 9, 'bold'))
        self.btnAdd.place(x=10, y=100)

        self.btnDel = Button(self, text='Delete user', bg='#B4D4FF', width=32, height=3, fg='#176B87',font=('helvetica', 9, 'bold'))
        self.btnDel.place(x=10, y=180)

        self.btnUpdate = Button(self, text='Update user', bg='#B4D4FF', width=32, height=3, fg='#176B87',font=('helvetica', 9, 'bold'))
        self.btnUpdate.place(x=10, y=260)

        self.btnFind = Button(self, text='Find user', bg='#B4D4FF', width=32, height=3, fg='#176B87',font=('helvetica', 9, 'bold'))
        self.btnFind.place(x=10, y=340)

        self.btnBackMain = Button(self, text='Main menu', bg='#B4D4FF', width=32, height=3, fg='#176B87',font=('helvetica', 9, 'bold'))
        self.btnBackMain.place(x=10, y=420)

class UpdateScreen(Tk):
    def __init__(self,Username, geometry='550x450+300+150',resizable=False, bg='#EEF5FF'):
        super().__init__()
        self.title('Update Screen')
        self.geometry(geometry)
        self.resizable(resizable, resizable)
        self.config(background=bg)
        self.iconbitmap('logo.ico')

        self.Username = Username
        self.mainFrame = MainFrame(self, xy=[0, 0], wh=[550, 450], bg='#B4D4FF')
        self.getUpdateForme()

    def Update(self):
        User = clsUserCode.clsUser.Find(self.Username)

        User.Update(self.NewEmail.get(),self.NewPhone.get(),self.NewPassword.get(),self.NewPermissions.get())

        self.destroy()
        try:
            if User.IsExist(self.Username):
                messagebox.showinfo('Message','User updated successfully')
        except ValueError:
            messagebox.showerror('Waring', 'You have error in file')
    def getUpdateForme(self):

        self.lblNewEmail = Label(self, text='New Email:', bg='#B4D4FF', fg='#176B87', font=('helvetica', 14, 'bold'))
        self.lblNewEmail.place(x=25, y=50)
        self.NewEmail = Entry(self, bg='#86B6F6', state='normal')
        self.NewEmail.place(x=140,y=55)

        self.lblNewPhone = Label(self, text='New Phone:', bg='#B4D4FF', fg='#176B87', font=('helvetica', 14, 'bold'))
        self.lblNewPhone.place(x=25, y=110)
        self.NewPhone = Entry(self, bg='#86B6F6', state='normal')
        self.NewPhone.place(x=140, y=115)

        self.lblNewPassword = Label(self, text='New Password:', bg='#B4D4FF', fg='#176B87', font=('helvetica', 14, 'bold'))
        self.lblNewPassword.place(x=25, y=170)
        self.NewPassword = Entry(self, bg='#86B6F6', state='normal')
        self.NewPassword.place(x=180, y=175)

        self.lblNewPermissions = Label(self, text='New Permissions:', bg='#B4D4FF', fg='#176B87',font=('helvetica', 14, 'bold'))
        self.lblNewPermissions.place(x=25, y=230)

        self.NewPermissions = Entry(self, bg='#86B6F6',state='normal')
        self.NewPermissions.place(x=200, y=235)

        '''self.rdiSelectAll = Radiobutton(self, text='Select All', bg='#B4D4FF', fg='#176B87',font=('helvetica', 8, 'bold'), command=self.getSelectAll)
        self.rdiSelectAll.place(x=200, y=235)
        
        self.chkNewshowvar = IntVar()
        self.chkNewShow = Checkbutton(self, text='Show client list', bg='#B4D4FF', fg='#176B87',font=('helvetica', 8, 'bold'), variable=self.chkNewshowvar)
        self.chkNewShow.place(x=40, y=310)

        self.chkNewAddvar = IntVar()
        self.chkNewAdd = Checkbutton(self, text='Add new client', bg='#B4D4FF', fg='#176B87',font=('helvetica', 8, 'bold'), variable=self.chkNewAddvar)
        self.chkNewAdd.place(x=170, y=310)

        self.chkNewDeletevar = IntVar()
        self.chkNewDelete = Checkbutton(self, text='Delete client', bg='#B4D4FF', fg='#176B87',font=('helvetica', 8, 'bold'), variable=self.chkNewDeletevar)
        self.chkNewDelete.place(x=40, y=350)

        self.chkNewUpdatevar = IntVar()
        self.chkNewUpdate = Checkbutton(self, text='Update client', bg='#B4D4FF', fg='#176B87',font=('helvetica', 8, 'bold'), variable=self.chkNewUpdatevar)
        self.chkNewUpdate.place(x=170, y=350)

        self.chkNewFindvar = IntVar()
        self.chkNewFind = Checkbutton(self, text='Find client', bg='#B4D4FF', fg='#176B87', font=('helvetica', 8, 'bold'),variable=self.chkNewFindvar)
        self.chkNewFind.place(x=40, y=390)

        self.chkNewMangevar = IntVar()
        self.chkNewMange = Checkbutton(self, text='Mange users', bg='#B4D4FF', fg='#176B87', font=('helvetica', 8, 'bold'),variable=self.chkNewMangevar)
        self.chkNewMange.place(x=170, y=390)'''


        self.BtnUpdate = Button(self, text='Update', bg='#B4D4FF', width=15, height=3, fg='#176B87',font=('helvetica', 8, 'bold'),command=self.Update)
        self.BtnUpdate.place(x=380, y=330)








