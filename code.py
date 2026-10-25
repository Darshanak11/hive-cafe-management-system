menu = {"Coffee": 60, "Tea": 30, "Sandwich": 90}

print("---- HIVE CAFE MENU ----")
for item, price in menu.items():
    print(item, "- Rs.", price)

item = input("Enter item: ").title()
qty = int(input("Quantity: "))

if item in menu:
    print("Total: Rs.", menu[item] * qty)
else:
    print("Item not available")