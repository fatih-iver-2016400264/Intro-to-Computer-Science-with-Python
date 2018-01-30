# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift(letter):
    return chr(ord(letter) + 1) if letter != 'z' else 'a'
    
def shift_back(letter):
    return chr(ord(letter) - 1) if letter != 'a' else 'z'


def shift_n_letters(letter, n):
    
    if n >= 0:
        for i in range(n):
            letter = shift(letter)
    else:
        for i in range(-n):
            letter = shift_back(letter)
    return letter



print (shift_n_letters('s', 1))
#>>> t
print (shift_n_letters('s', 2))
#>>> u
print (shift_n_letters('s', 10))
#>>> c
print (shift_n_letters('s', -10))
#>>> i