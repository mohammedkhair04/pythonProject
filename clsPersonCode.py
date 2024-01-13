# This code was written by Ahmed Abu-Awwad 202210704

class clsPerson:
    def __init__(self,FirstName,LastName,Email,Phone):
        self._FirstName = FirstName
        self._LastName = LastName
        self._Email = Email
        self._Phone = Phone
    
    
    def SetFirstName(self,FirstName):
        self._FirstName = FirstName
        
    def GetFirstName(self):
        return self._FirstName
    
    def SetLastName(self,LastName):
        self._LastName = LastName
    def GetLastName(self):
        return self._LastName

    def SetEmail(self,Email):
        self._Email = Email
    def GetEmail(self):
        return self._Email

    def SetPhone(self,Phone):
        self._Phone = Phone
    def GetPhone(self):
        return self._Phone
    
    def GetFullName(self):
        return self._FirstName + ' ' + self._LastName
    
    def Print(self):
        print('Info: \n')
        print('\n---------------------')
        print(f'\nFirstName: {self._FirstName}')
        print(f'\nLastName: {self._LastName}')
        print(f'\nFullName: {self.GetFullName()}')
        print(f'\nEmail: {self._Email}')
        print(f'\nPhone: {self._Phone}')
        print('\n---------------------\n')

