


def list_to_dict(list):
    # Using enumerate and a for loop to convert the list into a dictionary
    result_dict = {index: value for index, value in enumerate(list)}
    return result_dict

# Example usage with list1
list1 = [1, 2, 3, 4]
result_dict = list_to_dict(list1)

# Print the resulting dictionary
print(result_dict)

#output
#   {0: 1, 1: 2, 2: 3, 3: 4}