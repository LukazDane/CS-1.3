import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    t = text.lower()
    left = 0
    right = len(t) - 1
    while left < right:
        if not t[left].isalpha():
            left += 1
            continue
        if not t[right].isalpha():
            right -= 1
            continue
        if t[left] == t[right]:
            left += 1
            right -= 1
        else:
            return False
    return True
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    if left is None and right is None:
        # initialize left and right indices
        left = 0
        right = len(text) - 1
    if left > right:
        # Base case: left and right indices have overlapped, text must be a palindrome
        return True

    t = text.lower()

    if not t[left].isalpha():
        # left character isn't a letter; move left index to the right by one
        return is_palindrome_recursive(t, left + 1, right)

    elif not t[right].isalpha():
        # right character isn't a letter; move right index to the left by one
        return is_palindrome_recursive(t, left, right - 1)

    elif t[left] == t[right]:
        return is_palindrome_recursive(t, left + 1, right - 1)
    else:
        return False
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
