def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

def main():
    # Prompt the user to enter the original price and discount percentage
    original_price = float(input("Enter the original price of the item: $"))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price after applying the discount
    final_price = calculate_discount(original_price, discount_percent)

    # Print the final price
    if final_price == original_price:
        print("No discount applied. Final price: $", final_price)
    else:
        print("Final price after applying the discount: $", final_price)

if __name__ == "__main__":
    main()
