from collections import Counter
import labmath
import pytest
import factoring

  
def test_rsa():    
   max=100
   primes=list(p[0] for p in zip(labmath.primegen(),range(max)))
   for x in range(max):
      for y in range(x,max):
         factor1= primes[x]
         factor2= primes[y]       
         rsa_factor=factor1*factor2         
         actual_factor=   tuple(sorted(factoring.rsa(rsa_factor)))
         assert actual_factor == (factor1,factor2)

def test_rsa2():    
   max=10000
   primes=(p[0] for p in zip(labmath.primegen(),range(max)))
   for x in primes:
      factor1,factor2=factoring.rsa(x)
      assert factor2==1
      assert factor1==x
         
def test_factoring():
    max=10000   
    for x in range(2,max):
        actual = Counter(factoring.factor(x))
        expected=labmath.factorint(x)
        assert actual==expected
        
