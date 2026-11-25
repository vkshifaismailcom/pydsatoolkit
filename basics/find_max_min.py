def find_max_min(numbers):
    maximum = numbers[0]
    minimum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num
        elif num < minimum:
            minimum = num

    return maximum, minimum


numbers = [12, 45, 2, 67, 8, 34]

maximum, minimum = find_max_min(numbers)

print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")