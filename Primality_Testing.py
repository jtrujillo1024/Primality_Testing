from math import sqrt
import random
import time

def trial_division(n): #this test checks every number between 2 and n; this is woefully ineffectient
    if (n < 2):
        return False
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

 #this is an improved, but still inefficient test.
 #if (n = p * q), at least one of p or q is less than sqrt(n), otherwise (p * q) > (sqrt(n) * sqrt(n)) = n, therefore (p * q) != n
def improved_trial_div(n):
    if (n < 2):
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True

#Wilson's theorem uses factorials and modular arihmetic, terrible efficiency, 1 out of 10, would not recommend
#if ((n-1)! mod n) == n - 1, n is prime
def wilson_theorem(n):
    factorial = 1
    for i in range(1, n): #for-loop factorial
        factorial = (factorial * i) % n
    return (factorial == n - 1) #True if n is prime

#Fermat Test is a probabilistic test, as a false positive result is plausible
#k is the number of randomly selected 'a' values to test
def fermat(n, k):
    for i in range(k):
        a = random.randrange(2, n)
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
    while True:
        print('---------------Primality Test---------------')
        print('Enter Desired Method:\n(Methods are listed in descending order of efficiency)\n')
        print('--------------------')
        print('Miller-Rabin (Probablistic),\nFermat (Probablistic),\nImproved Trial Division (Deterministic),\nWilson\'s\nTheorem (Deterministic),\nTrial Division (Deterministic)')
        print('--------------------\n')
        mode = input().upper()
        #Warning for probablistic tests
        if (mode.startswith('M') or mode.startswith('F')):
            print('[!] Warning! This test is probablistic, and may return false positives. Proceed? y/n')
            confirmation = input().upper()
            if 'Y' not in confirmation:
                print('Cancelling selection.\n')
                continue

        #Miller-Rabin
        if mode.startswith('M'):
            mode = 'Miller-Rabin' #Corrects possible user input spelling errors (used later)
            print('\nEnter the number to test for primality:')
            n = int(input())
            print('Enter the number of trials to be executed on n (more trials reduces odds of false positive, but does not guarantee perfect accuracy).')
            k = int(input())
            start_time = time.time()
            result = miller_rabin(n, k)
            end_time = time.time()
        
        #Fermat
        elif mode.startswith('F'):
            mode = 'Fermat'
            print('\nEnter the number to test for primality:')
            n = int(input())
            print('Enter the number of trials to be executed on n (more trials reduces odds of false positive, but does not guarantee perfect accuracy).')
            k = int(input())
            start_time = time.time()
            result = fermat(n, k)
            end_time = time.time()
        
        #Improved Trial Division
        elif mode.startswith('I'):
            mode = 'Improved Trial Division'
            print('\nEnter the number to test for primality:\n')
            n = int(input())
            start_time = time.time()
            result = improved_trial_div(n)
            end_time = time.time()
        
        #Wilson's Theorem
        elif mode.startswith('W'):
            mode = 'Wilson\'s Theorem'
            print('\nEnter the number to test for primality:')
            n = int(input())
            start_time = time.time()
            result = wilson_theorem(n)
            end_time = time.time()
        
        #Trial Division
        elif mode.startswith('T'):
            mode = 'Trial Division'
            print('\nEnter the number to test for primality:')
            n = int(input())
            start_time = time.time()
            result = trial_division(n)
            end_time = time.time()
        
        else:
            print('[!] Invalid input')
            continue
        
        #Final outputs for user
        duration = round(end_time - start_time, 2) #time taken by actual function, two decimal places
        if result is True:
            print('\n[+] n is prime')
        else:
            print('\n[-] n is composite')
        print('Method used: {}\nApproximate time used: {} seconds\n'.format(mode, duration))

        #optional further tests
        print('Primality test complete, check another number? y/n')
        repeat_option = input().upper()
        if 'Y' not in repeat_option:
            break

    #TODO AKS primality test, print Miller-Rabin steps
if __name__ == '__main__':
    main()
