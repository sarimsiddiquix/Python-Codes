print("Welcome to the Easy Shop!")

# Display product categories
print("\nProduct Categories:")
print("1. Gadgets")
print("2. Apparel")
print("3. Literature")

# User selects a category
category_number = int(input("Select a category (1-3): "))

if category_number == 1:
    print("\nGadgets:")
    print("1. Smartphone - $500")
    print("2. Laptop - $1000")
    print("3. Headphones - $150")
    print("4. Smartwatch - $250")
    print("5. Camera - $700")
    product_prices = [500, 1000, 150, 250, 700]

elif category_number == 2:
    print("\nApparel:")
    print("1. T-Shirt - $20")
    print("2. Jeans - $40")
    print("3. Jacket - $80")
    print("4. Sneakers - $60")
    print("5. Dress - $50")
    product_prices = [20, 40, 80, 60, 50]

elif category_number == 3:
    print("\nLiterature:")
    print("1. Novel - $15")
    print("2. Textbook - $30")
    print("3. Comic - $10")
    print("4. Biography - $25")
    print("5. Cookbook - $20")
    product_prices = [15, 30, 10, 25, 20]

else:
    print("Invalid category selection. Please enter a number between 1 and 3.")
    product_prices = []

# Proceed if the category selection was valid
if product_prices:
    product_number = int(input("Select a product (1-5): "))

    if 1 <= product_number <= 5:
        selected_price = product_prices[product_number - 1]

        # Display selected product price and ask for checkout confirmation
        print(f"\nThe price of the selected product is: ${selected_price}")
        confirm_purchase = input("\nWould you like to proceed to checkout? (yes/no): ").strip().lower()

        if confirm_purchase == "yes":
            print(f"\nThank you for your purchase! Your total amount is ${selected_price}.")
        else:
            print("\nYour cart has been cleared. Thank you for visiting!")
    else:
        print("Invalid product selection. Please enter a number between 1 and 5.")