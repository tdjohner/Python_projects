#--------------------------
#   Lab6TJ.py             -
#--------------------------
#   Teagan Johner         -
#--------------------------

from graphics import*


#    Description:
def main():
    global win
    win = GraphWin("clockWindow", 300, 200)
    point1 = Point(0,0)
    point2 = Point(300,200)
    winRect = Rectangle(point1, point2)
    winRect.draw(win)
    winRect.setFill('white')
    label = add_label(win, 150, 25, 'text here')
    label.draw(win)
    add_button(win, 100, 150, "Start/Restart")
    add_button(win, 200, 150, "Exit")
    entry = add_entry(win, 150, 50, 20)
    
    
#    Syntax: label = add_label(win, x, y, text)
#    Parameter: win GraphWin object: 
#               x, y - the window int values: location for centre of label
#               text - str object: text to use for label
#    Return value: words - Text object used for the label 
#    Description: places a text object at the specified coordinates in 
#                  clockWindow
def add_label(win, x, y, text):
    point = Point(x, y)
    words = Text(point, text)
    words.setSize(8)
    words.setStyle('bold')
    return words
    

#    Syntax: button = add_button(win, x, y, text)
#    Parameter: win - GraphWin object: the window
#               x, y - int values: location for centre of button
#               text - str object: text to use for button’s label
#    Return value: clicker – Rectangle object used for the button
#    Description: adds a button at specified coordinates in 
#                  clockWindow
def add_button(win, x, y, text):
    point1 = Point( x-50, y+15 )
    point2 = Point( x+50, y-15 )
    clicker = Rectangle(point1, point2)
    clicker.setOutline('black')
    clicker.setFill('grey')
    labelA = add_label(win, x, y, text)
    clicker.draw(win)
    labelA.draw(win)
    return clicker
    
#    Syntax: entry = add_entry(win, x, y, width)
#    Parameter: win – GraphWin object: the window
#               x, y – int values: location for centre of entry
#               width – int value: width (in characters) of object
#    Return value: rectangle – Entry object    
#    Description: adds a user input receptacle at specified coordinates 
#                  in clockWindow
def add_entry(win, x, y, width):
    point = Point(x, y) 
    rectangle = Entry(point, width)
    rectangle.setFill('grey')
    rectangle.draw(win)
    return rectangle
    
#    Syntax: flash(winRect, flashCount)
#    Parameter: winRect - rectangle graphics object, clock background
#               flashCount - int, number of times clock flashes
#    Return value: none
#    Description: flashes the background of the clock after the countdown
def flash(winRect, flashCount):
    for i in range(flashCount):
        winRect.setFill('black')
        time.sleep(0.1)
        winRect.setFill('white')
        time.sleep(0.1)

#    Syntax: 
#    Parameter: 
#               
#    Return value: 
#    Description: 
def convert_to_seconds(entry):
    chronoString = getText(entry)
    chronoList = int(chronoString.split(':'))
    secondCount = 0
    for i in range(len(chronoList), 0, -1):
        secondCount += (60**i * chronoList[i])
        
#    Syntax: 
#    Parameter: 
#               
#    Return value: 
#    Description:        
def convert_to_time(secondCount):
    clockForm = (str(secondCount //60) + ':' + str(secondCount % 60))
    return clockForm
    
#    Syntax: 
#    Parameter: 
#               
#    Return value: 
#    Description:    
def is_clicked(point, button):
    top_left = button.getP1()
    bottom_right = button.getP2()
    return (point.x >= top_left.x and point.x <= bottom_right.x and point.y >= top_left.y and point.y <= bottom_right.y)
    
    