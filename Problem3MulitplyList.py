# Francisco Sanchez
# 11/08/23

# Define a function to multiply all the numbers in a list.
def multiplyListElements(numbers):
    result = 1

    # Iterate through the list of numbers.
    for number in numbers:
        result *= number  # Multiply the current number with the accumulated result.

    return result  # Return the final product.

# Define the list of numbers.
my_list = [5, 2, 7, -1]

# Call the function to multiply all the numbers in the list and store the results.
result = multiplyListElements(my_list)

# Print the result.
print(f"The product of the numbers in the list is: {result}")