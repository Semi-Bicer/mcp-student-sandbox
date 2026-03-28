def average_ratios(numbers):
    valid_ratios = []
    for num in numbers:
        if num == 0:
            print(f"Warning: Division by zero encountered for value {num}")
            continue
        
        try:
            ratio = 100 / num
            valid_ratios.append(ratio)
        except ZeroDivisionError:
            print(f"Error: Cannot divide by {num}")
            continue
    
    if not valid_ratios:
        raise ValueError("No valid numbers to calculate average")
    
    return sum(valid_ratios) / len(valid_ratios)


print(average_ratios([10, 5, 0]))
