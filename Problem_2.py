# Resource Allocation

# Description:
# Imagine you're a project manager tasked with allocating a limited set of resources (employees, budget, time) across several tasks. You need to distribute these resources in a way that ensures all tasks are completed effectively.

# Given:
# You have 3 tasks:

# Task A: Requires 2 employees, $5000 budget, and 3 weeks duration.
# Task B: Requires 3 employees, $7000 budget, and 4 weeks duration.
# Task C: Requires 1 employee, $3000 budget, and 2 weeks duration.

# Available resources:
# Employees: 6
# Budget: $15000
# Time: 6 weeks

# Constraints:
# All tasks must be completed.
# You cannot exceed the budget, number of employees, or available time.

# Questions:
# How can you allocate resources to ensure all three tasks are completed on time?
# What is the optimal order to execute the tasks?

# Solution Approach:
# The solution requires analyzing how to allocate resources efficiently using linear programming or optimization algorithms.



# Define tasks
tasks = {
    "A": {"employees": 2, "budget": 5000, "time": 3},
    "B": {"employees": 3, "budget": 7000, "time": 4},
    "C": {"employees": 1, "budget": 3000, "time": 2},
}

# Define available resources
available_resources = {
    "employees": 6,
    "budget": 15000,
    "time": 6,
}

# Function to determine if all tasks can be completed
def can_complete_all_tasks(tasks, available_resources):
    total_employees = sum(task["employees"] for task in tasks.values())
    total_budget = sum(task["budget"] for task in tasks.values())
    total_time = max(task["time"] for task in tasks.values())
    
    if (total_employees <= available_resources["employees"] and
        total_budget <= available_resources["budget"] and
        total_time <= available_resources["time"]):
        return True
    return False

# Check if tasks can be completed
if can_complete_all_tasks(tasks, available_resources):
    print("All tasks can be completed.")
else:
    print("Not all tasks can be completed.")
