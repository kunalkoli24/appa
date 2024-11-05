#  Write a program to solve a fractional Knapsack problem using a greedy method

# Class to represent an item with Profit and weight
class Item:
    def __init__(self, Profit, weight):
        self.Profit = Profit
        self.weight = weight

# Function to solve fractional knapsack
def fractional_knapsack(capacity, items):
    # Sort items by Profit-to-weight ratio in descending order
    items.sort(key=lambda x: x.Profit / x.weight, reverse=True)
    
    total_Profit = 0  # Total Profit in knapsack
    for item in items:
        if capacity >= item.weight:
            # If the knapsack can carry the whole item
            capacity -= item.weight
            total_Profit += item.Profit
        else:
            # Take the fraction of the remaining capacity
            fraction = capacity / item.weight
            total_Profit += item.Profit * fraction
            break  # Knapsack is full after this item
    
    return total_Profit

# Input from user
n = int(input("Enter the number of items: "))
items = []
for i in range(n):
    Profit = float(input(f"Enter Profit of item {i + 1}: "))
    weight = float(input(f"Enter weight of item {i + 1}: "))
    items.append(Item(Profit, weight))

capacity = float(input("Enter the maximum capacity of the knapsack: "))

# Calculate maximum Profit using fractional knapsack
max_Profit = fractional_knapsack(capacity, items)

print(f"Maximum Profit in knapsack: {max_Profit:.2f}")
