# numbers = [10, 20, 30, 40]

# numbers.append(50)
# print("After append:", numbers)

# numbers.insert(0, 5)
# print("After insert:", numbers) 
# numbers = [5, 12, 18, 25, 40, 55]
# target = 40
def linear_search(numbers, target):
    for i in range(len(numbers)):
        if target==numbers[i]:
            return i
    return -1
numbers = [5, 12, 18, 25, 40, 55]
result=linear_search(numbers,40)
print(result)





