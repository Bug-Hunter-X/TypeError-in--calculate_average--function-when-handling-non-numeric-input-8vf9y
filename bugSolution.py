def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle empty list or list with only non-numeric values
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_list = [10, 20, 30, 40, 50]
result = calculate_average(my_list)
print(f"The average is: {result}")

my_empty_list = []
result = calculate_average(my_empty_list) # This will correctly return 0
print(f"The average of an empty list is: {result}")

my_list_with_string = [10,20,'a',30]
result = calculate_average(my_list_with_string) #this will return the average of numbers only
print(f"The average of list with string is: {result}") 