import View
import Database
import User


class LogginInController():
        
        
        def __init__(self, database):
            logInView = View.LogInView()
            

            while (True):
               
                logInView.cleanConsole()
                logInView.displayLogInMenu()
                decision = input("what will you like to do: ")
                
            
                if decision == "1":
                    self.logginIn(database)
                    break
                elif decision == "2":
                    self.createAccount(database)
                    database.addUser(self.user)
                    break
                
            # ask the user to choose what they want to do
                 
             # call logging in method as default
            

        #end of initializer

            
        def getCurrentUser(self):
            return self.user

        #creates a new account: 
        def createAccount(self, database):
            print("creating an account")
            logInView = View.LogInView()
            while(True):
                try:
                    username = input("enter your username:")
                    password = input("enter your password:")
                    pendingUser = User.User(username, password)
            
                     # check if they exist in database
                    if (database.userAlreadyExists(pendingUser) == False):
                        print("acc in successfully")
                        self.user = pendingUser
                        break
                    else:
                        raise RuntimeError("username and password do not exist")
                except:
                    continue
    
        
        def logginIn(self,database):
            logInView = View.LogInView()
            print("signing in ")
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


