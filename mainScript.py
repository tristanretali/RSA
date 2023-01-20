import perso
import generate_keys as gK
import hashlib
import utils

def generate_public_key(parameters):
  '''Returns a tuple containing e and n parameters
    parameters -> (n,e,d)
  '''
  return (parameters[1], parameters[0]) 

def generate_private_key(parameters):
  '''Returns a tuple containing e and d parameters
    parameters -> (n,e,d)
  '''
  return (parameters[2], parameters[0]) 

def hashMessages(message):
  '''
  Hash a message with MD5 python hash function
  message : int

  Returns an integer
  '''
  hash = hashlib.md5(str(message).encode("utf-8"))
  hash = int.from_bytes(hash.digest(), "big")
  return hash

def verificationTransfertCle(message, hashMessage):
  ''' Verify the corredpondance between the key and the print statement of a message
    message -> the uncrypted message
    hashMessage -> the uncrypted hash of the message
  
    Returns a boolean
  '''
  hash = hashMessages(message)
  return hash == hashMessage 

def crypteMessage(message2crypte, key):
  '''
  Use the puissace function to crypte a message
  message2crypte : int -> the message to crypte
  key : tuple -> the key used to crypte the message

  Returns an Integer
  '''
  return utils.puissance(message2crypte, key[0], key[1])

def unCrypteMessage(message2Uncrypte, key):
  '''
  Use the puissace function to uncrypte a message
  message2Uncrypte : int -> the message to uncrypte
  key : tuple -> the key used to uncrypte the message
  
  Returns an Integer
  '''
  return utils.puissance(message2Uncrypte, key[0], key[1])

def runPrompt():

  parameters = gK.calculate_parameters("")
  parametersCA = gK.calculate_parameters("CA")

  Ca = perso.Person("CA", generate_private_key(parametersCA), generate_public_key(parametersCA))
  Alice = perso.Person("Alice", generate_private_key(parameters), generate_public_key(parameters))

  # 1st step 
  empreinte = hashMessages(Alice.getPublicKey()[0]) #e de la cle publique d'Alice
  aliceKey = str(Alice.getPublicKey()[0])  #e de la cle publique d'Alice

  print("Public key Alice : " + aliceKey)
  print("mark : " + str(empreinte))

  aliceKeyEncrypt = crypteMessage(Alice.getPublicKey()[0], Ca.getPublicKey())# message chiffré avec clé pub de la CA
  aliceKeyEncryptMark = crypteMessage(empreinte, Ca.getPublicKey()) # message chiffré avec clé pub de la CA

  print("Alice Public Key Encrypt : " + str(aliceKeyEncrypt)) 
  print("Mark of Alice Public Key : " + str(aliceKeyEncryptMark)) 
  
  # 2nd step
  aliceKeyUncrypt = unCrypteMessage(aliceKeyEncrypt, Ca.getPrivateKey())
  print("Alice Public Key Decrypt:" + str(aliceKeyUncrypt))
  aliceKeyUncryptMark = unCrypteMessage(aliceKeyEncryptMark, Ca.getPrivateKey())
  print("Alice Public Key Decrypt Mark:" + str(aliceKeyUncryptMark))

  verif = verificationTransfertCle(aliceKeyUncrypt, aliceKeyUncryptMark)

  # 3rd step
  if verif:
    genCertif = crypteMessage(Alice.getPublicKey()[0], Ca.getPrivateKey())
    print("gencertif :" + str(genCertif))
  
    print("e of Alice : " + str(Alice.getPublicKey()[0]))
    print("Decrypt of Alice e : " + str(unCrypteMessage(genCertif, Ca.getPublicKey()))) 
    print("Bob Certificate Checking : " + str(Alice.getPublicKey()[0] == unCrypteMessage(genCertif, Ca.getPublicKey())))  

if __name__ == '__main__':
  runPrompt()

