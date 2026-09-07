def cryptic_sorter(strings: list[str]) -> list[str]:
    result = strings[:]
    vowels = "aeiou"

    def key(word: str):
        vowel_count = sum(1 for c in word.lower() if c in vowels)
        return (len(word), word.lower(), vowel_count)

    for i in range(len(result)):
        for j in range(len(result) - 1 - i):
            if key(result[j]) > key(result[j + 1]):
                result[j], result[j + 1] = result[j + 1], result[j]

    return result


print(cryptic_sorter(["aaa"','"bbb"','"AAA"','"BBB"]))
