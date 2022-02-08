
import User

class UserDatabase():
    totalUsers = []
    
    def __init__(self):
        user = User.User("angelzzz23", "password")
        user2 = User.User("angel23", "password")
        self.totalUsers.append(user)
        self.totalUsers.append(user2)
        

    def addUser(User):
        print("jerje")
    

    def getUsersAtIndex(self,index):
        return self.totalUsers[index]

    def getTotalusers(self):
        return len(self.totalUsers)

    # this checks if the user exists in the database
    def userAlreadyExists(self,pendingUser):
        
        for user in self.totalUsers:
            if (user.isTheSame(pendingUser)):
                return True
        return False





