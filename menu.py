# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered

order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")

            for key, value in menu[menu_category_name].items():
                num_item_spaces = 24 - len(key)
                item_spaces = " " * num_item_spaces
                print(f"{i}      | {key}{item_spaces} | ${value}")
                menu_items[i] = {
                    "Item name": key,
                    "Price": value
                }
                i += 1

            # 2. Ask customer to input menu item number
            item_number = input("Please enter the item number you wish to order: ")

            # 3. Check if the customer typed a number
            if item_number.isdigit():
                item_number = int(item_number)  # Convert the menu selection to an integer

                # 4. Check if the menu selection is in the menu items
                if item_number in menu_items.keys():
                    # Store the item name as a variable
                    item_name = menu_items[item_number]["Item name"]
                    item_price = menu_items[item_number]["Price"]

                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"How many of '{item_name}' would you like? (Default is 1): ")

                    # Check if the quantity is a number, default to 1 if not
                    if not quantity.isdigit():
                        quantity = 1
                    else:
                        quantity = int(quantity)

                    # Add the item name, price, and quantity to the order list
                    order_list.append({
                        "Item name": item_name,
                        "Price": item_price,
                        "Quantity": quantity
                    })
                else:
                    # Tell the customer they didn't select a menu option
                    print("Invalid menu item number.")
            else:
                # Tell the customer that their input isn't valid
                print("Please enter a valid number for the menu item.")

    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    # Asking if the customer wants to order more
    while True:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()

        match keep_ordering:
            case "y":
                break
            case "n":
                place_order = False
                print("Thank you for your order.")
                break
            case _:
                print("Please enter 'Y' for yes or 'N' for no.")


# Print out the customer's order
print("This is what we are preparing for you.\n")

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for order_item in order_list:
    # 7. Store the dictionary items as variables
    item_name = order_item["Item name"]
    price = order_item["Price"]
    quantity = order_item["Quantity"]

    # 8. Calculate the number of spaces for formatted printing
    name_spaces = 27 - len(item_name)
    price_spaces = 7 - len(f"{price}")

    # 9. Create space strings
    name_spacing = ' ' * name_spaces
    price_spacing = ' ' * price_spaces

    # 10. Print the item name, price, and quantity
    print(f"{item_name}{name_spacing}| ${price}{price_spacing}| {quantity}")

# 11. Calculate the cost of the order using list comprehension
total_cost = sum(item["Price"] * item["Quantity"] for item in order_list)

# And print the total prices.
print("\nTotal cost: $" + "{:.2f}".format(total_cost))
1
