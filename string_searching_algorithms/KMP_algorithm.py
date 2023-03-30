def kmp_prefix(template, template_length):
    prefix_func = [0]
    x = 0
    for i in range(2, template_length + 1):
        while x > 0 and template[x] != template[i-1]:
            x = prefix_func[x-1]
        if template[x] == template[i-1]:
            x += 1
        prefix_func.append(x)
    return prefix_func

def kmp_algorithm(template, text):
    indexes = []
    text_len = len(text)
    template_len = len(template)
    if text_len == 0 or template_len == 0 or template_len > text_len:
        return

    prefix_function = kmp_prefix(template, template_len)
    x = 0 # liczba pasujących symboli

    for i in range(1, text_len + 1):
        while x > 0 and template[x] != text[i - 1]:
            x = prefix_function[x - 1]
        if template[x] == text[i-1]:
            x += 1
        if x == template_len:
            indexes.append(i - template_len)
            x = prefix_function[x-1]
    return indexes

def main():
    # TEST1
    test_text = ""
    to_find = ""
    print(kmp_algorithm(to_find, test_text))
    # TEST2
    test_text = "aba"
    to_find = "aba"
    print(kmp_algorithm(to_find, test_text))
    # TEST3
    test_text = "abbaababaabb"
    to_find = "aa"
    print(kmp_algorithm(to_find, test_text))
    # TEST4
    test_text = "abababababa"
    to_find = "abbbababababababab"
    print(kmp_algorithm(to_find, test_text))
    #TEST5
    test_text = "abababababa"
    to_find = "aaa"
    print(kmp_algorithm(to_find, test_text))

if __name__ == "__main__":
    main()