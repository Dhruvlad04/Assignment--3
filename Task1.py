# factorial of a number using recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        fact =1
        for i in range(1,n+1):
            fact*= i
    return fact
n=int(input("Enter a number: "))
print("Factorial of",n,"is",factorial(n))
