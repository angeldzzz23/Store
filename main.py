import app
import View
import Database
import User
import LoggingInController
import StoreController
import Checkout


# fake valid credit card: 79927398713


# Grocery store delivery service 

# creating the database
database = Database.UserDatabase()

# loggin in
loggingCont = LoggingInController.LogginInController(database)

currentUser = loggingCont.getCurrentUser()



# Adding things to your cart

storecontrol = StoreController.StoreController(currentUser)

print(currentUser.sizeOfCart




# checking out
checkController  = Checkout.CheckoutController(currentUser)
 





