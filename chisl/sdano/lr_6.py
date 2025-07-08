import numpy as np
import pandas as pd

def f(x):
    return np.sin(x) / (1 + np.cos(x))

I_exact = np.log(2)

def rectangle(a, b, n):
    h = (b - a) / n
    integral_sum = sum(f(a + i * h) for i in range(n))
    return h * integral_sum

a = 0
b = np.pi / 2

results = []

for n in [10, 100, 1000, 10000]:
    I_n = rectangle(a, b, n)
    error = abs(I_n - I_exact)
    results.append((n, I_n, error))

df_results = pd.DataFrame(results, columns=['I_n', 'Absolute Error'])
print(df_results)

print(f"значение интеграла {I_exact}")
