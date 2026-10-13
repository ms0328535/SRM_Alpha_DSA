
arr = [1, 2, 2, 3, 4, 4, 5]

result = []

for num in arr:
    if num not in result:
        result.append(num)

print("Array without duplicates:", result)
