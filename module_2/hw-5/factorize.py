import multiprocessing
import time


def factorize(numbers):
    results = []

    for number in numbers:
        [results.append(i) for i in range(1, number + 1) if number % i == 0]

    with open('test.txt', 'w') as fh:
        fh.write(results)

    return None


if __name__ == '__main__':
    start = time.perf_counter()
    # numbers = [128, 255, 99999, 10651060, 444444444, 44444444, 6644666]
    # a, b, c, d = factorize(128, 255, 99999, 10651060)

    # with multiprocessing.Pool(processes=4) as p:
    #     p.apply_async(factorize, 128)
    #     p.apply_async(factorize, 255)
    #     p.apply_async(factorize, 99999)
    #     p.apply_async(factorize, 10651060)

    finish = time.perf_counter()

    print(f"Finished at {round(finish - start, 2)} sec")

#
# assert a == [1, 2, 4, 8, 16, 32, 64, 128]
# assert b == [1, 3, 5, 15, 17, 51, 85, 255]
# assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
# assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158,
#              304316, 380395, 532553, 760790, 1065106, 1521580, 2130212,
#              2662765, 5325530, 10651060]
