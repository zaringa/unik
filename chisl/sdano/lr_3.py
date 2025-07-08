import math

def f(x):
    return x + math.log(x) - 0.5

def df(x):
    return 1 + 1.0 / x

def newton(x0, epsilon, max_iter=1000):
    iterations = 0
    x = x0
    
    for i in range(max_iter):
        try:
            fx = f(x)
            dfx = df(x)
        except ValueError:
            print("Ошибка: x должен быть положительным!")
            return None, None
        except ZeroDivisionError:
            print("Ошибка: деление на ноль в производной!")
            return None, None
        
        if abs(dfx) < 1e-12:
            print("Производная слишком мала, метод расходится")
            return None, None
        
        x_new = x - fx / dfx
        iterations += 1
        
        if abs(f(x_new)) < epsilon:
            return round(x_new, 10), iterations
        
        x = x_new
    
    print("Достигнуто максимальное число итераций!")
    return None, iterations

def chord(a, b, epsilon, max_iter=1000):
    if f(a) * f(b) >= 0:
        print("Функция должна иметь разные знаки на концах отрезка")
        return None, None
    
    iterations = 0
    x_prev = a
    
    for i in range(max_iter):
        try:
            x_new = b - f(b) * (b - a) / (f(b) - f(a))
        except ZeroDivisionError:
            print("Деление на ноль в методе хорд")
            return None, None
        
        iterations += 1
        
        if abs(f(x_new)) < epsilon or abs(x_new - x_prev) < epsilon:
            return round(x_new, 10), iterations
        
        if f(a) * f(x_new) < 0:
            b = x_new
        else:
            a = x_new
        
        x_prev = x_new
    
    print("Достигнуто максимальное число итераций!")
    return None, iterations

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число!")

if __name__ == "__main__":
    print("Выберите метод:")
    print("1 - Метод Ньютона")
    print("2 - Метод хорд")
    
    choice = input().strip()
    epsilon = get_float_input("Введите точность ε: ")
    
    if choice == "1":
        x0 = get_float_input("Введите начальное приближение x0 (>0): ")
        root, iterations = newton(x0, epsilon)
        
    elif choice == "2":
        a = get_float_input("Введите левую границу a (>0): ")
        b = get_float_input("Введите правую границу b (>0): ")
        root, iterations = chord(a, b, epsilon)
        
    else:
        print("Некорректный выбор метода!")
        exit()
    
    if root is not None:
        print(f"Корень: {root:.10f}")
        print(f"Итераций: {iterations}")
    else:
        print("\nРешение не найдено!")