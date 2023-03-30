def minimum_element(arr, input_index):
    current_min = arr[input_index]
    index_min = input_index
    for index in range(input_index + 1, len(arr)):
        if current_min > arr[index]:
            current_min = arr[index]
            index_min = index
    return index_min


def selection_sort(arr):
    for current_index in range(len(arr) - 1):
        min_index = minimum_element(arr, current_index)
        arr[current_index], arr[min_index] = arr[min_index], arr[current_index]
    return arr


def main():
    A = [1, 3, 2, 9, 7, 4, 5]
    B = [3, 5, 1]
    C = [81, 45, 32, -12, 0, 43, 87]
    print(selection_sort(A))
    print(selection_sort(B))
    print(selection_sort(C))


if __name__ == "__main__":
    main()
