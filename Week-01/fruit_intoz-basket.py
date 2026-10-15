def total_fruit(fruits):
    basket = {}
    left = 0
    max_fruits = 0
 
    for right in range(len(fruits)):
        basket[fruits[right]] = basket.get(fruits[right], 0) + 1
 
        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1
 
        max_fruits = max(max_fruits, right - left + 1)
 
    return max_fruits
 
 
if __name__ == "__main__":
    print(total_fruit([1, 2, 1]))                    # Expected: 3
    print(total_fruit([0, 1, 2, 2]))                 # Expected: 3
    print(total_fruit([1, 2, 3, 2, 2]))              # Expected: 4
    print(total_fruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))  # Expected: 5
 
