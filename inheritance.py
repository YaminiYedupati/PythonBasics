class Item:
    def __init__(self, price):
        self.price = price #price is a common feature for all items

###
# Burger - Child class of Item
###
class Burger(Item):
    def __init__(self):
        _burger_price = 5
        super().__init__(_burger_price) # calling constructor of super class in sub class
        self.unique_feature = "Has Bun and Patty" #something specific to Burger class
        self.burger_tax = 1

    def prepare_burger(): #virtual method
        pass

###
# Beverage - Child class of Item
###
class Beverage(Item):
    def __init__(self, beverage_price, size):
        super().__init__(beverage_price)
        self.size = size
        self.beverage_tax = 2

    def display_beverage_price(self):
        if self.size == 'Medium' :
            self.price = self.price + 0.5 + self.beverage_tax #sccessing "price" of super class
        elif self.size == 'Large' :
            self.price = self.price + 0.7 + self.beverage_tax
        else:
            self.price += self.beverage_tax
        return self.price

###
# VegBurger - child class of Burger
###
class VegBurger(Burger):
    def __init__(self, patty_count):
        super().__init__() #calling constructor of super class 'Burger'
        self.patty_count = patty_count #Can order each burger with different patty size, hence it is considered here

    def display_burger_price_with_tax(self):
        if(self.patty_count > 1):
            self.price += 1
        print("Price of veg burger with patty count",self.patty_count,"is", self.price + self.burger_tax)

    def prepare_burger(self): #overriding super class method with implementation specific to child class.
        print("Preparing veg burger")

class Drink(Beverage):
    def __init__(self, drink_name, size):
        _drink_price = 3
        super().__init__(_drink_price, size)
        self.drink_name = drink_name

    def display_drink_price(self):
        price = super().display_beverage_price() #calling super class method from sub class
        print("Price of", self.drink_name, "is", price)

print()
print('----------------------------Order Veg Burger Details--------------------------------')
paneer_burger = VegBurger(2)
paneer_burger.display_burger_price_with_tax()
paneer_burger.prepare_burger()

print()
print("-----------------------------Order Drink Details---------------------------------    ")
pepsi = Drink('Pepsi', 'Medium')
pepsi.display_drink_price()


####### Output of the above program ##############

# ----------------------------Order Veg Burger Details--------------------------------
# Price of veg burger with patty count 2 is 7
# Preparing veg burger

# -----------------------------Order Drink Details---------------------------------
# Price of Pepsi is 5.5

