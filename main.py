import time


def fast_pow(x, n):
    r = 1
    while n > 0:
        if n - 2 * (n >> 1) == 1:
            r *= x
        x *= x
        n = n >> 1
    return r


def main():
    print("Данная программа предназначена для быстрого возведения числа в степень")

    x = int(input("Введите основание степени: "))
    while x < 0:
        x = int(input("Произошла ошибка! Попробуйте еще раз: "))

    n = 0
    results = []
    while n != 50000:
        start_time = time.monotonic()
        fast_pow(x, n)
        elapsed_time = time.monotonic() - start_time

        # print(f"{x}^{n} = {fast_pow(x, n)}")

        results.append(elapsed_time)
        n += 100

    print(f"Время выполнения: {results}")


main()
