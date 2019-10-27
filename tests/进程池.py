import time

from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor


def task(i):

    print(i)
    time.sleep(2)


if __name__ == '__main__':
    p = ThreadPoolExecutor(10)
    for i in range(100):
        p.submit(task, i)

