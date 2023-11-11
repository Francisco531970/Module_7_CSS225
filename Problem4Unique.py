# Francisco Sanchez
# 11/08/23

def unique_elements(input_list):
    # Create an empty list to store unique elements
    unique_list = []

    # Iterate through the elements in the input list
    for num in input_list:
        # Check if the current element is not already in the unique_list
        if num not in unique_list:
            # If it's not in the list, add it to the unique_list
            unique_list.append(num)

    # Return the list containing unique elements
    return unique_list

# Provided input list
input_list = [1, 3, 3, 3, 6, 2, 3, 5]
result = unique_elements(input_list)
print(result)