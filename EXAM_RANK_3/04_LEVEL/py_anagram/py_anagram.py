def anagram(s1: str, s2: str) -> bool:
    fst = s1.replace(' ', '').lower()
    snd = s2.replace(' ', '').lower()
    return sorted(fst) == sorted(snd)
