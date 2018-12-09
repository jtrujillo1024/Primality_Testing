from math import sqrt
import random
#Headers
ntd_header = '-----Naive Trial Division-----\n'
trial_division_header = '-----Improved Trial Division-----\n'
wilson_theorem_header = '-----Wilson\'s Theorem-----\n'
fermat_header = '-----Fermat Test (Probablistic)-----\n'
miller_rabin_header = '-----Miller Rabin Test (Probabilistic)-----\n'
#Constant
k = 5 #number of trials in probabilistic prime tests

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

#Fermat Test is a probabilistic test, as a false positive result is plausible
#k is the number of randomly selected 'a' values to test
def fermat(n, k):
    for i in range(k):
        a = random.randrange(2, n)
        print('a = {}'.format(a))
        print('({0} ^ ({1}-1)) mod {1} = {2}\n'.format(a, n, pow(a, n - 1, n)))
        if (pow(a, n - 1, n) != 1):
            return False
    else: 
        return True #probably prime

#Miller-Rabin Test
def miller_rabin(n, k):
    if (n < 2):
        return False
    if (n < 4):
        return True
    if (n % 2 == 0):
        return False
    # n > 3, and is odd
    s = 0
    d = n - 1
    while(d % 2 ==0):
        s += 1
        d //= 2
    #n = (2 ^ s) * d where d is odd

    for i in range (k):
        a = random.randrange(2, n - 1) # 2 <= a <= n - 2
        x = (a ** d) % n
        if x == 1:
            continue
        for j in range(s):
            if x == n - 1:
                break
            x = (x * x) % n
        else:
            return False
    return True

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

    #Fermat Probabilistic Test
    print(fermat_header)
    if (fermat(n, k) is True):
        print('\n[+] n is probably prime\n')
    else:
        print('\n[-] n is composite\n')
    print(fermat_header)

    #Miller-Rabin Probabilistic Test
    print(miller_rabin_header)
    if (miller_rabin(n, k) is True):
        print('\n[+] n is probably prime\n')
    else:
        print('\n[-] n is composite\n')
    print(miller_rabin_header)

    #TODO AKS primality test, print Miller-Rabin steps
if __name__ == '__main__':
    main()
