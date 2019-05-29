def approach1(givenNumber):
    # Initialize a list
    primes = []
    for possiblePrime in range(2, givenNumber + 1):
        # Assume number is prime until shown it is not. 
        isPrime = True
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                isPrime = False
        if isPrime:
            primes.append(possiblePrime)
    return(primes)
    

def approach2(givenNumber):
    # Initialize a list
    primes = []
    for possiblePrime in range(2, givenNumber + 1):
        # Assume number is prime until shown it is not. 
        isPrime = True
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    
    return(primes)
   
def approach3(givenNumber):  
    
    # Initialize a list
    primes = []
    for possiblePrime in range(2, givenNumber + 1):
        # Assume number is prime until shown it is not. 
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    
    return(primes)





def countPrimes(n):
    if n <= 2: 
        return 0
    res = [True] * n
    res[0] = res[1] = False
    for i in range(2, n):
        if res[i] == True:
            for j in range(2, (n-1)//i + 1):
                res[i*j] = False
    return sum(res)

#num = countPrimes(10)
#print(num)



import timeit
# Approach 1: Execution time 
#print(timeit.timeit('approach1(500)', globals=globals(), number=10000))
# Approach 2: Execution time
print(timeit.timeit('approach2(500)', globals=globals(), number=10000))
# Approach 3: Execution time
print(timeit.timeit('approach3(500)', globals=globals(), number=10000))
# Approach 4:
print(timeit.timeit('countPrimes(500)', globals=globals(), number=10000))