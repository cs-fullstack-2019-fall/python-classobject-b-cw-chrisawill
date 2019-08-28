# Problem 1:
def problem1():
    class Dog:
        def __init__(self, name, breed, color, gender):
            self.name = name
            self.breed = breed
            self.color = color
            self.gender = gender
        def pupper(self):
            print(f"The dog {self.name} is a {self.breed}, who has a {self.color} coat and is {self.gender} years old.")
    adoption = Dog("Rose", "Pitbull", "white and brown", "4")
    # print(adoption.pupper) # !! : no need to print the function, you are no returning anything
    adoption.pupper() # !! : this is the correct syntax to call a method on an instnace of your class

# Problem 2:
def problem2():
    quit2 = input("Enter '='' to quit :  ")
    while quit2 != "=":
        quit2 = input("Try again : ")

# Problem 3:
# Create a class Product that represents a product sold online. A product has a name, price, and quantity.
# The class should have several functions:
# a) One function that can change the name of the product.
# b) Another function that can change the name and price of the product.
# c) A last function that can change the name, price, and quantity of the product.
# Create an object of Product and print all of it's attributes.
def problem3():
    class Product:
        def __init__(self, name, price, quantity):
            self.name = name
            self.price = price
            self.quantity = quantity

        def name_change(self):
            newname = self.name # !! : userInput required

        def selfchange(self):
            newprice = self.price # !! : userInput required
            newquantity = self.quantity # !! : userInput required

    store = Product("Spoon", "$1.00", "100")
    # !! : print all of it's attributes
    print(store.name_change()) # !! : you must return somthing to print the function
    print(store.selfchange()) # !! : you must return somthing to print the function

def main():
    problem1()
    problem2()
    problem3()
main()