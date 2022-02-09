# this takes care of the all of the controller related things for the user
import Store
import User
import StoreView

class StoreController:
    
    def __init__(self,user):
        # the store model 
        store = Store.Store(user)
        view = StoreView.StoreView()

        while(True):
            view.displayStoreItems(store)
            userInput = input("what will you like to add to your cart (or enter -1): ")

            if (self.validInput(userInput)):
                if (userInput == "-1"):
                    break                
                #check if there is enough space in inventory
                if (store.productHasInventory(int(userInput))):
                    #updating the view 
                     print("there is enough inventory")
                     # adding item to the cart
                     user.addProductToCart(store.getProductAtIndex(int(userInput)))
                        
    def validInput(self,ipt):
        if (len(ipt) > 2):
                print("size is incorrect")
                return False
        #making sure it is a number
        try:
            index = int(ipt)
            return True
        except ValueError:
                print("not a number")
                return False
