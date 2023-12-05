import re
from long_number import LongNumber


def extended_gcd(a, b):
    if a == LongNumber(0):
        return (b, LongNumber(0), LongNumber(1))
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)


def chinese_remainder_theorem(equations):
    x = LongNumber("0")
    prod = LongNumber("1")

    for _, ni in equations:
        prod = prod * ni

    for ai, ni in equations:
        p = prod // ni
        gcd, mi, _ = extended_gcd(p, ni)
        if gcd != LongNumber(1):
            raise Exception("Moduli are not coprime")
        x = x + ai * mi * p

    return x % prod


def chinese_theorem():
    try:
        print("Chinese Remainder Theorem")

        inp3 = input("Write pairs: (remainder_1, mod_1), (remainder_2, mod_2): ")
        str_inp3 = inp3

        pattern = r"\((\d+), (\d+)\)"

        matches = re.findall(pattern, str_inp3)
        equations = [(LongNumber(a), LongNumber(b)) for a, b in matches]
        print("Equations:", equations)

        if inp3 is not None:
            result3 = chinese_remainder_theorem(equations)
            print(f"Input: {equations}")
            print(f"Result: {result3}")

    except Exception as x:
        print(f"{x}")
