import Product


class Cart():
    products = []

    def __init__(self):
        self.total = 0
      
    def addProduct(self, product):
        self.total = self.total + product.getPrice()
        self.products.append(product)
    
    def getTotalProductsInCart(self):
        return len(self.products)

    def getProductAtIndex(self, index):
        return self.products[index]
    

# user class contains a password and a username
# also contains a
class User():
    
    def __init__(self,username, password):
        self.username = username
        self.password = password
        self.cart = Cart()

    def getTotal(self):
        return self.cart.total

    def addProductToCart(self,product):
        self.cart.addProduct(product)

    def sizeOfCart(self):
        return self.cart.getTotalProductsInCart()

    def getProduct(self, index):
        return self.cart.getProductAtIndex(index)
        
        

    def isTheSame(self, user):   
        if (self.username == user.username and self.password == user.password):
            return True
        return False

    def getUserName(self):
        return self.username

