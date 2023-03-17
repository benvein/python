from typing import *

def countSameLetters(text1: str, text2: str) -> int:
    sameLetter: int = None
    intersection: str = ""
    for i in text1:
        if (text2.find(i)>0 and intersection.find(i) == 0):
            intersection = intersection + i
    sameLetter = len(intersection)

    return sameLetter