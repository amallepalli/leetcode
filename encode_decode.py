
from typing import List


def encode(strs: List[str]) -> str:
    encode = ""
    for s in strs:
        encode += str(len(s)) + "," + s
    return encode
def decode(s: str) -> List[str]:
    decode = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != ",":
            j += 1
        length = int(s[i: j])
        decode.append(s[j + 1: j + 1 + length])
        i = j + 1 + length
    return decode


strs = ["we","say",":","yes","!@#$%^&*()"]
print(encode(strs))
print(decode(encode(strs)))