import sys

sys.setrecursionlimit(3000)


def quicksort(arr, starting_index, ending_index):
    if starting_index < ending_index:
        q = partition(arr, starting_index, ending_index)
        quicksort(arr, starting_index, q-1)
        quicksort(arr, q+1, ending_index)


def partition(arr, starting_index, ending_index):
    pointer = arr[ending_index]
    starting_target = starting_index - 1
    for j in range(starting_index, ending_index):
        if arr[j] <= pointer:
            starting_target = starting_target+1
            arr[starting_target], arr[j] = arr[j], arr[starting_target]
    arr[starting_target+1], arr[ending_index] = arr[ending_index], arr[starting_target+1]
    return starting_target + 1


def quicksort_function(arr):
    quicksort(arr, 0, len(arr)-1)
    return arr


def main():
    A = [1, 3, 2, 9, 7, 4, 5]
    B = [3, 5, 1]
    C = [81, 45, 32, -12, 0, 43, 87]

    print(quicksort_function(A))
    print(quicksort_function(B))
    print(quicksort_function(C))


if __name__ == "__main__":
    main()
