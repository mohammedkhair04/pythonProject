# This code was written by Ahmed Abu-Awwad 202210704

import clsPersonCode
from tkinter import messagebox

class clsUser(clsPersonCode.clsPerson):

    Filepath = 'Users.txt'
    def __init__(self,FirstName,LastName,Email,Phone,username,password,permission):
        super().__init__(FirstName, LastName, Email, Phone)
        self._username = username
        self._password = password
        self._permission = permission

    
    def Setusername(self,username):
        self._username = username
        
    def Getusername(self):
        return self._username
    
    def Setpassword(self,password):
        self._password = password
    
    def Getpassword(self):
        return self._password
    
    def Setpermission(self,permission):
        self._permission = permission

    def Getpermission(self):
        return self._permission


    def Print(self):
        print('Info: \n')
        print('\n---------------------')
        print(f'\nUserName: {self._username}')
        print(f'\nFirstName: {self._FirstName}')
        print(f'\nLastName: {self._LastName}')
        print(f'\nFullName: {self.GetFullName()}')
        print(f'\nEmail: {self._Email}')
        print(f'\nPhone: {self._Phone}')
        print(f'\nPassword: {self._password}')
        print(f'\npermission: {self._permission}')
        print('\n---------------------\n')

    @staticmethod
    def LoadDataOnTuple():
        try:
            allData = []
            file = open(clsUser.Filepath, 'r')
            Data = file.readlines()
            for line in Data:
                line = line.split('#//#')
                allData.append( (line[0], line[1], line[2], line[3], line[4], line[5], int(line[6]) ) )
            file.close()
            return tuple(allData)
        except:
            messagebox.showerror('Error','You have error in file')

    @staticmethod
    def LoadDataOnObjects():
        try:
            allData = []
            file = open(clsUser.Filepath, 'r')
            Data = file.readlines()
            for line in Data:
                line = line.split('#//#')
                allData.append(clsUser(line[0], line[1], line[2], line[3], line[4], line[5], int(line[6])))
            file.close()
            return allData
        except:
            messagebox.showerror('Error','You have error in file')

    def ConvertObjectToLine(self,obj,Delim='#//#'):
        return obj.GetFirstName()+Delim+obj.GetLastName()+Delim+obj.GetEmail()+Delim+obj.GetPhone()+Delim+obj.Getusername()+Delim+obj.Getpassword()+Delim+str(obj.Getpermission())
    def AddNew(self):
        file = open(clsUser.Filepath,'a')
        line = self.ConvertObjectToLine(self)+'\n'
        file.write(line)
        file.close()

    def Update(self,Email,Phone,password,permissions):
        alldata = self.LoadDataOnObjects()
        file = open(clsUser.Filepath,'w')
        file.close()
        file = open(clsUser.Filepath, 'a')
        for obj in alldata:
            if self.Getusername() == obj.Getusername():
                obj.SetEmail(Email)
                obj.SetPhone(Phone)
                obj.Setpassword(password)
                obj.Setpermission(permissions)

            file.write(self.ConvertObjectToLine(obj)+'\n')
        file.close()

    def Delete(self):
        alldata = self.LoadDataOnObjects()
        file = open(clsUser.Filepath, 'w')
        file.close()
        file = open(clsUser.Filepath, 'a')
        for obj in alldata:
            if self.Getusername() != obj.Getusername():
                file.write(self.ConvertObjectToLine(obj) + '\n')
        file.close()
    @staticmethod
    def IsExist(username):
        return ''!=clsUser.Find(username).Getusername()

    @staticmethod
    def Find(Username):
        alldata = clsUser.LoadDataOnObjects()
        for obj in alldata:
            if Username == obj.Getusername():
                return obj

        return clsUser('','','','','','',0)

    @staticmethod
    def Find2(Username,Password):
        alldata = clsUser.LoadDataOnObjects()
        for obj in alldata:
            if Username == obj.Getusername() and Password == obj.Getpassword():
                return obj

        return clsUser('', '', '', '', '', '', 0)



