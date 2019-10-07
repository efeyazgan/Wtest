import math
from math import log

# Adapted from https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
def prime_sieve(n):
    list_of_primes = []
    sieve = [1] * (n//2) #create a list with all elements set to 1 (i.e. true) with number of elements = prime_list_size/2
    for i in range(3,int(n**0.5),2): # loop starting from 3 to sqrt(prime_list_size)+1 in steps of 2 
                                     # --> Since none of the even numbers are primes, the range starts 
                                     # from 3 and goes in steps of 2. It goes up to sqrt(n) because from number theory we 
                                     # know that a composite number must have a (prime) factor less than or equal to its square root.
        if sieve[i//2]: #if the int(i/2)th element is true in the list do the following
            sieve[(i*i)//2::i] = [0] * ((n-1-(i*i))//(2*i)+1) # Following the sieve algo,
                                                              # set [(i^2)/2]th element, [(i^2/2)]+ith, [(i^2/2)]+(i+i)th, etc element
                                                              # in the sieve list to 0 (i.e. false) 
                                                              # (total number of zeros is (n-(i*i)-1)//(2*i)+1) 
                                                              # e.g. when i = 3, it will set 4th and 7th element to 0, etc. 
    for i in range(1,n//2):
        if sieve[i]:
            list_of_primes.append(2*i+1) #construct the list of primes using the elements that have 1 (i.e. true) in sieve 
    list_of_primes = [2] + list_of_primes #list of primes up to list_size/2
    return list_of_primes

def prime_list_size(n):
    if n > 3:
        list_size = n*(log(n)+log(log(n-1))+(log(log(n-2))/(log(n))-(log(log(n))**2-6*log(log(n+11)))/(2*(log(n))))) 
    if n <= 3:
        list_size = 6    
    list_size = int(list_size)
    return list_size       

m = int(input('nth prime number? '))
k = prime_list_size(m)
print("approximate prime counting function for ",m," is ",k)
prime = [0]+prime_sieve(k) #access the mth element of the prime numbers list (0 is added to the list so that the index of the list start from 0)
print("Prime number", m, "is", prime[m])
