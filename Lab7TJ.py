#--------------------------
#   Lab7TJ.py             -
#--------------------------
#   Teagan Johner         -
#--------------------------


#    Syntax:       intersect(dict1, dict2)
#    Parameter:    dictionary, dictionary              
#    Return value: dictionary
#    Description:  takes two dictionaries and makes a new 
#                   dictionary from them that contains all key/value
#                   pairs that are the same
def intersect(dict1, dict2):
    dict3 = {}
    if len(dict1) > len(dict2):
        for i in dict1.keys():
            for k in dict2.keys():
                if i in k and dict1[i] == dict2[k]:
                    dict3[i] = dict1[i]
                                                  
    else:
        for i in dict2.keys():
            for k in dict1.keys():
                if i in k and dict2[i] == dict1[k]:
                    dict3[i] = dict1[i]
                    
    return dict3


#    Syntax:       is_submap(dict1, dict2)
#    Parameter:    dictionary, dictionary
#    Return value: True / False
#    Description:  makes sure all key/value pairs in the
#                   first dictionary are in the second
def is_submap(dict1, dict2):
    mapFail = 0
    for i in dict1.keys():
        for k in dict2.keys():
            if i in k and dict1[i] == dict2[k]:
                mapFail = 1
                
    if mapFail == 1:
        return True
    else:
        return False


#    Syntax:       is_neighbour(stringA, stringB)
#    Parameter:    string, string
#    Return value: True / False
#    Description:  returns True if the edit distance between
#                   strings is 1, othwerwise returns False
def is_neighbour(stringA, stringB):
    editCount = 0
    if len(stringA) != len(stringB):
        return False
    else:
        for i in range(len(stringA)):
            if stringA[i] != stringB[i]:
                editCount += 1
    if editCount != 1:
        return False
    else:
        return True


#    Syntax:       build_neighbour_map(fileName)
#    Parameter:    string  (name of file)
#    Return value: dictionary
#    Description:  takes all strings in a file and returns
#                   a dictionary containing all neighbors as
#                   values for neighbour keys
def build_neighbour_map(fileName):
    
    neighbourDict = {}
    nameList = []
    try:
        
        with open(fileName) as file:
            for line in file:
                nameList.append(line)
                
            for i in range(len(nameList)):
                subNameList = []
                for k in range(len(nameList)):
                    if is_neighbour(nameList[i], nameList[k]) == True:
                        subNameList.append(nameList[k])
                
                        neighbourDict[nameList[i]] = subNameList
    except: 
        return None
        
    return neighbourDict
    
  
        
                
        
    
    
    
                
            
            
                    
                    