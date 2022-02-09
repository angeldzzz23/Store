
# this contains all of the methods that will be used to display the view

class StoreView:

    def __init__(self):
        print("")

    def displayStoreItems(self,store):
        size = store.getAmountProducts()
        for i in range(size):
            print( i,  " "+ store.getPrduct(i).name)

        
    
        

    
