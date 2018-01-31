#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):

    prev = 0
    curr = 1
    
    for i in range(n):
        prev, curr = curr, prev + curr

    return prev

print (fibonacci(2))
#>>> 14930352