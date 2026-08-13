def anagram(s1: str, s2: str) -> bool:
    first = s1.replace(' ', '').lower()
    second = s2.replace(' ', '').lower()
    return sorted(first) == sorted(second)
