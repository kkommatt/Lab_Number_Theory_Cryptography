import random
from legandre_jacobi import jacobi_symbol
from long_number import LongNumber

zero = LongNumber('0')
one = LongNumber('1')
two = LongNumber('2')
three = LongNumber('3')
six = LongNumber('6')
eight = LongNumber('8')
nine = LongNumber('9')
minus_one = LongNumber('-1')
N = LongNumber('10')


def solovei_strassen(a):
    i = N
    while i > zero:
        k = LongNumber(random.randrange(int(a.__str__())))
        print("Random number: ", k.__str__())
        if LongNumber.GCD(a, k) > one:
            print("GCD isn't one")
            return False
        jacobi = jacobi_symbol(str(k), str(a))

        while jacobi < zero:
            jacobi += a

        if LongNumber.pow_mod(k, (a - one) // two, a) != jacobi % a:
            print("Mod comparison failed:", LongNumber.pow_mod(k, (a - one) // two, a), jacobi % a)
            return False
        i -= one
    return True


def solovei():
    print("Solovay-Strassen Algorithm")

    try:
        print("\nCalculation:")
        inp2 = input("Input: ")
        inp2 = [LongNumber(c) for c in inp2.split(" ")]
        str_inp2 = inp2
        result2 = solovei_strassen(*inp2)

        print(f"Input: {str_inp2}")
        print(f"Result: {result2}")

    except Exception as x:
        print(f"{x}")
