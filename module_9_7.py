def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 2:
            print("Составное")
            return result

        for i in range(2, int(result ** 0.5) + 1):
            if result % i == 0:
                print("Составное")
                return result

        print("Простое")
        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result1 = sum_three(2, 3, 6)
print(f"Результат: {result1}")

result2 = sum_three(3, 2, 1)
print(f"Результат: {result2}")

result3 = sum_three(5, 5, 5)
print(f"Результат: {result3}")