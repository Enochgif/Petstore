class Pet_store:
    def __init__(self,Store_name, Store_motto, Store_location, Contact_us):
        self.Store_name = Store_name
        self.Store_motto = Store_motto
        self.Store_location = Store_location
        self.Contact_us  = Contact_us

    # def store_details(self):
    #     done = input("Enter Store name:") 
    #     return f"=========WELCOME TO {done} store ========="

    def store_details(self): 
        print(f"=========WELCOME TO Las Vegas Petstore =========")
        print(f"WE LASVEGAS PETSTORE offer you quality pets with experience.Thanks for transacting with")
        print(f"We are located at 1965 Brooklyn Street, Las Vegas, USA")
        print(f"You can contact us on our mobile and Social media platforms") 
        

    # # def store_details2(self):
    # #     ter = input("Enter store motto")
         
    # #     return f"Our motto is {ter}"
    
    # def store_details2(self):
    #     print(f"WE LASVEGAS PETSTORE offer you quality pets with experience.Thanks for transacting with")
    
    # # def store_details3(self):
    # #     yet = input("Enter store location: ")
    # #     return f"Our location is at {yet}"

    # def store_details3(self):
    #     print(f"We are located at 1965 Brooklyn Street, Las Vegas, USA")

    # # def store_details4(self):
    # #     det = input("Enter store contact:")
    # #     return f"Contact us on {det} toll" 

    # def store_details4(self):
    #     print(f"You can contact us on our mobile and Social media platforms") 
        
dei = Pet_store(1,2,3,4)
print(dei.store_details())
# print(Pet_store.store_details(3))
# print(Pet_store.store_details2(3))
# print(Pet_store.store_details3(5))
# print(Pet_store.store_details4(3))




class pets(Pet_store):
    def __init__(self, domestic, reptiles, birds) -> None:
        super().__init__()
        self.domestic = domestic
        self.reptiles = reptiles
        self.birds = birds

    def select_pet_category():
        fay = input("Enter required category: ")
        if fay == "domestic":
            return (f"You have chosen {fay} category")and input("DOG or CAT?")
        elif fay == "reptiles":
            return (f"You have chosen {fay} category")
        elif fay == "birds":
            return (f"You have chosen {fay} category")
        else:
            return (f"{fay} is invalid try again")
        
    def categories():
        day = input("Please confirm your choice of pet again"; "hgjk")
        if day == "domestic":
            fag = input("Available domestic pets are Cat and Dogs, please chose:")
            if fag == "Cat":
                print("Available Breeds")
                print("Siamese")
                print("British Shorthair")
                print("Maine Coon")
                print("Bombay")
                fav = input("selesct desired breed")
                print(f"You chose {fav}")
                print("Available Colors")
                print("Black")
                print("White")
                print("Orange")
                print("Mixed")
                gay = input("Enter Required Color")
                print(f"You chose {gay}")
                
                print("======Your selection=====")
                print(day)
                print(fag)
                print(fav)
                print(gay)
        else:
             return "wrong input"
     
print(pets.select_pet_category())
print(pets.categories())

        
        
        
class Ordering(pets):
    def __init__(self) -> None:
                super().__init__()

    def account_details():
        print("Pleaes make payments ino the following account details")
        print("09056888997")
        print("Opay")

    def delivery_options():
        print("HOME DELIVERY")
        print("Pickup from store: ")
        hay = input("Select delivery option: ")
        if hay == "Home delivery":
            yay = input("Enter home address: ")
            print(yay)

        elif hay == ("Pickup"):
            print("5am")
            print("3am")
            print("9am")
            print("6am")
            print("10am")
            het = input("Select suitable time for pickup")
            print(het)

    def appreciation():
        print("Thanks for your patronage")

print(Ordering.account_details())
print(Ordering.delivery_options())
print(Ordering.appreciation())