

def top_n(items, n):
    """"This function will return top n elements in desc order  
    Args:
     items (array) :list of  array-like object 
     n(int): num of items to return 
     
    Return :
     array : top n items , in desc order
     
     Egs :
      >>> top([7,1,4,0,2,],3)
        [7,4,2]
    """
    for i in range(n):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j],items[j+1]= items[j+1],items[j] # swap
                
    
    top_n = items[-n:]
    
    return top_n[::-1]