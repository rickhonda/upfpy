# upfpy

Right now this package only includes one function, factor(); it takes an integer and returns a list. 

The values of the list indices are such that the nth index contains the power on the nth prime in the Unique Prime Factorization of the given integer so that 2=[1], 3=[0,1] and 12=[2,1] and so fourth, the rest of the indices greater than the length of the list assumed to be zero. 


## Installation 

Run the following to install: 

...python\n
...pip install upfpy

## Usage

...python
from upf import factor
upf.py module name is upf

# factor(3)
[0, 1]
# factor(33)
[0, 1, 0, 0, 1]
# factor(32)
[5]


