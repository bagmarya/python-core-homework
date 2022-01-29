import time

from ex2 import fetcher

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """
    def wrapper(func):
        def wrapped(*args, **kwargs):
            total = 0
            for _ in range(num):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                print(f'Время выполнения: {end - start}')
                total += (end - start)
            print(f'Среднее время выполнения: {total / num}')
        return wrapped
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)

if __name__ == "__main__":
    fetch_page('https://google.com')