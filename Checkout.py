import Product
import User
import datetime
from datetime import datetime




# the checkout controller

class CheckoutController():

    def __init__(self, user):
        # get location from user
        self.authorizeLocation()
        print("\n")
        # ask them to fill their credit card info

        card = input("enter your card number: ")
        print(self.checkLuhn(card))


        
        # ask them for the date of reservation
        print("making the reservation (up to a year in advc)")
        date = self.getValidDate() 



        file1 = open("receipt.txt","w")
        file1.write("your " +  date + " receipt" + "\n")
        
        
        # print receipt
        #  print("your", date, "receipt")
        user.getTotal()
    
        for i in range(user.sizeOfCart()):
            print(user.getProduct(i).name, str(user.getProduct(i).price))
            file1.write(user.getProduct(i).name + " " + str(user.getProduct(i).price) + "\n")

        file1.write("total: " + str(user.getTotal()) + "\n") 
        

        file1.close()
        
            
    def getValidCardInfo(self):
        while(True):
            card = input("enter your card number: ")
            if (self.checkLuhn(card)):
                this.cardInf = card

                
    def authorizeLocation(self):
        while (True):
            print("authorizing location\n")
            inp = input("press n to share location: ")
            if (inp == "n" or inp == inp == "N"):
                print("location authorized")
                break

        
    # the lughn algorithm
    # just to check that the credit card info is correct
    # https://www.geeksforgeeks.org/luhn-algorithm/ . 
    # written one in c++ but this one seems more efficient. 
    def checkLuhn(self,cardNo):
     
        nDigits = len(cardNo)
        nSum = 0
        isSecond = False
         
        for i in range(nDigits - 1, -1, -1):
            d = ord(cardNo[i]) - ord('0')
         
            if (isSecond == True):
                d = d * 2
      
            # We add two digits to handle
            # cases that make two digits after
            # doubling
            nSum += d // 10
            nSum += d % 10
      
            isSecond = not isSecond
         
        if (nSum % 10 == 0):
            return True
        else:
            return False        


    def getValidDate(self):
        
        output = ""


        while(True):
            
            inputDate = input("Enter the date in format 'dd/mm/yy' : ")
            try:
                day, month, year = inputDate.split('/')
                isValidDate = True
            except:
                continue


            # this should solve of out input validation
            
            try:
                datetime.now().year
                if (int(datetime.now().year) == int(year) and int(datetime.now().month) == int(month)   ):
                    if datetime.now().day > int(day):
                        print("enter a valid date, please")
                        continue

                # has to be the same year
                if (int(datetime.now().year) != int(year)):
                    print("enter a valid date, please!")
                    continue

                # here i could also check the availabilities if I want,
                    
                
            except ValueError:
                isValidDate = False
            
            if(isValidDate):
                print("Input date is valid ..")
                
                output = month + "/" + day + "/" + year

                return output

                break
            else:
                print("Input date is not valid..")
                continue
    # end of valid ate         
                
        



product = Product.Fruit("apple",30,20)
product2 = Product.Fruit("pear",30,20)

user = User.User("anel", "pass")


user.addProductToCart(product)
user.addProductToCart(product2)
#print(user.getTotal())

check = CheckoutController(user)

#date_entry = input('Enter a date (i.e. 2017,7,1)')
#year, month, day = map(int, date_entry.split(','))
#date = datetime(year, month, day)

#print(datetime.now().day)
#print(datetime.now().month >  1)
#
#date = datetime.datetime(2008, 12, 22)
#print(datetime.now() > date)


