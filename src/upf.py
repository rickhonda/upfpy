import csv, math
from operator import add
from sympy import prime, primepi

#loc = 'upfpy/src/vectors.txt'
loc = 'vectors.txt'

import os.path
if os.path.exists(loc) == False:
    with open(loc, 'w') as csv_file:
        writer = (csv.writer(csv_file, delimiter=','))
        writer.writerow('2')
        writer.writerow([])
        writer.writerow('0')
        writer.writerow('1')

class UFD:
    def __init__(self):
        with open(loc) as csv_file:
            csv_reader = list(csv.reader(csv_file, delimiter=','))
            cur = 0
            for row in csv_reader:
                csv_reader[cur] = list(map(int, row))
                cur +=1
                
        self.vectors = csv_reader[1:]
        self.primes = csv_reader[0]
        
        self.generate = self.Generate
        self.generate.primes = self.primes
        self.generate.vectors = self.vectors
        
        self.show = self.Show
        self.show.vectors = self.vectors


    class Generate(object):
        def __init__(self,N):
            set_size = len(self.vectors)   

            while set_size <= N:
                self.vectors.append(self.dcomp(set_size))
                set_size +=1
#                print('while executed')
            
            with open(loc, 'w') as update_vectors:                                            # Make this replace and append rather
                writer = (csv.writer(update_vectors, delimiter=','))                                    # than rewrite the entire thing each time
                writer.writerow(self.primes)
                writer.writerows(self.vectors)
#                print('written to file')
            

        def plus(self,a,b):
            c = abs(len(a)-len(b))
            if len(a) < len(b):
                a = a + [0] * c
            else:
                b = b + [0] * c
            d = [x+y for x,y in zip(a,b)]
            return d

        def XfactN(self,x,n):               # this gives the number of factors of x in n; 
            a = n%x                         # a is n modulo x
            counter = 0
            while a == 0:                   # if a is zero, n has one or more factors of x, let's count them i = i + 1 
                counter +=1                   # count the number of iteration
                n = n/x                     # divide by x; i.e., factor it out and call it N
                a = n%x                     # a is N modulo x; if a is still zero, lets do another iteration 
            return counter                        # output is the number of iterations; i.e., the number of factors of x in n


        def dcomp(self,I):
            i = I
            L = []
            cur = 1
            while i != 1 and prime(cur) <= math.sqrt(I):          # Stops itteration if p > sqrt(2)
                exponent_of_p = self.XfactN(prime(cur),i)         
                L.append(exponent_of_p)
                if exponent_of_p != 0:
                    i = i//(prime(cur)**exponent_of_p)
                cur += 1
            if i > 1:
                if (len(self.vectors) - 1) >= i:             # i has already been factored          
                    L = self.plus(L,self.vectors[i])         # add L and i
                else:                                       # I is prime
                    self.primes.append(i)
                    L = (primepi(I)-1)*[0]            # consturct a prime vector
                    L.append(1)                                 

            return L
       
    class Show():
        def __init__(self):
            cur = 0
            for i in self.vectors:
                print(cur,i)
                cur += 1

def factor(x):
    set_size = len(UFD().vectors)
    if set_size - 1 < x:
        UFD().Generate(x)
        return UFD().vectors[x]
    else:
        return UFD().vectors[x]



print('upf.py module name is %s' % __name__)
        




