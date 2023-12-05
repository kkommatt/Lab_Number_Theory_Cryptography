from long_number import LongNumber
from RhoPollard import pollard_rho

zero = LongNumber('0')
one = LongNumber('1')


def euler_phi_function(n):
    n = LongNumber(n)
    factors = pollard_rho(n)
    factor_powers = {}
    for factor in factors:
        factor_power = factor_powers.get(factor, LongNumber('0'))
        factor_powers.update({factor: factor_power + one})

    result = LongNumber('1')
    for factor, power in factor_powers.items():
        result *= (factor ** (power - one)) * (factor - one)
    return result


def mobius_mu_function(n):
    n = LongNumber(n)
    factors = pollard_rho(n)
    factor_powers = {}
    for factor in factors:
        factor_power = factor_powers.get(factor, 0)
        if factor_power > 0:
            return LongNumber(0)
        factor_powers.update({factor: factor_power + 1})
    return LongNumber(-1) ** LongNumber(len(factors))


def euler_mobius():
    try:
        print("Mobius function: \n")
        inp1 = input("Input1: ")
        if inp1 is not None:
            result = mobius_mu_function(inp1)
            print(f"Input: {inp1}")
            print(f"Result: {result}")

    except Exception as x:
        print(x)

    try:
        print("Euler function: \n")
        inp2 = input("Input2: ")
        if inp2 is not None:
            result2 = euler_phi_function(inp2)
            print(f"Input: {inp2}")
            print(f"Result: {result2}")

    except Exception as x:
        print(x)

    try:
        print("GCD N numbers:")
        inp3 = input("Write a numbers separated by space: ")
        str_inp3 = inp3
        if inp3 is not None:
            result3 = LongNumber.GCD_n(inp3)
            print(f"Input: {str_inp3}")
            print(f"Result: {result3}")

    except Exception as x:
        print(x)
