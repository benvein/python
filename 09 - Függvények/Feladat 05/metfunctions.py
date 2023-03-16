from typing import *

def countSameLetters(text1: str, text2: str) -> int:
    sameLetter: int = None
    for letter in text1:
        for letter in text2:
            sameLetter = text1.count(letter)

    return sameLetter