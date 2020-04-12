import string
import math
# ##### https://en.wikipedia.org/wiki/List_of_Unicode_characters

# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    decoded = []
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)
    ndec = 0
    digits = digits[::-1]
    # if base == 2:
    for i in range(len(digits)):
        digit = int(digits[i], base=base)
        ndec += digit * base ** i
    return ndec
    # elif base == 16:
    #     x = int(str(digits), 16)
    #     print(x)
    # else:
    # reverse the digits
    # digits = digits[::-1]
    # # print(digits)
    # # variable to hold our answer
    # num = 0
    # # loop through each index
    # for x in range(len(digits)):
    #     # variable to hold each index while we work it out
    #     uni = digits[x]
    #     if uni.isdigit():
    #         # if already a number (0-9) keep it
    #         uni = int(uni)
    #         # print(uni)
    #     else:  # assumes alphabet
    #         # convert to unicode uppercase val, subtract calue of A and add 10 to get base 10 number
    #         uni = ord(uni.upper())-ord('A')+10
    #         # unicode a -> A = 65 | A(65) - A(65) + 10 = 10(a)
    #         # unicode b -> B = 66 | B(66) - A(65) + 10 = 11(b)
    #         # print(uni)
    #     num += uni*(base**x)
    #     decoded.append(num)
    # print(decoded)


print(decode('10', 2))
print(decode('fff', 16))
print(decode("1a2b", 32))


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # https://stackoverflow.com/questions/1181919/python-base-36-encoding
    base_36 = string.digits + string.ascii_uppercase
    result = []
    while number > 0:
        q = number / base
        remainder = number % base
        sep_q = str(q).split(".")
        number = int(sep_q[0])
        if 9 < remainder < base:
            remainder = base_36[remainder].lower()
        result.insert(0, str(remainder))

    return "".join(result)


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    decoded = decode(digits, base1)
    return encode(decoded, base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(
            digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
