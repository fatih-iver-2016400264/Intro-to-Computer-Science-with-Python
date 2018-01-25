# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.

def measure_udacity(ls):
    counter = 0
    for s in ls:
        counter += 1 if s[0] == 'U' else 0
    return counter

#print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

#print measure_udacity(['Umika','Umberto'])
#>>> 2