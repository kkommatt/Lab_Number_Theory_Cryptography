import copy

from long_number import LongNumber
from RhoPollard import pollard_rho

zero = LongNumber('0')
one = LongNumber('1')
two = LongNumber('2')
three = LongNumber('3')
six = LongNumber('6')
eight = LongNumber('8')
nine = LongNumber('9')
minus_one = LongNumber('-1')


def legendre_symbol(A, P):
    A = LongNumber(A)
    P = LongNumber(P)
    a = copy.deepcopy(A)
    p = copy.deepcopy(P)
    factors = []
    if a == one:
        return a
    if a == minus_one:
        return minus_one ** ((p - one) // two)
    if a < zero:
        factors.append(LongNumber('-1'))
        a = a * LongNumber('-1')
    a %= p
    factors += pollard_rho(a)
    factor_powers = {}
    for factor in factors:
        if factor_powers.get(factor):
            factor_powers[factor] += one
        else:
            factor_powers[factor] = LongNumber('1')

    odd_factor_powers = {}
    for key, value in factor_powers.items():
        if value % two != zero:
            odd_factor_powers[key] = value

    result = LongNumber('1')
    two_factor_amount = odd_factor_powers.get(two)
    if two_factor_amount:
        power_result = minus_one ** ((p ** two - one) // eight)
        i = LongNumber('0')
        while i < two_factor_amount:
            result *= power_result
            i += one
        odd_factor_powers.pop(two)

    for key, value in odd_factor_powers.items():
        assert value % two == one
        i = LongNumber('0')
        power_result = minus_one ** (((key - one) // two) * ((p - one) // two))
        legendre = legendre_symbol(str(p), str(key))
        while i < value:
            i += one
            result *= power_result * legendre

    return result


def jacobi_symbol(a, m):
    a = LongNumber(a)
    m = LongNumber(m)
    factors = pollard_rho(m)
    result = LongNumber('1')
    if not factors:
        factors = [m]

    for factor in factors:
        legendre = legendre_symbol(str(a), str(factor))
        result *= legendre

    return result


def legandre_jacobi():
    print("Calculation of Legendre and Jacobi symbols")

    try:
        print("\nCalculation of Legendre symbols:")
        inp2 = input("Input (numbers separated by space): ")
        str_inp2 = inp2
        inp2 = inp2.split(" ")
        result2 = legendre_symbol(*inp2)
        print(f"Input: {str_inp2}")
        print(f"Result: {result2}")

    except Exception as x:
        print(f"{x}")

    try:
        print("\nCalculation of Jacobi symbols:")
        inp3 = input("Input (numbers separated by space): ")
        str_inp3 = inp3
        inp3 = inp3.split(" ")
        result3 = jacobi_symbol(*inp3)
        print(f"Input: {str_inp3}")
        print(f"Result: {result3}")

    except Exception as x:
        print(f"{x}")
