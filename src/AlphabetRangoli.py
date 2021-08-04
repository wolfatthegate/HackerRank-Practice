import string


def print_rangoli(size):
    # your code goes here
    alphabets = string.ascii_lowercase
    L = []
    for i in range(size): 
        s = '-'.join(alphabets[i:size])
        L.append((s[::-1]+s[1:]).center(4*n-3, '-'))

    print('\n'.join(L[::-1]+L[1:size]))

if __name__ == '__main__':
    n = 5
    print_rangoli(n)