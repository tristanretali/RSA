'''Simple class Person
    A private and a public key is associated to a person

    ----------------------------------------------------------------
    getter methods
        - getPrivateKey()
        - getPublicKey()

    setter methods
        - setPrivateKey()
        - setPublicKey()
'''
class Person:
    def __init__(self, name, private_key, public_key):
        self.name = name
        self.private_key = private_key
        self.public_key = public_key
        
    def getPrivateKey(self):
        '''Get the private key associated'''
        return self.private_key

    def setPrivateKey(self, newPrivateKey):
        '''Set the private key associated'''
        self.private_key = newPrivateKey

    def getPublicKey(self):
        '''Get the public key associated'''
        return self.public_key
        
    def setPublicKey(self, newPublicKey):
        '''Set the public key associated'''
        self.public_key = newPublicKey