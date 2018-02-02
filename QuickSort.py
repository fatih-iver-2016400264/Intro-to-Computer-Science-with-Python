# Use this to try out anything you like. Use print to display your answer
# when you press the "Test Run" button.
# Use the "Reset" button to reset the screen 

def median_of_three(ls):
    print("will be done")
    

def quicksort(ls):
    
    if not ls:
        return []
    elif len(ls) == 1:
        return ls
    else:
        
        pivot = ls[0]
    
        left = []
        right = []
        middle = []
        
        for e in ls:
            if e > pivot:
                right.append(e)
            elif e < pivot:
                left.append(e)
            else:
                middle.append(e)
    
        return quicksort(left) + middle + quicksort(right)
    
print(quicksort([6,2,8,1,2,7,3,9]))