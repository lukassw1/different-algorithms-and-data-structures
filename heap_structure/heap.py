
class Heap:
    def __init__(self, size):
        self.arr = []
        self.size = size

    def heapify(self, index):
        if self.size*index+1 > len(self.arr) - 1:
            return
        largest_index = index
        largest_element = self.arr[self.size*index+1]
        arr_len = len(self.arr)
        for i in range(self.size):
            temp_index = self.size * index + 1 + i
            if largest_index < arr_len and largest_element > self.arr[largest_index]:
                largest_index = temp_index
        if largest_index != index:
            self.arr[largest_index], self.arr[index] = self.arr[index], self.arr[largest_index]
            self.heapify(largest_index)

    def add(self, value):
        index = len(self.arr)
        self.arr.append(value)
        # restore heap
        while index != 0:
            parent_index = (index - 1) // self.size
            if self.arr[parent_index] < self.arr[index]:
                self.arr[parent_index], self.arr[index] = self.arr[index], self.arr[parent_index]
            index = parent_index

    def remove_max(self):
        if len(self.arr) == 0:
            return
        self.arr[0] = self.arr[len(self.arr) - 1]
        self.arr.pop(-1)
        self.heapify(0)


def main():
    print("Binary heap demo: ")
    arr2 = Heap(2)
    arr2.add(5)
    arr2.add(14)
    arr2.add(24)
    arr2.add(2)
    arr2.add(97)
    arr2.add(13)
    print(arr2.arr)
    print("Trinary heap demo: ")
    arr3 = Heap(3)
    arr3.add(5)
    arr3.add(14)
    arr3.add(24)
    arr3.add(2)
    arr3.add(97)
    arr3.add(13)
    print(arr3.arr)
    print("Tetrary heap demo: ")
    arr4 = Heap(4)
    arr4.add(5)
    arr4.add(14)
    arr4.add(24)
    arr4.add(2)
    arr4.add(97)
    arr4.add(13)
    print(arr4.arr)
    print("Tetrary heap root removal demo: ")
    heap = Heap(4)
    heap.add(5)
    heap.add(14)
    heap.add(24)
    heap.add(2)
    heap.add(97)
    heap.add(13)
    heap.add(6)
    heap.add(4)
    heap.add(36)
    print(heap.arr)
    heap.remove_max()
    print(heap.arr)


if __name__ == "__main__":
    main()
