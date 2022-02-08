
#user class contains a password and a username
# also contains a 


class User():
    def __init__(self,username, password):
        self.username = username
        self.password = password

    def isTheSame(self, user):   
        if (self.username == user.username and self.password == user.password):
            return True
        return False

    def getUserName(self):
        return self.username



