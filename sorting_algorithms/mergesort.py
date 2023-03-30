def merge(left_arr, right_arr):
    left_pointer = 0
    right_pointer = 0
    merged_array = []

    while left_pointer < len(left_arr) and right_pointer < len(right_arr):
        if left_arr[left_pointer] <= right_arr[right_pointer]:
            merged_array.append(left_arr[left_pointer])
            left_pointer += 1
        else:
            merged_array.append(right_arr[right_pointer])
            right_pointer += 1

    while left_pointer < len(left_arr):
        merged_array.append(left_arr[left_pointer])
        left_pointer += 1
    while right_pointer < len(right_arr):
        merged_array.append(right_arr[right_pointer])
        right_pointer += 1

    return merged_array


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_arr = merge_sort(arr[mid:])
    right_arr = merge_sort(arr[:mid])
    return merge(left_arr, right_arr)


def main():
    A = [1, 3, 2, 9, 7, 4, 5]
    B = [3, 5, 1]
    C = [81, 45, 32, -12, 0, 43, 87]
    print(merge_sort(A))
    print(merge_sort(B))
    print(merge_sort(C))


if __name__ == "__main__":
    main()
