def print_upper_words(words, start_with):
    for word in words:
        for letter in start_with:
            if words.startswith('e') or word.startswith('E'):
             print(word.upper())