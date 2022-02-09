

class Product():
    def __init__(self,name, price, inventory):
        self.name = name
        self.price = price
        self.inventory = inventory

    #checks if there is enough inventory 
    def hasEnoughInventory(self):
        if self.inventory > 0:
            return True
        return False
        

    def decreaseInventory(self):
        self.inventory = self.inventory - 1


# types of products that can be created
    
class Fruit(Product):

    def info(self):
        
        print("this is a fruit: "+ self.name, "hey")



class Electronic(Product):
    def info(self):
        print("this is an electronic: " + self.name)





