import View
import Database
import User


class LogginInController():
            
        def __init__(self, database):
            # ask the user to choose what they want to do
            print("ask here")        
             # call logging in method as default
            self.logginIn()
        def getCurrentUser(self):
            return self.user


        def logginIn(self):
            logInView = View.LogInView()
            while(True):
                try:
                    username = input("enter your username:")
                    password = input("enter your password:")
                    pendingUser = User.User(username, password)
            
                     # check if they exist in database
                    if (database.userAlreadyExists(pendingUser)):
                        print("logged in successfully")
                        self.user = pendingUser
                        break
                    else:
                        raise RuntimeError("username and password do not exist")
                except:
                    continue
            
database = Database.UserDatabase()

logController = LogginInController(database)


