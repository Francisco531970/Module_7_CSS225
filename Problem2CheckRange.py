# Francisco Sanchez
# 11/08/23

# Define a function to check whether a number is in a given range.
def checkNumberInRange(number, my_range):
    if number in my_range:
        print(f"{number} is in the range {my_range}")
    else:
        print(f"{number} is not in the range {my_range}")

# Define the range (1 to 10) using the range() function.
my_range = range(1, 10)

# Change this to the number you want to check.
number_to_check = 5

# Call the function to check if 'number_to_check' is in 'my_range'.
checkNumberInRange(number_to_check, my_range)