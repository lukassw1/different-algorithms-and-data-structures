import random
from KR_algorithm import KR_search
from KMP_algorithm import kmp_algorithm
from naive_algorithm import naive_algorithm

def test_algorithms():
    letters = "ab"
    text = ''.join(random.choice(letters) for i in range(1000))
    pattern = ''.join(random.choice(letters) for i in range(3))
    print(naive_algorithm(pattern, text) == kmp_algorithm(pattern, text) == KR_search(pattern, text))


def main():
    test_algorithms()

if __name__ == "__main__":
    main()