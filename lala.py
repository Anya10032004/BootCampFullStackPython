m = 0
shopping_cart = {
    'Name of Item': [],
    'Price of Item': [],
    'Quantity of Item': []
}
num_of_items = 0
while m == 0:
    print("===================================")
    print("           Cassier Program         ")
    print("===================================")
    print(" ")
    print(" ")
    print("1. Add Item")
    print("2. Look list of items")
    print("3. checkout")
    print("4. Exit")
    print(" ")
    choose = input("Choose menu: ")
    choose = int(choose)
    match choose:
        case 1:
             print("===================================")
             print("           Add Item                ")
             print("===================================")
             item = input("Enter item name: ")
             price = int(input("Enter item price: "))
             quantity = int(input("Enter item quantity: "))
             shopping_cart['Name of Item'].append(item)
             shopping_cart['Price of Item'].append(price)
             shopping_cart['Quantity of Item'].append(quantity)
             num_of_items += 1
             if len(shopping_cart['Name of Item']) == num_of_items and len(shopping_cart['Price of Item']) == num_of_items and len(shopping_cart['Quantity of Item']) == num_of_items:
                    print("Item added successfully!")
             else:
                    print("Failed to add item.")
        case 2:
              print("===================================")
              print("           List of Items           ")
              print("===================================")
              if num_of_items == 0:
                    print("No items in the shopping cart.")
              else:
                    for i in range(num_of_items):
                        print(f"Item {i + 1}:")
                        print(f"Name: {shopping_cart['Name of Item'][i]}")
                        print(f"Price: {shopping_cart['Price of Item'][i]}")
                        print(f"Quantity: {shopping_cart['Quantity of Item'][i]}")
                        print("-----------------------------------")
              print("===================================")
        case 3:
              print("===================================")
              print("           Checkout                ")
              print("===================================")
              if num_of_items == 0:
                    print("No items in the shopping cart.")
              else:
                    total_price = 0
                    for i in range(num_of_items):
                         item_total = shopping_cart['Price of Item'][i] * shopping_cart['Quantity of Item'][i]
                         total_price += item_total
                    print(f"Total price: { total_price}")
              print("===================================")
        case 4:
               print("Exiting the program.")
               m = 1

        case _:
            print("Invalid choice. Please try again.")
        