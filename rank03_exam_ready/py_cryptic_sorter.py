def cryptic_sorter(strings: list[str]) -> list[str]:
    vowels = 'aeiou'

    def sort_key(word: str) -> tuple[int, str, int]:
        vowel_count = sum(1 for char in word.lower() if char in vowels)
        return (len(word), word.lower(), vowel_count)

    return sorted(strings, key=sort_key)
