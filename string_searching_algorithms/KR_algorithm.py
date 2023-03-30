SLO = {' ': 0, 'd': 1, 'k': 2, 'c': 3, 'z': 4, 'm': 5, 'i': 6, 'a': 7, 'w': 8, 'e': 9, 'u': 10, 's': 11, 'l': 12, 't': 13, 'y': 14, 'j': 15, 'p': 16, 'n': 17, 'o': 18, '5': 19, 'b': 20, '2': 21, '4': 22, '8': 23, '7': 24, '-': 25, '3': 26, '9': 27, 'r': 28, 'g': 29, 'ę': 30, 'ó': 31, 'ż': 32, '—': 33, 'ź': 34, 'ą': 35, 'ł': 36, ',': 37, 'ś': 38, ':': 39, '!': 40, 'ć': 41, '.': 42, 'h': 43, '(': 44, ';': 45, 'f': 46, 'ń': 47, ')': 48, 'é': 49, '?': 50, '…': 51, '«': 52, '»': 53, 'v': 54, 'x': 55, '*': 56, 'à': 57, '/': 58, 'q': 59, '1': 60, 'æ': 61, '–': 62, '0': 63, '6': 64}


def KR_search(string, text):
    q = 113 # random prime number
    m = len(string)
    n = len(text)
    d = 65  # 32 + .,:;()!?*
    p = 0
    t = 0
    h = 1
    ret = []

    if n == 0 or m == 0 or m > n:
        return None

    for i in range(m-1):
        h = (h*d) % q

    for i in range(m):
        p = (d * p + SLO[string[i]]) % q
        t = (d * t + SLO[text[i]]) % q

    for j in range(n - m + 1):
        if p == t:
            if string == text[j:j+m]:
                ret.append(j)

        if j < n - m:
            t = (d*(t-SLO[text[j]]*h) + SLO[text[j + m]]) % q
            if t < 0:
                t += q
    return ret


def find(string, text):
    indexes = []
    indexes = KR_search(string, text)
    return indexes


def main():
    # TEST1
    test_text = ""
    to_find = ""
    print(find(to_find, test_text))
    # TEST2
    test_text = "aba"
    to_find = "aba"
    print(find(to_find, test_text))
    # TEST3
    test_text = "abbaababaabb"
    to_find = "aa"
    print(find(to_find, test_text))
    # TEST4
    test_text = "abababababa"
    to_find = "abbbababababababab"
    print(find(to_find, test_text))
    #TEST5
    test_text = "abababababa"
    to_find = "aaa"
    print(KR_search(to_find, test_text))

if __name__ == "__main__":
    main()
