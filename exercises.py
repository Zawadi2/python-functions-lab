# Exercise 1: Calculate Area of a Triangle
#
# Write a function named `calculate_area_triangle` that takes the base and height of a triangle and returns the area.
# The area formula is (base * height) / 2.
#
# Examples:
# calculate_area_triangle(10, 5) should return 25.0.
# calculate_area_triangle(7, 3) should return 10.5.
#
# Define your function and call it below.

def calculate_area_triangle(base, height):
    """
    Calculate the area of a triangle given the base and height.
    Args:
        base (float): The base of the triangle.
        height (float): The height of the triangle.
    Returns:
        float: The area of the triangle.
    """
    return (base * height) / 2



print('Exercise 1:', calculate_area_triangle(10, 5))

# Exercise 2: Calculate Simple Interest
#
# Write a function named `simple_interest` that takes principal, rate of interest (as a percentage), and time (years).
# Calculate and return the simple interest using the formula (principal * rate * time) / 100.
#
# Examples:
# simple_interest(1000, 5, 2) should return 100.
# simple_interest(1500, 3.5, 5) should return 262.5.
#
# Define your function and call it to see the result.

def simple_interest(principal, rate, time, **kwargs):
    print("Additional arguments:", kwargs)
    return principal * rate * time / 100

print('Exercise 2:', simple_interest(1000, 5, 2))


# Exercise 3: Apply a Discount
#
# Write a function named `apply_discount` that takes a product's price and a discount percentage (from 0 to 100).
# Return the new price after applying the discount.
#
# Examples:
# apply_discount(100, 25) should return 75.
# apply_discount(80, 10) should return 72.
#
# Define your function and call it to display the discounted price.


def apply_discount(price, discount, **kwargs):
    if not 0 <= discount <= 100:
        raise ValueError("Discount must be between 0 and 100")
    print(f"Original price: {price}")
    print(f"Discount percentage: {discount}%")
    new_price = price * (1 - discount / 100)
    print(f"Discount amount: {price - new_price}")
    print(f"New price: {new_price}")
    print("Additional arguments:", kwargs)
    return new_price
print('Exercise 3:', apply_discount(100, 25))

# Exercise 4: Convert Temperature
#
# Write a function called `convert_temperature` that takes a
# temperature and a unit ('C' for Celsius, 'F' for Fahrenheit)
# and converts the temperature to the other unit.
# The formula for converting Celsius to Fahrenheit is (Celsius * 9/5) + 32.
# The formula for converting Fahrenheit to Celsius is (Fahrenheit - 32) * 5/9.
#
# Examples:
# convert_temperature(0, 'C') should return 32.0.
# convert_temperature(32, 'F') should return 0.0.
#
# Define the function and then call it below.

def convert_temperature(*args):
    if len(args) != 2:
        raise ValueError("Exactly two arguments required: temperature and unit")
    temp, unit = args
    if unit.upper() == 'C':
        print(f"Converting {temp}°C to Fahrenheit:")
        return (temp * 9/5) + 32
    elif unit.upper() == 'F':
        print(f"Converting {temp}°F to Celsius:")
        return (temp - 32) * 5/9
    else:
        raise ValueError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))


# Exercise 5: Sum to N
#
# Write a function named `sum_to` that takes a single integer n and returns the sum of all integers from 1 to n.
#
# Examples:
# sum_to(6) should return 21.
# sum_to(10) should return 55.
#
# Define the function and then call it below.


def sum_to(n):
    print(f"Calculating sum to {n}:")
    total = 0
    for i in range(1, n + 1):
        print(f"Adding {i} to total")
        total += i
    print(f"Sum to {n}: {total}")
    return total

print('Exercise 5:', sum_to(6))


# Exercise 6: Find the Largest Number
#
# Write a function named `largest` that takes three integers as arguments and returns the largest of them.
#
# Examples:
# largest(1, 2, 3) should return 3.
# largest(10, 4, 2) should return 10.
#
# Define your function and test it with different inputs.

def largest(*args):
    print("Finding the largest number:")
    for num in args:
        print(f"Considering {num}")
    return max(args)

print('Exercise 6:', largest(1, 2, 3))


# Exercise 7: Calculate a Tip
#
# Create a function called `calculate_tip`. It should take the bill amount and the tip percentage (as a whole number).
# The function should return the amount of the tip.
#
# Examples:
# calculate_tip(50, 20) should return 10.
#
# Write your function and test its output below.

def calculate_tip(bill_amount, tip_percentage):
    print(f"Calculating tip for bill amount ${bill_amount} and tip percentage {tip_percentage}%:")
    tip_amount = (bill_amount / 100) * tip_percentage
    print(f"Tip amount: ${tip_amount}")
    return tip_amount

print('Exercise 7:', calculate_tip(50, 20))


# Exercise 8: Calculate Product of Numbers
#
# Write a function named `product` that takes an arbitrary number of numbers, multiplies them, and returns the product.
# Review your notes on *args for handling an arbitrary number of arguments.
#
# Examples:
# product(-1, 4) should return -4.
# product(2, 5, 5) should return 50.
#
# Define the function and call it with different sets of numbers to test.

def product(*args):
    print("Calculating product:")
    result = 1
    for num in args:
        print(f"Multiplying by {num}")
        result *= num
    print(f"Product: {result}")
    return result

print('Exercise 8:', product(2, 5, 5))


# Exercise 9: Basic Calculator
#
# Create a function named `basicCalculator` that takes three arguments: 
# two numbers and a string representing an operation ('add', 'subtract', 'multiply', 'divide'). 
# Perform the provided operation on the two numbers. In operations where the order of numbers is important, 
# treat the first parameter as the first operand and the second parameter as the second operand.
#
# Examples:
# basicCalculator(10, 5, 'subtract') should return 5.
# basicCalculator(10, 5, 'add') should return 15.
# basicCalculator(10, 5, 'multiply') should return 50.
# basicCalculator(10, 5, 'divide') should return 2.
#
# Define the function and then call it below.

def basicCalculator(num1, num2, operation):
    print(f"Performing {operation} operation on {num1} and {num2}:")
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            raise ValueError("Cannot divide by zero!")
    else:
        raise ValueError("Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'.")
    print(f"Result: {result}")
    return result

print('Exercise 9 Result:', basicCalculator(10, 5, "subtract"))
