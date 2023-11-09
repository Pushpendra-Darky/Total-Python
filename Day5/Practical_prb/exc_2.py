def remove_duplicates(word):
    unique_letters = []
    seen_letters = set()

    for letter in word:
        if letter not in seen_letters:
            unique_letters.append(letter)
            seen_letters.add(letter)
    unique_letters.sort()
    return unique_letters


word = "entertaining"
result = remove_duplicates(word)
print(result)
