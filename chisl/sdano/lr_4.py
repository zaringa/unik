import numpy as np

def F(X):
    x, y = X
    return np.array([np.sin(x - 1) - (1.3 - y), x - np.sin(y + 1) - 0.8])

def J(X):
    x, y = X
    return np.array([[np.cos(x - 1), 1],
                     [1, -np.cos(y + 1)]])

def newton_method(initial_guess, epsilon, max_iterations=100):
    X = np.array(initial_guess, dtype=float)
    for _ in range(max_iterations):
        J_inv = np.linalg.inv(J(X))
        F_val = F(X)
        X_new = X - J_inv @ F_val
        
        if np.linalg.norm(F(X_new)) < epsilon:
            return X_new
        
        X = X_new
    
    return None

initial_guess = [2, 0]
epsilon = 1e-6

root_newton = newton_method(initial_guess, epsilon)
print(f"x={root_newton[0]}, y={root_newton[1]}")