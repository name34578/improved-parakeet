print("hello world")

def factorial(a):
    if a==1:
        return a
    a = a * factorial(a - 1)
    return a

print(factorial(5))

input()
