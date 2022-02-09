import app
import View
import Database
import User
import LoggingInController


# Grocery store delivery service 

# creating the database
database = Database.UserDatabase()

# loggin in
loggingCont = LoggingInController.LogginInController(database)

currentUser = loggingCont.getCurrentUser()

print(currentUser.getUserName())


# Adding things to your cart
    

# checking out

# choosing date of delivery

# printing receipt as a textfile 

#valInp = app.ValidInput()
#username = valInp.get("username")



