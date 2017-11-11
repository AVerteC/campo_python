# implementing sieve of eratosthenes
         sieve = [0,1]
         for i in range(2, val):
             sieve.append(True)

         for i in range(2, round(math.sqrt(val))):
             if sieve[i] is True:
                 for j = i**2, i**2+