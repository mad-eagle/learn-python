# factorial method

def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n*factorial(n-1)

a = factorial(1)

# fibonacci number

def fibonacci(n):
    if(n==0 or n==1):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
b = fibonacci(35)

print(b)