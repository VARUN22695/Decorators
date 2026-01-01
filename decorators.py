def multiply(func):
    def k(a,b): 
      m=func(a,b)
      n= a**3 +b**3
      return m ,n
    return k

def formula(func):
    def wrapper(a,b):
        r1= func(a,b)
        result= a**2 + b**2+2*a*b   
        return r1, result
    return wrapper


@multiply
@formula
def addition(a,b):
    return a+b 

print(addition(3,4))