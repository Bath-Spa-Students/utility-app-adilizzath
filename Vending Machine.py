from prettytable import PrettyTable
import pyfiglet

# Displaying the title using pyfiglet
title = pyfiglet.figlet_format("Adhils Vending Machine !", font="slant")
print(title)

# Define the items
A1 = {"Item": "DrPepper", "Price": "4.00", "Stock": "9"}
A2 = {"Item": "Fanta", "Price": "3.00", "Stock": "7"}

B1 = {"Item": "Maltesers", "Price": "3.50", "Stock": "12"}
B2 = {"Item": "Galaxy", "Price": "3.50", "Stock": "9"}

C1 = {"Item": "Chocolate Cake", "Price": "4.00", "Stock": "4"}
C2 = {"Item": "Cheese Cake", "Price": "7.00", "Stock": "2"}

D1 = {"Item": "Lays", "Price": "1.00", "Stock": "21"}
D2 = {"Item": "Cheetos", "Price": "2.50", "Stock": "8"}

E1 = {"Item": "Chocolate Juice", "Price": "1.50", "Stock": "11"}
E2 = {"Item": "Strawberry Juice", "Price": "1.50", "Stock": "7"}

F1 = {"Item": "Chupa Chups", "Price": "1.50", "Stock": "7"}
F2 = {"Item": "Sour patch", "Price": "3.00", "Stock": "8"}

items = [A1, A2, B1, B2, C1, C2, D1, D2, E1, E2, F1, F2]

# Create a table to display items
table = PrettyTable()
table.field_names = ["Item", "Price", "Stock"]

for item in items:
    table.add_row([item["Item"], item["Price"], item["Stock"]])

print("Items Available for Purchase:")
print(table)

ITEMS = input("Enter the name of the item you want to buy: ")
item_code = None

for i in items:
    if ITEMS.lower() == i['Item'].lower():
        item_code = i
        break

if item_code is None:
    print("INVALID ITEM")
else:
    print(f"Awesome, {item_code['Item']} will cost you {item_code['Price']} $")

    price = float(input(f"Enter {item_code['Price']} dollars to purchase: "))
    if price == float(item_code['Price']):
        print(f"Thank you for your purchase. Here is your {item_code['Item']}.")
    else:
        print(f"Please enter only {item_code['Price']} $.")
