#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-08-25 14:33:10
# @Last Modified by:   john
# @Last Modified time: 2016-12-03 11:16:39
 
from Crypto.Util.number import getPrime, inverse
import binascii
 
'''
This Python code tries to illustrate how RSA is done at a basic level.
'''
 
 
# At RSA's core, there are two PRIME factors, p and q.
# With this code, I just generate two large random prime numbers.
# p and q are typically NOT given to you in an RSA challenge.
# bits_size = 256
p = 153143042272527868798412612417204434156935146874282990942386694020462861918068684561281763577034706600608387699148071015194725533394126069826857182428660427818277378724977554365910231524827258160904493774748749088477328204812171935987088715261127321911849092207070653272176072509933245978935455542420691737433
q = 156408916769576372285319235535320446340733908943564048157238512311891352879208957302116527435165097143521156600690562005797819820759620198602417583539668686152735534648541252847927334505648478214810780526425005943955838623325525300844493280040860604499838598837599791480284496210333200247148213274376422459183
 
 
# These two prime factors multiply to create n, which is "the modulus".
# n is typically GIVEN to you in an RSA challenge.
n = p * q
 
 
# The plaintext is typically referred to as m. Since we are working
# with numbers and math, we treat the string information as hex.
# Obviously this is NEVER given to you in an RSA challenge.
# m = "This is the clear text message."
# m = binascii.hexlify(m)
# m = int(m, 16)
 
 
# Another value, called e, is "the exponent".
# Both e and n make up "the public key", which is meant to be common
# knowledge. This is why typically n and e are BOTH GIVEN in an RSA challenge.
# Typcially, e is 65537, which is 0x10001 in hex
e = 65537
 
 
# The ciphertext, c, is created by this ENCRYPTION formula here.
#    c = ( m ^ e ) % n
# See how e is the exponent and n is the modulus?
# That is how the ENCRYPTION takes place.
# Typically you are given the c in an RSA challenge and it is your task
# to DECRYPT it to the m value, the plaintext.
#c = pow( m, e, n )
c = 5315135537182226856134532843338546481354659841681272223692273789930341302489189252395544040217036010025492161730920090820789264419456405499853943420863961834511620167348215712366219204972198527365477630427263725627920265227612760416678425823843187407675643742844283110052895704455415142735463486037912801307917634230788549540802477270278755052542590491708620341889689884020271200598596327430790861785538107067664504281508756159305916221674161062222221931717498244841323828452111473034440447694160917521358885718436832783214139059379459896493819067235346238816701274408935126796953373891399167497687512301978797146598
 
# Now how do we decrypt? We need "the private key"....
# We call this d in RSA. Thanks to some handy mathematical functions,
# you can find "Euler's Totient", or "the Phi function" of a number.
# This is 'the number of numbers that are less than a certain number and share
# a common denominator with that certain number'.
# I know that is hard to wrap your mind around here, but thankfully it is MUCH
# easier for a prime number. For a prime number, it is simply that number minus 1!
 
# So, if you are given n, what you need to do is find the factors of n.
# Like we've seen, this is typically p and q. So, can we find the phi function
# of n? Well, n is prime, and so are its factors, p and q, so phi should just be:
phi = ( q - 1 ) * ( p - 1 )
 
 
# Now, we can kind of unravel that modular arithmetic that was done during the
# ENCRYPTION formula. We can find the private key, d, with the MODULAR INVERSE,
# of e and phi.  
# I use a module to do this that is reworked to use Trey's function
#     https://github.com/JohnHammond/primefac_fork
d = inverse( e, phi )
print str(c)+"\n"
print str(d)+"\n"
print str(n)+"\n"
# Now, we can do a similar thing like before, but this time for DECRYPTION.
#        m = ( c ^ d ) % n
# This time we raise to our private key as an exponent, but still take the modulus.
# And we have successfully decrypted RSA!
#m = ( c ^ d ) % n
m = pow( c, d, n )
# m = (c**d)%n
print m
print repr(binascii.unhexlify(hex(m)[2:-1]))