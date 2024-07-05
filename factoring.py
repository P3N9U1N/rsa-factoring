import math
from typing import Generator

def rsa(n:int)->tuple[int,int]:
    if n==0: return None
    if n % 2 ==0: return (2,n//2)
    i=math.isqrt(n)
    i=i-1+(i%2) 
    rest=n-i*i
    left=right=i    
    while rest!=0:
        while rest >0:
            left+=2
            rest-=(right<<1)
        while rest <0:
            right-=2
            rest+=(left<<1)         
    return (left,right)

  
def factor(n:int)->Generator[int,None,None]:
    factor1,factor2=rsa(n)
    if factor2 ==1:
        yield n
    else:
        yield from factor(factor1)
        yield from factor(factor2)

