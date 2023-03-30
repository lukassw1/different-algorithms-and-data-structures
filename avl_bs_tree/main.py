import time
import gc
from random import sample
from matplotlib import pyplot as plt

from tree_avl import Node, AvlTree
from tree_bst import BstNode, search_bst, print_tree_bst, insert_bst, delete_node_bst


random_numbers = sample(range(30001), 10000)
number_amount = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]


def create_bst_tree(word_count):
    root = BstNode(random_numbers[0])
    for num in random_numbers[1:word_count]:
        insert_bst(root, num)
    return root


def create_avl_tree(word_count):
    root = AvlTree()
    for num in random_numbers[:word_count]:
        root.add(num)
    return root


def search_bst_tree(tree, word_count):
    for num in random_numbers[:word_count]:
        search_bst(tree, num)


def delete_bst_tree(tree, word_count):
    for num in random_numbers[:word_count]:
        delete_node_bst(tree, num)


def calculate_time_create(function):
    times = []
    for amount in number_amount:
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        function(amount)
        stop = time.process_time()
        singular_time = stop - start
        times.append(singular_time)
        if gc_old: gc.enable()
    return times


def calculate_time_search_delete(function):
    times = []
    for amount in number_amount:
        tree = create_bst_tree(amount)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        function(tree, amount)
        stop = time.process_time()
        singular_time = stop - start
        times.append(singular_time)
        if gc_old: gc.enable()
    return times


def calculate_time_search_avl():
    times = []
    for amount in number_amount:
        tree = AvlTree(values=random_numbers[:amount])
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for number in random_numbers[:amount]:
            tree.find(number)
        stop = time.process_time()
        singular_time = stop - start
        times.append(singular_time)
        if gc_old: gc.enable()
    return times


def calculate_time_delete_avl():
    times = []
    for amount in number_amount:
        values=random_numbers[:10000]
        tree = AvlTree(values=values)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for number in values:
            tree.remove_node(number)
        stop = time.process_time()
        singular_time = stop - start
        times.append(singular_time)
        if gc_old: gc.enable()
    return times


def save_times(func_type, times):
    with open("result.txt", "a") as result:
        result.write(f"{func_type}: \n")
        for i in range(len(times)):
            result.write(f"{number_amount[i]} : {times[i]}\n")


def plot(title, time_values_bst, time_values_avl, filename):
    plt.plot()
    plt.title(title)
    plt.plot(number_amount, time_values_bst, label="bst")
    plt.plot(number_amount, time_values_avl, label="avl")
    plt.xlabel("number amount")
    plt.ylabel("time")
    plt.legend()
    plt.savefig(filename)
    plt.show()


def main():
    save_times("\nNew Attempt", [])
    create_bst_times = calculate_time_create(create_bst_tree)
    create_avl_times = calculate_time_create(create_avl_tree)
    save_times("Create BST", create_bst_times)
    save_times("Create AVL", create_avl_times)
    plot("Create tree times", create_bst_times, create_avl_times, "plot-create.png")
    search_bst_times = calculate_time_search_delete(search_bst_tree)
    search_avl_times = calculate_time_search_avl()
    save_times("Search BST", search_bst_times)
    save_times("Search AVL", search_avl_times)
    plot("Search tree times", search_bst_times, search_avl_times, "plot-search.png")
    delete_bst_times = calculate_time_search_delete(delete_bst_tree)
    delete_avl_times = calculate_time_create(create_avl_tree)
    save_times("Delete BST", delete_bst_times)
    save_times("Delete AVL", delete_avl_times)
    plot("Delete tree times", delete_bst_times, delete_avl_times, "plot-delete.png")


if __name__ == "__main__":
    main()
