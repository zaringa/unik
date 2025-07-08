import numpy as np
import pandas as pd

def f(x):
    return np.sin(x) / (1 + np.cos(x))

I_exact = np.log(2)

def simps(a, b, n):
    if n % 2 == 1:
        n += 1
    
    h = (b - a) / n
    integral_sum = f(a) + f(b)
    
    for i in range(1, n, 2):
        integral_sum += 4 * f(a + i * h)
    
    for i in range(2, n-1, 2):
        integral_sum += 2 * f(a + i * h)
    
    return (h / 3) * integral_sum

a = 0
b = np.pi / 2

results = []
prev_error = None

for n in [10, 20, 40, 80]:
    I_n = simps(a, b, n)
    error = abs(I_n - I_exact)
    ratio = prev_error / error if prev_error is not None else np.nan
    results.append((n, I_n, error, ratio))
    prev_error = error

df_results = pd.DataFrame(results, columns=['n', 'I_n', 'Погрешность', 'R(i-1)/R(i)'])
print(df_results)

print(f"\nТочное значение интеграла: {I_exact}")