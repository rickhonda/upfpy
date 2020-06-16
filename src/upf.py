import csv, math, pathlib, os.path
from sympy import prime, primepi

loc = str(pathlib.Path(__file__).parent) + "/vectors.txt"

"""
If the file vectors.txt does not exist in the same directory, create it.
This file stores outputs so they don't have to be recacluated.
"""
if os.path.exists(loc) == False:
    with open(loc, 'w') as csv_file:
        writer = (csv.writer(csv_file, delimiter=','))
        writer.writerow('2')
        writer.writerow([])
        writer.writerow('0')
        writer.writerow('1')

class UFD:
    def __init__(self):

        # Open the file vectors.txt and populate the list csv_reader.
        with open(loc) as csv_file:
            csv_reader = list(csv.reader(csv_file, delimiter=','))
            cur = 0
            for row in csv_reader:
                csv_reader[cur] = list(map(int, row))
                cur +=1
        # Set prime and integer vectors and allow access to each subclass
        self.primes = csv_reader[0]
        self.vectors = csv_reader[1:]
        
        self.generate = self.Generate
        self.generate.primes = self.primes
        self.generate.vectors = self.vectors
        
        self.show = self.Show
        self.show.vectors = self.vectors

    """
    Generates and stores new vectors; i.e., fully factored integers.
    There is also a subclass Show() that will be moved elsewhere 
    and changed.

    Generate is only called when the factor() is called
    to produce a vector that is not already in the list UFD().vectors. 
    
    Note: I'm half tempted to rename UFD() to Integer().
    """
    class Generate(object):
        def __init__(self,N):
            # set_size is the number of factored integers in self.vectors
            set_size = len(self.vectors) - 1
            # Construct the next vector and append it to self.vectors up to N
            while set_size < N:
                self.vectors.append(self.dcomp(set_size + 1))
                set_size +=1
                
            # Write new vectors to vextors.txt
            with open(loc, 'w') as update_vectors:
                writer = (csv.writer(update_vectors, delimiter=','))
                writer.writerow(self.primes)
                writer.writerows(self.vectors)

        """
        Index-wise adds two lists and outputs a list who's length is the same as 
        the larger list. 
        """
        def plus(self,a,b):
            c = abs(len(a)-len(b))
            if len(a) < len(b):
                a = a + [0] * c
            else:
                b = b + [0] * c
            d = [x+y for x,y in zip(a,b)]
            return d

        """
        Gives the number of factors of x in n.
        """
        def XfactN(self,x,n):
            # a is n modulo x
            a = n%x
            counter = 0
            # if a is zero, n has one or more factors of x, let's count them.
            while a == 0:
                counter +=1
                # divide by x; i.e., factor it out and call it N
                n = n/x
                # a is N modulo x; if a is still zero, lets do another iteration
                a = n%x
            # output is the number of iterations; i.e., the number of factors of x in n    
            return counter

        """
        Takes an integer I, returns the vector for I; that is, a list who's index values
        are the exponents on the nth prime in the unique prime factorization of I.
        """
        def dcomp(self,I):
            i = I
            L = []
            cur = 1
            # Cycle through each prime up to sqrt(I), count number of factors and append to L.
            while i != 1 and prime(cur) <= math.sqrt(I):          
                exponent_of_p = self.XfactN(prime(cur),i)         
                L.append(exponent_of_p)
                # If prime(cur) divides i(i.e., expontent_of_p is non-zero), factor it out.
                if exponent_of_p != 0:
                    i = i//(prime(cur)**exponent_of_p)
                cur += 1
            # If we reach sqrt(I) and i is still not one, i is either already in self.vectors or i is prime
            if i > 1:
                # Is i in self.vectors?
                if (len(self.vectors) - 1) >= i:
                    # If yes indexwise add L and the ith vector in self.vectors and set it to L
                    L = self.plus(L,self.vectors[i])
                # If i isn't in self.vectors by now it must be prime
                else:
                    self.primes.append(i)
                    # consturct a prime vector
                    L = (primepi(I)-1)*[0]
                    L.append(1)                                 
            return L

    """
    Lists each integer in self.vectors next to its fully factored form
    """       
    class Show():
        def __init__(self):
            cur = 0
            for i in self.vectors:
                print(cur,i)
                cur += 1

"""
Takes an integer x and returns vector representing the unique prime factorizaiton of x.
"""
def factor(x):
    set_size = len(UFD().vectors) - 1
    if set_size  < x:
        UFD().generate(x)
    return UFD().vectors[x]








