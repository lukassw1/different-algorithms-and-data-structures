import time
import gc
from random import sample
from matplotlib import pyplot as plt
from heap import Heap


random_numbers = sample(range(300001), 100000)
number_amount = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]


def make_heap(data, n):
    heap = Heap(n)
    for number in data:
        heap.add(number)
    return heap


def create_heap_times(n):
    times = []
    for number in number_amount:
        data = random_numbers[:number]
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        make_heap(data, n)
        stop = time.process_time()
        singular_time = stop - start
        times.append(singular_time)
        if gc_old: gc.enable()
    return times


def plot(title, time_values_2, time_values_5, time_values_10, filename):
    plt.plot()
    plt.title(title)
    plt.plot(number_amount, time_values_2, label="2")
    plt.plot(number_amount, time_values_5, label="5")
    plt.plot(number_amount, time_values_10, label="10")
    plt.xlabel("number amount")
    plt.ylabel("time")
    plt.legend()
    # plt.savefig(filename)
    plt.show()


def delete_peaks_times(n):
    times=[]
    for number in number_amount:
        data = random_numbers[:number]
        heap = make_heap(data, n)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for element in data:
            heap.remove_max()
            pass
        stop = time.process_time()
        singular_time = stop - start
        times.append(singular_time)
        if gc_old: gc.enable()
    return times


def print_cheap(cheap, n):
    str1 = f'Kopiec {n}-krotny:\n'
    index = 0
    in_row = 0
    row = 0
    while index < len(cheap):
        if in_row + 1 == pow(n, row):
            str1 += str(cheap[index]) + "\n"
            row += 1
            in_row = 0
        else:
            in_row += 1
            str1 += str(cheap[index]) + " "
            if in_row % n == 0:
                str1 += '| '
        index += 1
    return str1


def main():
    create_time_2 = create_heap_times(2)
    create_time_5 = create_heap_times(5)
    create_time_10 = create_heap_times(10)
    plot(f"Creating heap", create_time_2, create_time_5, create_time_10, "create.png")
    delete_time_2 = delete_peaks_times(2)
    delete_time_5 = delete_peaks_times(5)
    delete_time_10 = delete_peaks_times(10)
    plot(f"Deleting heap", delete_time_2, delete_time_5, delete_time_10, "delete.png")


if __name__ == "__main__":
    # main()
    heap = make_heap(random_numbers[:27], 10)
    print(print_cheap(heap.arr, 2))
