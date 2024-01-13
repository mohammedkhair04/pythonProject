from tkinter import *
from tkinter import simpledialog


class clsPerson:
    def __init__(self, FirstName, LastName, Email, Phone):
        self._FirstName = FirstName
        self._LastName = LastName
        self._Email = Email
        self._Phone = Phone

    def SetFirstName(self, FirstName):
        self._FirstName = FirstName

    def GetFirstName(self):
        return self._FirstName

    def SetLastName(self, LastName):
        self._LastName = LastName

    def GetLastName(self):
        return self._LastName

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


class client(clsPerson, Tk):
    def __init__(self, accountNumber, FirstName, LastName, Email, Phone, pincode, accountBalance):
        clsPerson.__init__(self, FirstName, LastName, Email, Phone)
        Tk.__init__(self)
        self.pincode = pincode
        self.accountBalance = accountBalance
        self.accountNumber = accountNumber

        self.title("Client Page")
        self.geometry("600x300")

        self.show_button = Button(
            self, text="Show Client", command=self.show_client)
        self.show_button.pack()

        self.add_button = Button(
            self, text="Add New Client", command=self.AddNewClient)
        self.add_button.pack()

        self.delete_button = Button(
            self, text="Delete Client", command=self.DeleteClient)
        self.delete_button.pack()

        self.update_button = Button(
            self, text="Update Client Info", command=self.UpdateClientInfo)
        self.update_button.pack()

        self.find_button = Button(
            self, text="Find Client", command=self.FindClient)
        self.find_button.pack()

    @staticmethod
    def check_access_permission(permission, page_number):
        if permission == -1 or permission == page_number in [1, 2, 4, 8, 16, 32]:
            return True
        else:
            return False

    def show_client(self):
        show_client_window = Toplevel(self)
        show_client_window.title("Client Information")

        user_id_label = Label(show_client_window, text="Enter your Id No:")
        user_id_label.pack()
        user_id_entry = Entry(show_client_window)
        user_id_entry.pack()
        show_button = Button(show_client_window, text="Show",
                             command=lambda: self.display_client_info(user_id_entry.get()))
        show_button.pack()

    def display_client_info(self, user_id):
        file = open("user.txt")
        rfile = file.readlines()
        for line in rfile:
            d = line.split("#//#")
            if int(user_id) == int(d[0]):
                if client.check_access_permission(int(d[-1]), 1):
                    client_info_window = Toplevel(self)
                    client_info_window.title("Client Information")
                    file = open("client.txt", "r")
                    filess = file.readlines()
                    for l in filess:
                        all_data = l.split("#//#")
                        client_info_label = Label(client_info_window, text=f"Account Number: {all_data[0]}\n"
                                                  f"Name: {all_data[3]}\n "
                                                  f"Phone Number: {all_data[5]}\n"
                                                  f"Email: {all_data[4]}\n"
                                                  f"Pincode: {all_data[6]}\n"
                                                  f"Account Balance: {all_data[7]}\n")

                        client_info_label.pack()

                else:
                    error_label = Label(
                        text="You don't have permission to show client information.")
                    error_label.pack()

    def AddNewClient(self):
        file = open("user.txt")
        rfile = file.readlines()
        userid = int(input("enter your Id No: "))
        for line in rfile:
            d = line.split("#//#")
            if userid == int(d[0]):
                if client.check_access_permission(int(d[-1]), 2):
                    self.accountNumber = int(input("Enter accountNumber:"))
                    self._FirstName = str(input("Enter your first Name:"))
                    self._LastName = str(input("Enter your last name:"))
                    self._Email = input("Enter your Email:")
                    self._Phone = int(input("Enter your phone Number:"))
                    self.pincode = int(input("Enter your pincode:"))
                    self.accountBalance = float(
                        input("Enter your AccountBalnce:"))
                    add = (str(self.accountNumber), "#//#", self._FirstName, "#//#", self._LastName, "#//#", str(self.GetFullName()), "#//#",
                           str(self._Email), "#//#", str(self._Phone), "#//#", str(self.pincode), "#//#", str(self.accountBalance), "\n")
                    file = open("client.txt", "a")
                    file.writelines(add)
                    print(f"add account done.")
                    print(f"""your info:
        your accountNumber: {self.accountNumber},
        Name :{self.GetFullName()},
        phone NO :{self._Phone},
        your email :{self._Email},
        pincode:{self.pincode}""")
                else:
                    print("you dont have permission to show client")

    @staticmethod
    def delete_line(file_path, line_number):
        file = open(file_path, 'r')
        lines = file.readlines()
        if 0 <= line_number <= len(lines):
            del lines[line_number]
            file = open(file_path, 'w')
            file.writelines(lines)
            print(f"Line {line_number} deleted successfully.")
        else:
            print("Invalid line number.")

    def DeleteClient(self):
        user_id = simpledialog.askinteger("Delete Client", "Enter your Id No:")
        if user_id is not None:
            user_permission = None

            # Find the user in the user.txt file
            user_file = open("user.txt", "r")
            for line in user_file:
                user_data = line.split("#//#")
                if user_id == int(user_data[0]):
                    user_permission = int(user_data[-1])
                    break
            if client.check_access_permission(user_permission, 4):
                account_number = simpledialog.askinteger(
                    "Delete Client", "Enter accountNumber:")
                if account_number is not None:
                    with open("client.txt", "r") as client_file:
                        data = client_file.readlines()
                        for line in data:
                            client_data = line.split("#//#")
                            if account_number == int(client_data[0]):
                                confirmation = simpledialog.askstring(
                                    "Delete Client",
                                    f"Are you sure you want to delete account {account_number}? (yes/no)")
                                if confirmation and confirmation.lower() == 'yes':
                                    self.delete_line(
                                        "client.txt", data.index(line))
                                    print(
                                        f"Account {account_number} deleted successfully.")
                                else:
                                    print(
                                        f"Account {account_number} is not deleted.")
                                break
                        else:
                            print(f"Account {account_number} not found.")
            else:
                print("You don't have permission to delete a client.")

    def updateInfo(file_path, line_index, separator, index_to_update_1, index_to_update_2, new_content_1,
                   new_content_2):

        file = open(file_path, 'r')
        lines = file.readlines()
        if 0 <= line_index < len(lines):
            line = lines[line_index]
            # Split the line based on the specified separator
            parts = line.split(separator)
            if len(parts) == 8:
                if 0 <= index_to_update_1 < len(parts) and 0 <= index_to_update_2 < len(parts):
                    # Update the desired indices within the parts
                    parts[index_to_update_1] = str(new_content_1)
                    parts[index_to_update_2] = str(new_content_2)
                    # Join the updated parts to form the new line
                    updated_line = separator.join(parts)
                    lines[line_index] = updated_line
                    with open(file_path, 'w') as file:
                        file.writelines(lines)
                    print(
                        f"Contents at line {line_index} updated successfully.")
                else:
                    print(
                        f"One or both indices are out of range for line {line_index}.")
            else:
                print(f"The line does not have 8 parts.")
        else:
            print(f"Line index {line_index} is out of range.")

    def UpdateClientInfo(self):
        user_id = simpledialog.askinteger(
            "Update Client Info", "Enter your Id No:")
        if user_id is not None:
            user_permission = None

            # Find the user in the user.txt file
            with open("user.txt", "r") as user_file:
                for line in user_file:
                    user_data = line.split("#//#")
                    if user_id == int(user_data[0]):
                        user_permission = int(user_data[-1])
                        break

            if client.check_access_permission(user_permission, 8):
                account_number = simpledialog.askinteger(
                    "Update Client Info", "Enter accountNumber:")
                if account_number is not None:
                    with open("client.txt", "r") as client_file:
                        data = client_file.readlines()
                        for line in data:
                            client_data = line.split("#//#")
                            if account_number == int(client_data[0]):
                                confirmation = simpledialog.askstring(
                                    "Update Client Info",
                                    f"Are you sure you want to update account {account_number}? (yes/no)")
                                if confirmation and confirmation.lower() == 'yes':
                                    self._Email = simpledialog.askstring(
                                        "Update Client Info", "Enter new email:")
                                    self._Phone = simpledialog.askinteger(
                                        "Update Client Info", "Enter new number:")
                                    client.updateInfo(
                                        "client.txt", data.index(line), "#//#", 4, 5, self._Email, self._Phone)
                                    print(
                                        f"Account {account_number} updated successfully.")
                                else:
                                    print(
                                        f"Account {account_number} is not updated.")
                                break
                        else:
                            print(f"Account {account_number} not found.")
            else:
                print("You don't have permission to update client info.")

    def FindClient(self):
        user_id = simpledialog.askinteger("Find Client", "Enter your Id No:")
        if user_id is not None:
            user_permission = None

            # Find the user in the user.txt file
            user_file = open("user.txt", "r")
            for line in user_file:
                user_data = line.split("#//#")
                if user_id == int(user_data[0]):
                    user_permission = int(user_data[-1])
                    break

            if client.check_access_permission(user_permission, 16):
                account_number = simpledialog.askinteger(
                    "Find Client", "Enter accountNumber:")
                if account_number is not None:
                    with open("client.txt", "r") as client_file:
                        data = client_file.readlines()
                        for line in data:
                            client_data = line.split("#//#")
                            if account_number == int(client_data[0]):
                                print(f"Account Number: {client_data[0]}\n"
                                      f"Name: {client_data[3]}\n "
                                      f"Phone Number: {client_data[5]}\n"
                                      f"Email: {client_data[4]}\n"
                                      f"Pincode: {client_data[6]}\n"
                                      f"Account Balance: {client_data[7]}")
                                break
                        else:
                            print(f"Account {account_number} not found.")
            else:
                print("You don't have permission to find a client.")


client1 = client("546345", "Ahmed", "ali",
                 "sadhfa@gmail.com", "894", "780", "788")
client1.mainloop()
