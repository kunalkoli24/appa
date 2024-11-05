# Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch
# and bound strategy.


#  0-1 Knapsack problem using dynamic programming
"""
def knapsack_dp(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Input from user
n = int(input("Enter number of items: "))
weights = []
values = []

for i in range(n):
    weight = int(input(f"Enter weight of item {i + 1}: "))
    value = int(input(f"Enter value of item {i + 1}: "))
    weights.append(weight)
    values.append(value)

capacity = int(input("Enter the capacity of the knapsack: "))

max_value = knapsack_dp(weights, values, capacity)
print(f'Maximum value in knapsack: {max_value}')
"""

#  0-1 Knapsack problem using  branch and bound strategy
"""
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def knapsack_branch_bound(capacity, items):
    items = sorted(items, key=lambda x: x.value / x.weight, reverse=True)  # Sort items by value-to-weight ratio
    max_value = 0
    n = len(items)

    def bound(i, current_weight, current_value):
        if current_weight >= capacity:
            return 0
        total_value = current_value
        j = i
        while j < n and current_weight + items[j].weight <= capacity:
            current_weight += items[j].weight
            total_value += items[j].value
            j += 1
        if j < n:
            total_value += (capacity - current_weight) * (items[j].value / items[j].weight)
        return total_value

    def knapsack(i, current_weight, current_value):
        nonlocal max_value
        if i >= n:
            max_value = max(max_value, current_value)
            return
        # Include the next item
        if current_weight + items[i].weight <= capacity:
            knapsack(i + 1, current_weight + items[i].weight, current_value + items[i].value)

        # Exclude the next item and check the bound
        if bound(i + 1, current_weight, current_value) > max_value:
            knapsack(i + 1, current_weight, current_value)

    knapsack(0, 0, 0)
    return max_value


# Input from user
n = int(input("Enter number of items: "))
items = []

for i in range(n):
    weight = int(input(f"Enter weight of item {i + 1}: "))
    value = int(input(f"Enter value of item {i + 1}: "))
    items.append(Item(value, weight))

capacity = int(input("Enter the capacity of the knapsack: "))

max_value = knapsack_branch_bound(capacity, items)
print(f'Maximum value in knapsack: {max_value}')
"""