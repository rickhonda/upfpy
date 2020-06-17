# UpfPy 

This package includes a function, factor(); it takes an integer and returns a list. 

This list represents the Unique Prime Factorization of a given integer. 

https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic

The values of the list indices are such that the nth index contains the power on the nth prime in the Unique Prime Factorization of the given integer so that 2=[1], 3=[0,1] and 12=[2,1] and so fourth; the list terminates when the rest of the subsequent values are all zero. 

These lists are stored in a file called vectors.txt as csv. The reason I made this is partly to generate that file. Next we will be adding a number of basic functions to analyze that file which is really a model of the prime factor structure inside integers; and also I want to make it faster and make it reflect other aspects of prime numbers such as all primes greater than 3 are either 1 or 5 modulo 6.

## Installation 

Run the following to install:  

pip install upfpy  

## Usage

The first time upfpy is imported it will create a file, vectors.txt; from here on out will refer to the lists produced by factor() as vectors. The inital file contains four rows. 

The first row will be a csv list of primes and the initial file will just have a 2 here. When factor() is given a number, say N, greater than 2, all the primes less than N will appended here after a comma; it will append N if N is prime. The subsequent rows are vectors, i.e., unique prime factor lists.

The second row will contain an empty bracket [ ], this represents the integer zero and is the "null" or "empty" vector.

The third row represents the number one and contains a '0'. Consider: 

1 = (2\*\*0)\*(3\*\*0)\*(5\*\*0)\*(7\*\*0)...(n\*\*0)... = [0,0,0,0,...] = [0]; where n is the nth prime 

which is not true in python but it's true in math and we are modeling this structure using python.

The forth row represents the integer 2 and contains a '1'; because... 

2 = (2\*\*1)\*(3\*\*0)\*(5\*\*0)... = [1,0,0,...] = [1]

...python  
&gt;&gt;&gt; from upfpy import *  
&gt;&gt;&gt; factor(30)  
[1,1,1]  

There is one class, UFD() in upf and it has two subclasses Generate() and Show(); I will relocate and change this. Generate() is used to calculate vectors that arent already in vectors.txt and writes them to there as needed. 

If you exectued factor(30) as earlier you could execute:

&gt;&gt;&gt; UFD().primes  
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

also note:  

&gt;&gt;&gt; UFD().vectors[1:6]    
[[0], [1], [0, 1], [2], [0, 0, 1]]

and:  

&gt;&gt;&gt; UFD().show()  
0 []  
1 [0]  
2 [1]  
3 [0, 1]  
4 [2]  
5 [0, 0, 1]  
...  
28 [2, 0, 0, 1]  
29 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]  
30 [1, 1, 1]  


