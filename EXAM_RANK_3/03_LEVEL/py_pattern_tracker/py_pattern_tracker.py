def pattern_tracker(text: str) -> int:
    count = 0

    for index in range(len(text) - 1):
        first = text[index]
        second = text[index + 1]

        if first.isdigit() and second.isdigit():
            if int(second) == int(first) + 1:
                count += 1

    return count
