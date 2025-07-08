import math

def f(x):
    return x + math.log(x) - 0.5

def bisection(a, b, epsilon):
    if f(a) * f(b) >= 0:
        print("Функция должна иметь разные знаки на концах отрезка.")
        return None, None, None
    
    iterations = 0
    while (b - a) / 2 > epsilon:
        midpoint = (a + b) / 2
        if f(midpoint) == 0:
            return midpoint, iterations, iterations
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        iterations += 1
    
    return (a + b) / 2, iterations, (b - a) / 2

def iteration(x0, epsilon):
    iterations = 0
    x1 = x0
    
    while True:
        x1 = 0.5 - math.log(x1)
        iterations += 1
        
        if abs(x1 - x0) < epsilon:
            break
        
        x0 = x1
    
    return x1, iterations

method_choice = input("метод ").strip().lower()
epsilon = float(input("ε: "))

if method_choice == "1":
    a = float(input("a: "))
    b = float(input("b: "))
    
    root_bisect, iter_bisect, precision_bisect = bisection(a, b, epsilon)
    
    print(f"{root_bisect}, Точность: {epsilon}, Итерации: {iter_bisect}")

elif method_choice == "2":
    x0 = float(input("Введите приближение x0: "))
    
    root_iter, iter_iter = iteration(x0, epsilon)
    
    print(f"{root_iter}, Итерации: {iter_iter}")