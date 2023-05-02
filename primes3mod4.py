import math
from sympy.ntheory import primefactors

#This is an implementation of the proof that there are infinitely many primes of the form 4n-1
#(or equivalently of the form 4n+3). (note that all primes except 2 are either 1 or -1 mod 4)
#By way of contradiction suppose there were only a finitely many primes congruent to -1 modulo 4, p_1,...,p_k,
#and consider N = 4 p_1 ... p_k - 1. This number does not have p_1,...,p_k as prime factors (since if p_i | N
#then p_i | 1), and also cannot have all its prime factors congruent to 1 mod 4 (since numbers that are 1 mod 4
#are closed under multiplication), and hence N has at least one new prime factor congruent to -1 modulo 4, QED.

#We begin with 4 times the product over the empty set minus 1, which is 3. Then we successively build up
#more primes of the form 4n-1:
# 4(3) - 1 = 11, prime (and necessarily -1 mod 4)
# 4(3*11) - 1 = 131, prime
# 4(3*11*131) - 1 = 17291, prime
# 4(3*11*131*17291) - 1 = 298995971
# 4(3*11*131*17291*298995971) - 1 = 89398590973228811 = 8779*10079*1010341471, whose least prime factor
#congruent to -1 mod 4 is 8779.
#This is the OEIS sequence A057205.

a = [3]
print(str(1) + "   " + str(3))

count = 2
while True:
    N = 4*math.prod(a) - 1
    #print("     factoring " + str(N))
    #print("     which has " + str(len(str(N))) + " digits...")
    for p in primefactors(N):
        if p%4 == 3:
            a += [p]
            print(str(count) + "   " + str(p))
            count += 1
            break