from math import sqrt
#Headers
ntd_header = '-----Naive Trial Division-----\n'
trial_division_header = '-----Improved Trial Division-----\n'
wilson_theorem_header = '-----Wilson\'s Theorem-----\n'


def naive_trial_div(n): #this test checks every number between 2 and n; this is woefully ineffectient
    if (n < 2):
        return False
    for i in range(2, n):
        print('{} mod {} = {}'.format(n, i, (n % i)))
        if (n % i == 0):
            return False
    return True

 #this is an improved, but still inefficient test.
 #if (n = p * q), at least one of p or q is less than sqrt(n), otherwise (p * q) > (sqrt(n) * sqrt(n)) = n, therefore (p * q) != n
def trial_division(n):
    if (n < 2):
        return False
    for i in range(2, int(sqrt(n)) + 1):
        print('{} mod {} = {}'.format(n, i, (n % i)))
        if (n % i == 0):
            return False
    return True

#Wilson's theorem uses factorials and modular arihmetic, terrible efficiency, 1 out of 10, would not recommend
#if ((n-1)! mod n) == n - 1, n is prime
def wilson_theorem(n):
    factorial = 1
    for i in range(1, n): #for-loop factorial
        factorial = (factorial * i) % n
    print('{0}! mod {1} == ({1} - 1): {2}'.format(factorial, n, (factorial == n - 1)))
    return (factorial == n - 1) #True if n is prime

def main():
    print('Enter the number to determine primality: ')
    n = int(input())

    #naive trial division
    print(ntd_header)
    if (naive_trial_div(n) is True):
        print('\n[+] n is prime\n')
    else:
        print('\n[-] n is composite\n')
    print(ntd_header)

    #improved trial division
    print(trial_division_header)
    if (trial_division(n) is True):
        print('\n[+] n is prime\n')
    else:
        print('\n[-] n is composite\n')
    print(trial_division_header)

    #Wilson's Theorem applied for primality test
    print(wilson_theorem_header)
    if (wilson_theorem(n) is True):
        print('\n[+] n is prime\n')
    else:
        print('\n[-] n is composite\n')
    print(wilson_theorem_header)

    #TODO Fermat, Miller-Rabin, AKS primality tests
if __name__ == '__main__':
    main()