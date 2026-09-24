m = 0
shopping_cart = {
    'Name of Item': [],
    'Price of Item': [],
    'Quantity of Item': []
}
num_of_items = 0

def add_item(shopping_cart, item_name, item_price, item_quantity):
    shopping_cart['Name of Item'].append(item_name)
    shopping_cart['Price of Item'].append(item_price)
    shopping_cart['Quantity of Item'].append(item_quantity)
    global num_of_items
    num_of_items += 1
    if len(shopping_cart['Name of Item']) == num_of_items and len(shopping_cart['Price of Item']) == num_of_items and len(shopping_cart['Quantity of Item']) == num_of_items:
          print("Item added successfully!")
          return 
    else:
          print("Failed to add item.")

def list_items(shopping_cart, num_of_items):
     for i in range(num_of_items):
           print(f"Item {i + 1}:")
           print(f"Name: {shopping_cart['Name of Item'][i]}")
           print(f"Price: {shopping_cart['Price of Item'][i]}")
           print(f"Quantity: {shopping_cart['Quantity of Item'][i]}")
           print("-----------------------------------")
     
def hitung_total_price(shopping_cart, num_of_items):
    total_price = 0
    for i in range(num_of_items):
          item_total = shopping_cart['Price of Item'][i] * shopping_cart['Quantity of Item'][i]
          total_price += item_total
    return total_price

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
    try:
         choose = int(input("Choose menu: "))
    except:
         print("Invalid input. Please enter a valid choice.")
         continue
    if choose == 1:
          print("===================================")
          print("           Add Item                ")
          print("===================================")
          item = input("Enter item name: ")
          try: 
            price = int(input("Enter item price: "))
          except:
             print("Invalid input. Please enter a valid price.")
             continue
          try:
            quantity = int(input("Enter item quantity: "))
          except:
            print("Invalid input. Please enter a valid quantity.")
            continue
          add_item(shopping_cart, item, price, quantity)
    elif choose == 2:
      if num_of_items == 0:
           print("No items in the shopping cart.")
           continue
      print("===================================")
      print("           List of Items           ")
      print("===================================")
      list_items(shopping_cart, num_of_items)
      print(' ')

    elif choose == 3:
          if num_of_items == 0:
                print("No items in the shopping cart.")
                continue
          print("===================================")
          print("           Checkout                ")
          print("===================================")
          total_price = hitung_total_price(shopping_cart, num_of_items)
          print(f"Total Price: {total_price}")
    elif choose == 4:
           print("Exiting the program.")
           m = 1
    else:
          print("Invalid choice. Please try again.")

            
        