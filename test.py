def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers
numbers = [64, 33, 21, 12, 22, 11, 89]
sorted_numbers = bubble_sort(numbers)
print("排序后的列表:", sorted_numbers)
