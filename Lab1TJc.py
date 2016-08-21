#-------------------------------------------------------------------------

#                   Lab1TJ.py

#-------------------------------------------------------------------------

#                Teagan Johner

#                  Program name:  Alternate List Compiler
#-------------------------------------------------------------------------

def alternate(listA, listB):
    result = []
    for i in range(len(listA)):
        if i % 2 == 0:
            result[i] = listA[i]
        else:
            result[i] = listB[i]
    return result
            

        
        
    
    
        
        
        
    