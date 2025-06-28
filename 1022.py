from sys import stdin

def mdc(a: int, b: int) -> int:
    while True:
        r = a % b
        if not r:
            return b
        a, b = b, r

