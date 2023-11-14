# rsa-factoring
RSA and number factoring, can be used for solving CTF challenges. It is fast enough for up to 64 bit numbers.
```python
import math
from typing import Generator

def rsa(n:int)->tuple[int,int]:
    if n==0: return None
    if n % 2 ==0: return (2,n//2)
    i=math.isqrt(n)
    i=i+1+(i%2) 
    while(i:=i-2):
        if n%i==0:
            return (n//i,i)    
  
def factor(n:int)->Generator[int,None,None]:
    factor1,factor2=rsa(n)
    if factor2 ==1:
        yield n
    else:
        yield from factor(factor1)
        yield from factor(factor2)

```

Usage:
```python
print(list(factor(500)))
```