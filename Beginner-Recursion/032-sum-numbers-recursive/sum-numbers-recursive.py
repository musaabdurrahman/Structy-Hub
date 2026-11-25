def sum_numbers_recursive(numbers):
  
    if numbers == []:
        return 0
    else:
        first_number = numbers[0]
        numbers.pop(0)
        return first_number + sum_numbers_recursive(numbers)
    
    
print(sum_numbers_recursive([5, 2, 9, 10]))