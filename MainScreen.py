from tkinter import *
import HeadScreens
import MangeusersScreen
import LoginScreen as login




class Window(Tk):
    def __init__(self, title, geometry, resizable, bg='#EEF5FF'):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.resizable(resizable, resizable)
        self.config(background=bg)
        self.iconbitmap('logo.ico')


        self.headFrame = HeadScreens.clsHeadFrame(self, xy=[0, 0], wh=[1032, 125], bg='#B4D4FF', contentTitle='Main Screen')
        self.listFrame = ListFrame(self, xy=[0, 150], wh=[270, 500], bg='#B4D4FF')
        self.mainFrame = MainFrame(self, xy=[300, 150], wh=[730, 500], bg='#B4D4FF')





        self.listFrame.MangeBtn['command'] = self.GoToMangeusersScreen

        self.headFrame.btnLogout.place(x=940, y=45)
        self.headFrame.btnLogout['command'] = self.Logout

        self.mainloop()

    def Logout(self):
        self.destroy()
        app = login.LoginScreen(title='Bank information editor',geometry='555x394+500+200',resizable=False)


    def GoToMangeusersScreen(self):
        self.destroy()
        app = MangeusersScreen.Window(title='Bank information editor', geometry='1032x679+200+50', resizable=False)

class MainFrame(Frame):
    login = False
    def __init__(self,container,xy,wh,bg):
        super().__init__(container,background=bg)

        self.config(highlightbackground='#176B87', highlightthickness=5,width=wh[0],height=wh[1])
        self.place(x=xy[0],y=xy[1])

class ListFrame(Frame):
    login = False
    def __init__(self,container,xy,wh,bg):
        super().__init__(container,background=bg)

        self.config(highlightbackground='#176B87', highlightthickness=5,width=wh[0],height=wh[1])
        self.place(x=xy[0],y=xy[1])

        self.showBtn = Button(self, text='Show client list', bg='#B4D4FF', width=32, height=3, fg='#176B87',font=('helvetica', 8, 'bold'))
        self.showBtn.place(x=10, y=20)
        self.showBtn.config(highlightbackground='#176B87', highlightthickness=2)

        self.AddBtn = Button(self, text='Add new client', bg='#B4D4FF', width=32, height=3, fg='#176B87',font=('helvetica', 8, 'bold'))
        self.AddBtn.place(x=10, y=100)

        self.DelBtn = Button(self, text='Delete client', bg='#B4D4FF', width=32, height=3, fg='#176B87',font=('helvetica', 8, 'bold'))
        self.DelBtn.place(x=10, y=180)

        self.UpdateBtn = Button(self, text='Update client', bg='#B4D4FF', width=32, height=3, fg='#176B87',font=('helvetica', 8, 'bold'))
        self.UpdateBtn.place(x=10, y=260)

        self.FindBtn = Button(self, text='Find client', bg='#B4D4FF', width=32, height=3, fg='#176B87',font=('helvetica', 8, 'bold'))
        self.FindBtn.place(x=10, y=340)

        self.MangeBtn = Button(self, text='Mange users', bg='#B4D4FF', width=32, height=3, fg='#176B87',font=('helvetica', 8, 'bold'))
        self.MangeBtn.place(x=10, y=420)







