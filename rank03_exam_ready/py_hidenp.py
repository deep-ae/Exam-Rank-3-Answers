def hidenp(small: str, big: str) -> bool:
    index = 0

    for char in big:
        if index < len(small) and char == small[index]:
            index += 1

    return index == len(small)
