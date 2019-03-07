
def is_palindrome(n):
    s = str(n)

    i = 0
    j = len(s) - 1

    while i<j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    else:
        return True


output = filter(is_palindrome,range(1900,2140))

print('1-1000:', list(output))


