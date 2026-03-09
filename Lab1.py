import numpy as np

marks = np.array([
    [50, 60, 70],
    [65, 75, 85],
    [55, 45, 65]
])

print("Student Marks Matrix:")
print(marks)

total_marks = np.sum(marks, axis=1)
print("\nTotal marks of each student:")
print(total_marks)

bonus_marks = marks * 2
print("\nMarks after bonus (doubled):")
print(bonus_marks)