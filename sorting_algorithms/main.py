import time
import gc
from matplotlib import pyplot as plt
from quicksort import quicksort_function
from mergesort import merge_sort
from bubblesort import bubble_sort
from selectionsort import selection_sort


word_count = [1000, 2000, 5000, 10000, 20000, 30000, 40000, 50000, 65000]


def make_data(handle):
    word_list = []
    lines = handle.readlines()
    for line in lines:
        line.strip()
        for word in line.split():
            word_list.append(word)
    return word_list


def read_file(path):
    with open(path) as fh:
        data = make_data(fh)
    return data


def calculate_time(sort_function, data):
    sort_times = []

    for words in word_count:
        gc_old = gc.isenabled()
        gc.disable()
        words_to_sort = data[:words]
        start = time.process_time()
        sort_function(words_to_sort)
        stop = time.process_time()
        sort_time = stop - start
        sort_times.append(sort_time)
        if gc_old: gc.enable()
    return sort_times


def save_times(sort_type, times):
    with open("result.txt", "a") as result:
        result.write(f"{sort_type}: \n")
        for i in range(len(times)):
            result.write(f"{word_count[i]} : {times[i]}\n")


def main():
    path = "pan-tadeusz.txt"
    data = read_file(path)

    save_times("\n\nNew attempt", [])
    merge_times = calculate_time(merge_sort, data)
    save_times("Merge Sort", merge_times)
    quick_times = calculate_time(quicksort_function, data)
    save_times("Quick Sort", quick_times)
    bubble_times = calculate_time(bubble_sort, data)
    save_times("Bubble Sort", bubble_times)
    selection_times = calculate_time(selection_sort, data)
    save_times("Selection Sort", selection_times)

    plt.plot()
    plt.title("Sorting algorithms comparison")
    plt.plot(word_count, merge_times, label="merge")
    plt.plot(word_count, quick_times, label="quick")
    plt.plot(word_count, bubble_times, label="bubble")
    plt.plot(word_count, selection_times, label="selection")
    plt.xlabel("words")
    plt.ylabel("time")
    plt.legend()
    plt.savefig("sorting-algorithms.png")


if __name__ == "__main__":
    main()
