import numpy as np

# Original traffic matrix
A = np.array([
    [200, 150],
    [100, 250]
])

# Transformation matrix
T = np.array([
    [0.8, 0.2],
    [0.3, 0.7]
])

# Simulate new traffic after signal optimization
A_new = np.dot(A, T)

# Print original and new traffic data
print("Original Traffic Matrix:")
print(A)

print("Transformation Matrix T:")
print(T)

print("New Traffic Matrix after signal optimization:")
print(A_new)

print("Total traffic before optimization:", np.sum(A))
print("Total traffic after optimization:", np.sum(A_new))