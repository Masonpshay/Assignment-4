# Timed Challenge Question:
# Remove Duplicates (Keep Order)
# Return the values in the order they first appeared, without duplicates.
# Input: ["apple", "banana", "apple", "kiwi", "banana"]
# Output: ["apple", "banana", "kiwi"]

def remove_duplicates_keep_order(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Test cases
print(remove_duplicates_keep_order(["apple", "banana", "apple", "kiwi", "banana"]))

print(remove_duplicates_keep_order([]))

print(remove_duplicates_keep_order(["a", "a", "a"]))

print(remove_duplicates_keep_order(["x", "y", "z"]))

"""
Reflection:
I chose question number 3 because it allows fast checking of whether an item has been seen or not and it keeps the original order.
This question seemed more my speed compared to the others because it involves straightforward logic without complex algorithms.
The time limit wasn't the worst thing ever I just personally don't like time limits on coding challenges.
It causes unnecessary stress and can lead to mistakes that wouldn't happen in a normal coding environment.
The timer had 16 minutes left when I finished my code and began typing my reflection.
"""
