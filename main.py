from tasks_checker import TaskChecker

user_solution = 'def find_maximum(arr): \n return max(arr)'

test_cases = [
    ([0, 2, 3, 4, 5], 5),
    ([-1, -5, 0, -10], 0),
    ([100, 200, 50, 300], 300),
    ([0, 0, 0, 0], 0),
]

print(TaskChecker(user_solution, test_cases).check())
