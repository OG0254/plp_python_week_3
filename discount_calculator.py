def calculate_discount(price, discount_percent):
    """
    Function to calculate the final price after applying discount
    Only applies discount if discount_percent is >= 20
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt the user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(price, discount_percent)

# Display the result
print("The final price is:", final_price)
