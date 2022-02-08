import app
import View
import Database
import User

# grocery store


#present log in menu
  #log in or exit
logInView = View.LogInView()
n = True;


database = Database.UserDatabase()



# loggin in
print("loggin in")

while(True):
    try:
        username = input("enter your username:")
        password = input("enter your password:")
        pendingUser = User.User(username, password)
            
         # check if they exist in database
        if (database.userAlreadyExists(pendingUser)):
            print("logged in successfully")
            break
        else:
            raise RuntimeError("username and password do not exist")
    except:
        continue

    

#end of loggin in
    
print("here we are")

# creating an account



# Adding things to your cart

# checking out

# choosing date of delivery

# printing receipt as a textfile 

#valInp = app.ValidInput()
#username = valInp.get("username")



