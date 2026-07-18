class User:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
    
    def get_password(self):
        return self.__password
    
    def login(self, password):
        if self.__password == password:
            print("Welcome ",self.username)
        else:
            print("Password do not match")
        
    def changePassword(self,oldPassword,newPassword):
        if oldPassword==self.__password:
            if len(str(newPassword))==8:
                self.__password=newPassword
                print("Password updated")
            else:
                print("Password must be of 8 characters")
        else:
            print("Password does not match")

u=User("Rahul",12349856)
u.login(12349856)
print(u.get_password())
u.changePassword(12349856,98765432)
print(u.get_password())