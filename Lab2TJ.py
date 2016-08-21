#--------------------------
#   Lab2TJ.py             -
#--------------------------
#   Teagan Johner         -
#--------------------------

def loop_a():
    for i in range(20, 33, 3):
        print(i)
        
        
def loop_b():
    for i in range(7, -2, -2):
        print(i)
        
       
#   syntax: diamond_maker()
#   parameters: none
#   returns: none
#   diamond_maker() is the main function, it calls get_width()
#    and uses an if statement to determine which diamond to build
def diamond_maker():
    width = get_width()
    if width % 2 == 0:
        hollow_diamond()
    else:
        fulldiamond()
        
#   syntax: get_width()
#   parameters: none()
#   returns: int
#   get_width() prompts user for input then runs test_width()
#    to verify it is acceptable
def get_width():
    width = input('Enter a positive number:')
    test_width(width)
    return int(width)
        

#   syntax: test_width()
#   parameters: width *int or char*
#   returns: none
#   test_width() is given a variable and if it is not a 
#    positive int it simply calls get_width to get another input
def test_width(width):
    if width.isnumeric():
        while width < 1:
            get_width()
    else:
        get_width()
        
        
def hollow_diamond(width):
    edge = '*'
    center = ' '
    for i in range(width//2):
        centCount = (i - 1)
        edgeCount = ((width/2) - (i-1))
        print(edge * edgeCount, center * centCount, center * centCount, edge * edgeCount)