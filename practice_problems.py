"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    seen = set()
    for pid in product_ids:
        if pid in seen:
            return True
        seen.add(pid)
    return False

# Test cases
print(has_duplicates([10, 20, 30, 20, 40]))  
print(has_duplicates([1, 2, 3, 4, 5]))       
print(has_duplicates([]))                    
print(has_duplicates([1, 1, 1]))             

# Justification:
# A set allows fast checking if a product ID has been seen before.
# Each ID is checked once and extra memory is used for the set.

"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:
    def __init__(self):
        self.queue = []  

    def add_task(self, task):
        self.queue.append(task)  

    def remove_oldest_task(self):
        if self.queue:
            return self.queue.pop(0)  
        return None

# Test cases
tasks = TaskQueue()
tasks.add_task("Email follow-up")
tasks.add_task("Code review")
print(tasks.remove_oldest_task())  
print(tasks.remove_oldest_task())  
print(tasks.remove_oldest_task())  


# Justification:
# A list preserves order and allows adding to the end quickly.
# Removing from the front is simple but slightly slower for long lists.

"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.seen = set()  

    def add(self, value):
        self.seen.add(value)  

    def get_unique_count(self):
        return len(self.seen)  

# Test cases
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
print(tracker.get_unique_count())  
tracker.add(30)
print(tracker.get_unique_count())  
tracker.add(20)
print(tracker.get_unique_count())  

# Justification:
# A set ensures uniqueness automatically and allows fast checking.
# Counting unique values is as simple as getting the length of the set.