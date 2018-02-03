# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def remove_tags(page_with_tags):
    page_without_tags = ""
    
    is_there_open_tag = False
    
    for c in page_with_tags:
        
        if c == '<':
            page_without_tags += " "
            is_there_open_tag = True
        elif c == '>':
            is_there_open_tag = False
        else:
            if not is_there_open_tag:
                page_without_tags += c
    
    return page_without_tags.split()
        


print (remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>'''))
#>>> ['Title','This','is','a','link','.']

print (remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>'''))
#>>> ['Hello','World!']

print (remove_tags("<hello><goodbye>"))
#>>> []

print (remove_tags("This is plain text."))
#>>> ['This', 'is', 'plain', 'text.']