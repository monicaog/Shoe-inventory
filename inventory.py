CYAN = '\033[96m'
BOLD = '\033[1m'
ENDC = '\033[0m'
YELLOW = '\033[93m'

#========The beginning of the class==========
class Shoe:

    #Constructor that initialises the attributes: country, code, product, cost, and quantity.
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    #Creates method get_cost. It returns the cost of the shoe
    def get_cost(self):
        return(self.cost)

    #Creates method get_product. It returns the product
    def get_product(self):
        return(self.product)

    #Creates method get_quantity. It returns the quantity of the shoe
    def get_quantity(self):
        return(self.quantity)

    #Creates method get_code. It returns the code of the shoe
    def get_code(self):
        return(self.code)

    #Creates method to to returns a string representation of a class
    def __str__(self):
        output = f'''{CYAN}\n
        -------------------------------
        Country:  {self.country}
        Code:     {self.code}
        Product:  {self.product}
        Cost:     {self.cost}
        Quantity: {self.quantity}
        -------------------------------{ENDC}'''
        return(output)


#=============Shoe list===========

#The list will be used to store a list of objects of shoes.
shoe_list = []

#==========Functions outside the class==============
#Creates function read_shoes_data - It reads the data from file "inventory.txt" and it creates a shoe object with the data and append
#this object to the shoe list
def read_shoes_data():
    try:
        file = open("inventory.txt", "r")
        contents = file.readlines()
        for counter, content in enumerate (contents):
            #It splits every word on the line on the variable assigned
            cou,cod,pro,cos,quan = content.split(",",5)
            #Skipping the first line
            if counter != 0:
                #Creates a shoe object and appends it to the shoe_list
                shoe_list.append(Shoe(cou,cod,pro,cos,quan))
    except FileNotFoundError:
            print(f"{CYAN}The text file cannot be found, please check your folder and try again{ENDC}")
    return()

#Creates function capture_shoes - Allows an user to enter data about a shoe and use this data to create a shoe object and append 
#this object inside the shoe list.
def capture_shoes():
    while True:
        country_input = input("Enter the country: ")
        code_input = input ("Enter the code: ")
        product_input = input ("Enter the product: ")
        cost_input = int (input ("enter the cost: "))
        quantity_input = int(input("Enter the quantity: "))
        try:
            #It validates that the variables are not empty or have a wrong input
            if len(country_input) == 0   or len(code_input) == 0 or len(product_input) == 0 or country_input.isalpha() == False \
            or code_input.isalnum() == False or product_input.isalnum() == False:
                print(f"{CYAN}Error in the inputs, please try again{ENDC}")
            else:
                shoe_list.append(Shoe(country_input,code_input,product_input,cost_input,quantity_input))
                break
        except ValueError:
                print(f"{CYAN}Error in the inputs, please try again{ENDC}")

#Creates function view_all - This functions iterates over the shoe list and print the details of the shoe object
def view_all():
    for shoe in shoe_list:
        print (shoe)
    return()
    
#Creates function search_shoe -It searchs for a product in the shoe_list, using the shoe code and prints it.
def search_shoe():
    contador = 0
    search_code = input("Enter the code of the shoe you would like to search: \n").upper()
    for check in shoe_list:
        if check.get_code() == search_code:
            result = check
            contador = 1
    if contador == 0:
        print(f"{CYAN}We didn't find a product with that code{ENDC}")
    else:
        print(result)
    return()

#Creates function value_per_item - It calculates the total value for each item. (value = cost * quantity)
def value_per_item():
    for each in shoe_list:
        cost_each = each.get_cost()
        quantity_each = each.get_quantity()
        value = int (cost_each)* int(quantity_each)
        print(f'''{CYAN}
{each.get_product()} value = {value} {ENDC}''')
    return()

#Creates function total_quantity - It creates and returns a list with the quantity of shoes available
def total_quantity():
    quantity_list =[]
    for check1 in shoe_list:
        element = check1.get_quantity()
        element = element.replace("\n","")
        quantity_list.append(int(element))
    return(quantity_list)

#Creates function find_product -It finds a product once it has receive the quantity of stock.
def find_product(x):
    for check2 in shoe_list:
        quantity_element = check2.get_quantity()
        quantity_element=quantity_element.strip()
        if quantity_element == str(x):
            return(check2.get_product())

#Creates function re_stock - It finds the shoe object with the lowest quantity (which is the shoes that need to be re-stocked).It asks
#the user if they want to add a quantity to this shoes inventory and then update the file "inventory.txt". It calls functions
#total_quantity() and find_product()
def re_stock():
    final_content = ""
    new_line = ""
    lowest_stock = total_quantity()
    lowest_stock = min(lowest_stock)
    restock_product=find_product(lowest_stock)
    option=input(f'''{CYAN}
The product with the lowest quantity is {restock_product} with a stock of {lowest_stock} shoes,
would you like to add a quantity to this shoes inventory? (yes or no):{ENDC} ''').lower()
    while True:
        #It option is "yes", it asks the user for the quantity that would like to add, open the file, modify the line and rewrite the
        #contents in text file "inventory.txt"
        if option == "yes":
            stock_number = int(input("\nEnter the quantity of stock that you would like to add: "))
            new_stock = stock_number + lowest_stock
            file2 = open("inventory.txt","r")
            contents2 = file2.readlines()
            file2.close()
            
            for counter2, line in enumerate (contents2):
                line = line.split(",")
                if line[2] == restock_product:
                    new_line = line
                    new_line[4] = str(new_stock)
                    edited_line = ",".join(new_line)
                    contents2[counter2] = edited_line + "\n"
            
            for line2 in contents2:
                final_content += line2
            
            #Writes in the text file inventory with the new information about the stock
            file2 = open("inventory.txt","w")
            file2.write(final_content)
            print(f"{CYAN}The inventory file has been updated")
            file2.close()
            break          
        elif option == "no":
            break
        elif option != "yes" and option != "no":
            print(f"{CYAN}wrong option, please try again{ENDC}")
        
        return()
  
#Creates function highest_qty. It determines the product with the highest quantity. it calls the functions total_quantity() and find product()
#and returns the shoe with the highest quantity as being for sale
def highest_qty():
    highest_stock = total_quantity()
    highest_stock = max(highest_stock)
    sale_stock = find_product(highest_stock)
    print(f'''{CYAN} Product On Sale! {sale_stock} {ENDC}''')
    return()

#==========Main Menu=============

user_choice = " "
#Creates a menu that executes each function of the program inventory inside a while loop.
while user_choice != "exit":
    #It requests the user for an input from the menu, it uses method .lower() to avoid errors in the typing.
    user_choice = input(f'''{YELLOW}----------------------------------------------------------------------------------------------------------------
                                Inventory Menu\n
"read inventory"    -   Read the inventory stored on the inventory text file
"capture shoes"     -   Enter new shoe inventory details
"view all"          -   Display all the shoe inventory
"search product"    -   Search for a product using the shoe code
"on sale product"   -   Display the shoe inventory with the highest quantity
"restock"           -   Display the shoe inventory with the lowest quantity and allows to restock it
"value per item"    -   Display the value per item
"exit"              -   Exits the program
----------------------------------------------------------------------------------------------------------------{ENDC} \n''').lower()
    #User's choice is read inventory, it calls function read_shoes_data()
    if user_choice == "read inventory":
        read_shoes_data()
    #User's choice is capture shoes, it calls functions read_shoes_data() and capture_shoes()
    elif user_choice == "capture shoes":
        read_shoes_data()
        capture_shoes()
    #User's choice is view all, it calls functions read_shoes_data() and view_all()
    elif user_choice == "view all":
        read_shoes_data()
        view_all()
    #User's choice is search product, it calls functions read_shoes_data() and search_shoe()
    elif user_choice == "search product":
        read_shoes_data()
        search_shoe()
    #User's choice is on sale product, it calls functions read_shoes_data() and higuest_qty()
    elif user_choice == "on sale product":
        read_shoes_data()
        highest_qty()
    #User's choice is restock, it calls functions read_shoes_data() and re_stock()
    elif user_choice == "restock":
        read_shoes_data()
        re_stock()
    #User's choice is value per item, it calls functions read_shoes_data() amd value_per_item()
    elif user_choice == "value per item":
        read_shoes_data()
        value_per_item()
    #User's choice is exits, it breaks the loop and prints goodbye
    elif user_choice == "exit":
        print (f"{CYAN}Goodbye{ENDC}")
    #It validates that the option entered is incorrect and prints an error message
    else:
        print(f"{CYAN}You have entered an invalid option, please try again{ENDC}")
