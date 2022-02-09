import Product
import User


# handles the inventory aspect 


class Store():
    products = []

    def __init__ (self, user):
        
        apple = Product.Fruit("apple", 12, 2)
        banana = Product.Fruit("banana", 12, 30)
        peach = Product.Fruit("peach", 12, 30)
        tangerine = Product.Fruit("tangerine", 12, 30)
        orange = Product.Fruit("orange", 12, 30)
        iphone = Product.Electronic("iphone",30,20)
        mac = Product.Electronic("iphone",300,20)
        self.products.append(apple)
        self.products.append(banana)
        self.products.append(tangerine)
        self.products.append(orange)
        self.products.append(iphone)
        self.products.append(mac)
        
    def getAmountProducts(self):
        return len(self.products)

    # throw an error if index is out of range
    def getProductAtIndex(self, index):
        self.products[index].decreaseInventory()
        return self.products[index]

    # TODO: might want to throw error if
    # user enteres an index that can go out of boubds
    def productHasInventory(self, index):
        return self.products[index].hasEnoughInventory() and index < self.getAmountProducts()
    
        
user = User.User("angel", "sheep787")


#print(store.getAmountProducts())

