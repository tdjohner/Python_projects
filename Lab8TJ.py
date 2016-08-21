#--------------------------
#   Lab8TJ.py             -
#--------------------------
#   Teagan Johner         -
#--------------------------



portfolio = [('25 Jan 2015', 23.26, 17, 'CAT', 54.64), ('25 Jan 2015', 13.11, 15, 'DKL', 23.54), ('25 Jan 2015', 64.16, 65, 'GHJK', 69.87)]


#    Syntax:       total_purchase_price(portfolio)
#    Parameter:    dictionary               
#    Return value: int
#    Description:  takes a dictionary and returns the
#                   total amount paid for the portfolio
def total_purchase_price(portfolio):
    portPrice = 0
    for i in range(len(portfolio)):
        portPrice += (portfolio[i][1] * portfolio[i][2])
    return round(portPrice, 2)

#    Syntax:       total_value(portfolio)
#    Parameter:    dictionary               
#    Return value: int
#    Description:  takes a dictionary and returns the
#                   total cost to purchase all stocks
#                   in the portfolio
def total_value(portfolio):
    portValue = 0
    for i in range(len(portfolio)):
            portValue += (portfolio[i][4] * portfolio[i][2])
    return round(portValue, 2)    
    
#    Syntax:       total_gain(portfolio)
#    Parameter:    dictionary               
#    Return value: int
#    Description:  takes a dictionary and returns the 
#                   difference between total purchase price
#                   and total value
def total_gain(portfolio):
    cost = total_purchase_price(portfolio)
    revenue = total_value(portfolio)
    profit = revenue - cost
    return round(profit, 2)

#    Syntax:       testQ1()
#    Parameter:    none               
#    Return value: none
#    Description:  a main function that calls the helper 
#                   functions and prints the values they return
def testQ1():
    cost = total_purchase_price(portfolio)
    revenue = total_value(portfolio)
    profit = total_gain(portfolio)
    print('Total cost      =',  cost)
    print('Current value   =', revenue)
    print('Total gain/lost =', profit)
    

#    Syntax:       read_file(fileName)  
#    Parameter:    string               
#    Return value: dictionary
#    Description:  takes a file name and reads it into a dictionary
#                   then returns the dictionary
def read_file(fileName):
    try:
        tempData = open(fileName)
        dataString = tempData.read()
        dataString = dataString.lower()
        tempData.close()
    except:
        print('There is a problem with the file')
        
    tempDict = {}
    
    dataString = dataString.split('\n')
    
    # series of for loops to break the file into
    #  a 2 dimenional list
    for i in range(len(dataString)):
        dataString[i] = dataString[i].split(':')
    for j in range(len(dataString)):
        dataString[j][1] = dataString[j][1].split(',')
    # nested for loop converts the lists of numbers
    #  from string to integer types
    for k in range(len(dataString)):
        for m in range(len(dataString[k][1])):
            dataString[k][1][m] = int(dataString[k][1][m])
                                    
    # this loop puts the list into a dictionary
    for d in range(len(dataString)):
        tempDict[dataString[d][0]] = dataString[d][1]
            
    return tempDict

#    Syntax:       month_temp(month, tempDict)  
#    Parameter:    string, dictionary               
#    Return value: list
#    Description:  returns the temperatures in a month
#                   that only happened once that month
def month_temp(month, tempDict):
    month2 = tempDict.pop(month)
    listlzr = []
    
    for i in range(len(month2)):
        if month2[i] not in listlzr:
            listlzr.append(month2[i])
            
    tempDict[month] = month2
    
    return listlzr

#    Syntax:       common_degrees(tempDict)
#    Parameter:    dictionary               
#    Return value: list
#    Description:  returns a list of degrees that were
#                   recorded in every month
def common_degrees(tempDict):
    common = []
    commonTick = 0
    for i in tempDict.keys():
        for j in range(len(tempDict[i])):
            for k in tempDict.keys():
                if tempDict[i][j] in tempDict[k] and tempDict[i][j] not in common:
                    commonTick += 1
                    
            if commonTick == 12:
                common.append(tempDict[i][j])
            commonTick = 0
                
    return common

#    Syntax:       rare_degrees(month, tempDict)
#    Parameter:    string, dicionary               
#    Return value: list
#    Description:  returns a list of degrees that were
#                   recorded exclusively in the month specified
def rare_degrees(month, tempDict):
    month2 = tempDict.pop(month)
    listlzr = []
        
    for i in range(len(month2)):
        for j in tempDict.keys():
            if month2[i] not in tempDict[j]:
                listlzr.append(month2[i])
    month2 = []
        
    for i in range(len(listlzr)):
        if listlzr[i] not in month2:
            month2.append(listlzr[i])
            
    tempDict[month] = month2
                
    return month    

#    Syntax:       degree_limits(tempDict)
#    Parameter:    dictionary               
#    Return value: dictionary
#    Description:  returns a dictionary of the highest and 
#                   lowest temperatures of each month
def degree_limits(tempDict):
    limitDict = {}
    high = 0
    low = 100
    
    for i in tempDict.keys():
        for j in range(len(tempDict[i])):
            for k in range(len(tempDict[i])):
                if tempDict[i][k] > high:
                    high = tempDict[i][k]
                
                if tempDict[i][k] < low:
                    low = tempDict[i][k]
        
        limitDict[i] = (high, low)
        high = 0
        low = 100
        
    return limitDict

#    Syntax:       testQ2  
#    Parameter:    none               
#    Return value: none
#    Description:  calls the functions and prints a demonstration
#                   of their calls and returns
def testQ2():
    tempDict = read_file('yearly_temperature.txt')
    monthTemp = month_temp('february', tempDict)
    commonTemp = common_degrees(tempDict)
    rareTemp = rare_degrees('december', tempDict)
    degLimit = degree_limits(tempDict)
    
    print("month_temp('february', tempDict):", monthTemp)
    print("common_degrees(tempDict):", commonTemp)
    print("rareTemp = rare_degrees('december', tempDict):", rareTemp)
    print("degLimit = degree_limits(tempDict):")
    for i in degLimit.keys():
        print(i + ':', degLimit[i])
        
            
                
                           
            
            
    

                    
    
                
    
                       


                
                
                    
                    
                    
                
                

        




        
        

        
    
    


    
        
                
    
