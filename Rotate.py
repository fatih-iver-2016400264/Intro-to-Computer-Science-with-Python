# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.


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

def rotate(string, n):
    newString = ""
    
    for letter in string:
        newString += shift_n_letters(letter, n) if letter != " " else " "
        
    return newString
    
    # Your code here

print (rotate ('sarah', 13))
#>>> 'fnenu'
print (rotate('fnenu',13))
#>>> 'sarah'
print (rotate('dave',5))
#>>>'ifaj'
print (rotate('ifaj',-5))
#>>>'dave'
print (rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17))
#>>> ???