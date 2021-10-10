import multiprocessing
import time


def create_dev(number, sender):

    sending_list = [i for i in range(1, number + 1) if number % i == 0]

    sender.send(sending_list)


def factorize(*numbers):
    process_list = []
    pipe_list = []

    for number in numbers:
        receiver, sender = multiprocessing.Pipe()
        p = multiprocessing.Process(target=create_dev, args=(number, sender))
        process_list.append(p)
        pipe_list.append(receiver)
        p.start()

    for process in process_list:
        process.join()
    return [x.recv() for x in pipe_list]


if __name__ == '__main__':
    start = time.perf_counter()

    a, b, c, d = factorize(128, 255, 99999, 10651060)

    print(a)
    print(b)
    print(c)
    print(d)

    finish = time.perf_counter()

    print(f"Finished at {round(finish - start, 2)} sec")

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158,
                 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212,
                 2662765, 5325530, 10651060]
