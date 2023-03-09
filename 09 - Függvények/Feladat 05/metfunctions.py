def check(text1: str, text2: str) -> int:
    sameLetter: int = None
    for i in text1:
        for j in text2:
            sameLetter = (i==j)

    return sameLetter
