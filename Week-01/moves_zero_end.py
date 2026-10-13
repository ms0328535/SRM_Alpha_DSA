
arr = [0, 1, 0, 3, 12]

result = []

for num in arr:
    if num != 0:
        result.append(num)

zeros = len(arr) - len(result)

result.extend([0] * zeros)

print("Result:", result)
