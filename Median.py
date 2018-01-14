# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a, b ,c):
    if (b >= a and a >= c) or (c >= a and a >= b):
        return a
    if (a >= b and b >= c) or (c >= b and b >= a):
        return b
    if (a >= c and c >= b) or (b >= c and c >= a):
        return c
        
        
    
print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7