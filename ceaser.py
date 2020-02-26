import random
alphabet = "'abcdefghijklmnopqrstuvwxyz.,!'"

def makeKey(alphabet):
   alphabet= list(alphabet)
   key= random.shuffle(alphabet)
   alphabet= str(alphabet)
   return key


def encrypt(plaintext, key, alphabet):
    """Encrypt the string and return the ciphertext"""
    return ''.join(key[l] for l in plaintext)
print (alphabet)