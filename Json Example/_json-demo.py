import json
import os
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

    # load  user from .json file
        self.loadUser() 
    def loadUser(self):
        if os.path.exists("user.json"):
            with open("users.json","w",encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    print(user)
    def register(self, user : User):
        self.users.append(User)
        # self.savetoFile()
        print("Kullanıcı Oluşturuldu.")
    def login(self):
        pass
    def savetoFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        with open("user.json","w") as file:
            json.dump(self.users, file)

repository = UserRepository()

while True:
    print("Menü".center(50,"*"))
    secim = input("1-Register\n 2-Login\n 3- Logout\n 4-İdentity\n 5-Exit\nSeçiminiz: ")
    if secim == "5":
        break
    if secim == "1":
        username = input("Username: ")
        password = input("Password: ")
        email = input("Email: ")

        user = User(username= username, password= password, email= email)
        repository = UserRepository(user)
    elif secim == "2":
        username = input("Username: ")
        password = input("Password: ")
        
        user = User(username=username, password=password)
        repository = UserRepository(user)
        pass
    elif secim == "3":
        #logout
        pass
    elif secim == "4":
        #identity
        pass
    else:
        print("Yanlış Seçim Yaptınız.")