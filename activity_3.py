
def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)

function = int(input("Enter a number from 1 - 10: "))
print(factorial(function))

