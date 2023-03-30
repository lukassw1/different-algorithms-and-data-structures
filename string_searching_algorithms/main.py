import time
import gc
from matplotlib import pyplot as plt
from naive_algorithm import naive_algorithm
from KR_algorithm import KR_search
from KMP_algorithm import kmp_algorithm

word_count = [50, 100, 150, 200, 250, 300, 350, 400] #, 5000, 6000, 7000, 8000, 9000, 10000]


def read_file(path):
    with open(path) as fh:
        data = make_data(fh)
    return data


def make_data(handle):
    word_list = []
    lines = handle.readlines()
    for line in lines:
        line.strip()
        line = line.lower()
        for word in line.split():
            word_list.append(word)
    return word_list


def make_txt(amount, data):
    txt = ""
    for i in range(amount):
        txt += data[i]
    return txt


def calculate_time(finding_function, text, data):
    sort_times = []

    for words in word_count:
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for i in range(words):
            finding_function(data[i], text)
        stop = time.process_time()
        sort_time = stop - start
        sort_times.append(sort_time)
        if gc_old: gc.enable()
    return sort_times

def plot(title, naive_times, kr_times, kmp_times, filename):
    plt.plot()
    plt.title(title)
    plt.plot(word_count, naive_times, label="Naive times")
    plt.plot(word_count, kr_times, label="KR times")
    plt.plot(word_count, kmp_times, label="KMP times")
    plt.xlabel("word amount")
    plt.ylabel("time")
    plt.legend()
    plt.savefig(filename)


def main():
    DATA = read_file("pan_tadeusz.txt")
    text = make_txt(len(DATA), DATA)
    naive_times = calculate_time(naive_algorithm, text, DATA)
    print(naive_times)
    kr_times = calculate_time(KR_search, text, DATA)
    print(kr_times)
    kmp_times = calculate_time(kmp_algorithm, text, DATA)
    print(kmp_times)
    plot("Search times", naive_times, kr_times, kmp_times, "plot1.png")


if __name__ == "__main__":
    main()
