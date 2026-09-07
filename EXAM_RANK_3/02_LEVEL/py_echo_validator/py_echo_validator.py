def echo_validator(text: str) -> bool:
    cleaned = ""

    for char in text:
        if char.isalpha():
            cleaned += char.lower()

    if cleaned == "":
        return False

    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print(echo_validator("aaaa"))
