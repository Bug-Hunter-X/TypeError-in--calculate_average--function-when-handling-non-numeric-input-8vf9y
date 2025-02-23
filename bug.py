def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = [10, 20, 30, 40, 50]
result = calculate_average(my_list)
print(f"The average is: {result}")

my_empty_list = []
result = calculate_average(my_empty_list) # This will correctly return 0
print(f"The average of an empty list is: {result}")

my_list_with_string = [10,20,'a',30]
result = calculate_average(my_list_with_string)