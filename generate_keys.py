'''
  Calculates parameters for private and public key generation
  
  ----------------------------------------------------------------

  methods used for keys generation

  - generate_public_key()
  - generate_private_key()

'''
import random
import utils

def generate_phi(p, q):
  '''Calculates phi number
    p : int as prime number
    q : int as prime number

    Returns an Integer
  '''
  assert utils.test_prime_number(p)
  assert utils.test_prime_number(q)
  return (p - 1) * (q - 1)

def generate_n(p, q):
  '''Calculates n number
    p : int as prime number
    q : int as prime number

    Returns an Integer
  '''
  assert utils.test_prime_number(p)
  assert utils.test_prime_number(q)
  return p * q

def generate_phi(p, q):
  '''Calculates phi number'''
  return (p - 1) * (q - 1)

def generate_e(phi):
  '''Calculates e number such as the greatest common divisor of e and phi equals to 1'''
  e = random.randint(2, phi-1)
  while(utils.pgcd(e, phi) != 1 and e >= phi):
    e = random.randint(2, phi-1)
  return e

def generate_d(phi, e):
  '''Calculates d number using Bezout
    phi : int 
    e : int

    Returns an Integer
  '''
  d = utils.bezout(e, phi)
  return d

def calculate_parameters(name):
  '''Calculates parameters of private and public key
    name : string

    Returns a tuple (n,e,d)
  '''
  d = -1
  e = 1
  if(name == "CA"):
    p = utils.generate_prime_number(120, 125)
    q = utils.generate_prime_number(120, 125)
    n = p * q
    phi = generate_phi(p, q)
    while(d < 0 or (e*d != ((e*d//phi)*phi)+1)):
      e = generate_e(phi)
      d = generate_d(phi, e)
  else: # the message size must be inferior to the n (message = Alice public key)
    p = utils.generate_prime_number(105, 110)
    q = utils.generate_prime_number(105, 110)
    n = p * q
    phi = generate_phi(p, q)
    while(d < 0 or (e*d != ((e*d//phi)*phi)+1)):
      e = generate_e(phi)
      d = generate_d(phi, e)
  return (n,e,d)
