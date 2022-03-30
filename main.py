import time


def fast_pow(x, n):
    res = 1
    while n > 0:
        if n - 2 * (n >> 1) == 1:
            res *= x
        x *= x
        n = n >> 1
    return res


def main():
    print("Данная программа предназначена для быстрого возведения числа в степень")

    x = int(input("Введите основание степени: "))
    while x < 0:
        x = int(input("Произошла ошибка! Попробуйте еще раз: "))

    n = int(input("Введите показатель степени: "))
    while n < 0:
        n = int(input("Произошла ошибка! Попробуйте еще раз: "))

    start_time = time.monotonic()
    fast_pow(x, n)
    elapsed_time = time.monotonic() - start_time

    print(f"x^n = {fast_pow(x, n)}")
    print(f"Время выполнения: {elapsed_time}")


main()
