'''
Utils functions for generating RSA public and private keys
'''
import random

def pgcd(u, v):
    '''
    Finds the greatest common divisor
    u : integer
    v : integer

    returns the greatest common divisor
    '''
    t = 0.0
    while(v):
        t = u
        u = v
        v = t%u     
    if(u < 0):
        return -u
    else:
        return u  


def puissance (a, e, n):
    '''
    a : long --> a as intger
    e : long --> n-1
    n : long --> random integer generated between 0 ans 2^15

    Returns a^e mod n

    '''
    
    assert a < n
    p = 1
    while e > 0:        
        if (e%2 != 0):
            p=(p*a)%n
        a=(a*a)%n
        e=e//2
    return p

def test_prime_number(n):
    '''
    Tests if n is a prime number
    n : int

    Returns a boolean
    '''
    if((puissance(2,n-1,n)==1) and
       (puissance(3,n-1,n)==1) and
       (puissance(5,n-1,n)==1) and
       (puissance(7,n-1,n)==1) and
       (puissance(11,n-1,n)==1) and
       (puissance(13,n-1,n)==1)):
       return True
    else:
        return False

def generate_prime_number(min, max):
    '''
    Generates a prime number
    min : int -> 2^min
    max : int -> 2^max
    
    Returns a prime number as integer
    '''
    primeNumber = random.randint(pow(2,min), pow(2,max)-1)
    while (not test_prime_number(primeNumber)):
        primeNumber = random.randint(pow(2,min), pow(2,max)-1)
    return primeNumber  



def bezout(a, b):

    p = 1
    q = 0
    r = 0
    s = 1

    while (b != 0):
        c = a % b
        quotient = a//b
        a = b
        b = c
        nouveau_r = p - quotient * r 
        nouveau_s = q - quotient * s
        p = r 
        q = s
        r = nouveau_r
        s = nouveau_s
    return p
