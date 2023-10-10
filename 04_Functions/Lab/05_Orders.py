# Write a function that calculates the total price of an order and returns it. The function should receive one of the following products: "coffee", "coke", "water", or "snacks", and a quantity of the product. The prices for a single piece of each product are:

# · coffee - 1.50

# · water - 1.00

# · coke - 1.40

# · snacks - 2.00

# Print the result formatted to the second decimal place. 


def calculate_total_price(product, quantity):
    if product == 'coffee':
        return f'{1.50 * quantity:.2f}'
    elif product == 'coke':
        return f'{1.40 * quantity:.2f}'
    elif product == 'water':
        return f'{1.00 * quantity:.2f}'
    elif product == 'snacks':
        return f'{2.00 * quantity:.2f}'

product = input()
product = int(input())
result = calculate_total_price(product,quantity)
print(result)