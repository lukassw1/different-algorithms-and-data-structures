def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def main():
    A = [1, 3, 2, 9, 7, 4, 5]
    B = [3, 5, 1]
    C = [81, 45, 32, -12, 0, 43, 87]
    print(bubble_sort(A))
    print(bubble_sort(B))
    print(bubble_sort(C))


if __name__ == "__main__":
    main()
