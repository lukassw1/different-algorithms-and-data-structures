def naive_algorithm(template, text):
    indexes = []
    text_length = len(text)
    template_length = len(template)

    if text_length == 0 or template_length == 0 or template_length > text_length:
        return

    for i in range(0, text_length - template_length + 1):
        if template == text[i : i + template_length]:
            indexes.append(i)
    return indexes


def main():
    # TEST1
    test_text = ""
    to_find = ""
    print(naive_algorithm(to_find, test_text))
    # TEST2
    test_text = "aba"
    to_find = "aba"
    print(naive_algorithm(to_find, test_text))
    # TEST3
    test_text = "abbaababaabb"
    to_find = "aa"
    print(naive_algorithm(to_find, test_text))
    # TEST4
    test_text = "abababababa"
    to_find = "abbbababababababab"
    print(naive_algorithm(to_find, test_text))
    #TEST5
    test_text = "abababababa"
    to_find = "aaa"
    print(naive_algorithm(to_find, test_text))

if __name__ == "__main__":
    main()