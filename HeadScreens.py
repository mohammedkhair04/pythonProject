from tkinter import *

class clsHeadFrame(Frame):
    def __init__(self,container,xy,wh,bg,contentTitle):
        super().__init__(container,background=bg)

        self.config(highlightbackground='#176B87', highlightthickness=5,width=wh[0],height=wh[1])
        self.place(x=xy[0],y=xy[1])

        self.label = Label(self, text=contentTitle,fg='#176B87',bg='#B4D4FF',font=('helvetica',12,'bold'))
        self.label.place(relx=.5, rely=.5,anchor= CENTER)

        self.btnLogout = Button(self,text='Logout',bg='#86B6F6', fg='#176B87',font=('helvetica', 8, 'bold'))

    def Title(self,title):
        self.label.config(text=title)



