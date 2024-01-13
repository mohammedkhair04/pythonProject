# This code was written by Ahmed Abu-Awwad 202210704

from tkinter import *
from tkinter import messagebox
import HeadScreens
import MainScreen
import clsUserCode


class LoginScreen(Tk):
    def __init__(self, title, geometry, resizable, bg='#EEF5FF'):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.resizable(resizable, resizable)
        self.config(background=bg)
        self.iconbitmap('logo.ico')

        self.headFrame = HeadScreens.clsHeadFrame(self, xy=[0, 0], wh=[555, 100], bg='#B4D4FF', contentTitle='Login Screen')
        self.mainFrame = MainFrame(self, xy=[0, 110], wh=[555, 284], bg='#B4D4FF')

        self.mainFrame.btnLogin['command'] = self.Login

        self.mainloop()

    AttemptCounter = 0
    IsLocked = False
    def Login(self):
        Username = self.mainFrame.Username.get()
        Password = self.mainFrame.Password.get()
        user = clsUserCode.clsUser.Find2(Username, Password)
        if Username=='' and Password=='':
            messagebox.showinfo('waring','The blanks must be filled in')

        elif Username == user.Getusername() and Password == user.Getpassword() and not self.IsLocked:
            self.destroy()
            app = MainScreen.Window(title='Bank information editor', geometry='1032x679+200+50', resizable=False)

        else:
            self.AttemptCounter+=1
            if self.AttemptCounter >= 3:
                self.IsLocked = True
                messagebox.showinfo('', f'Your account locked ')
            else:
                messagebox.showinfo(f'waring', f'username or password error later {3-self.AttemptCounter}times')


class MainFrame(Frame):
    login = False
    def __init__(self,container,xy,wh,bg):
        super().__init__(container,background=bg)

        self.config(highlightbackground='#176B87', highlightthickness=5,width=wh[0],height=wh[1])
        self.place(x=xy[0],y=xy[1])

        self.Usernamelabel = Label(self, text='Username:', bg=bg, fg='#176B87', font=('helvetica', 8, 'bold'))
        self.Usernamelabel.place(x=180, y=70)

        self.Username = Entry(self, bg='#86B6F6', state='normal')
        self.Username.config(highlightbackground='#86B6F6', highlightthickness=2)
        self.Username.place(x=250, y=70)

        self.Passwordlabel = Label(self, text='Password:', bg=bg, fg='#176B87', font=('helvetica', 8, 'bold'))
        self.Passwordlabel.place(x=180, y=120)

        self.Password = Entry(self, bg='#86B6F6', show='*')
        self.Password.config(highlightbackground='#86B6F6', highlightthickness=2)
        self.Password.place(x=250, y=120)

        self.btnLogin = Button(self, text='Login', bg='#86B6F6', width=26, fg='#176B87',font=('helvetica', 8, 'bold'))
        self.btnLogin.place(x=180, y=170)
        self.btnLogin.config(highlightbackground='#86B6F6', highlightthickness=2)




