#--------------------------
#   CelticaTJ.py          -
#--------------------------
#   Teagan Johner         -
#--------------------------


from graphics import*
import random
import time

#   syntax:     main()
#   parameters: none
#   returns:    noe
#    oversees the operation of the entire game by calling other functions
def main():
    
    objList = set_board()
    play_button( objList )
    run_game()


#   syntax:     run_game()
#   parameters: none
#   returns:    none
#    creates, draws, and controls the game board during play
def run_game():
    global marbleList
    
    board = setup_game()
    marbleList = display()
    board = shuffle_board(board, marbleList)
         # adds text object to verify marble check  
           
    
    while is_game_over(board) == False:
        move = win.getMouse()
        xRoot = move.getX()
        yRoot = move.getY() 
        
        for i in range(len(marbleList)):  
            current = marbleList[i]
            curPoint = current.getCenter()
            dX = xRoot - curPoint.getX()
            dY = yRoot - curPoint.getY()
            
            if dX * dX + dY * dY <= current.getRadius() * current.getRadius():
                
                j = board.index('X')
                swap(i, j, board)
                break
               
                       
    victory = Text ( Point( 150, 150 ), 'You Win!')
    victory.setSize(16)
    victory.setStyle('bold')
    victory.draw(win)    
                
    playAgain = Rectangle( Point ( 272.5, 200 ), Point ( 372.5, 260 ))
    playAgain.setFill(color_rgb( 60, 150, 150 ))  
    playAgain.draw(win)
            
    replay = Text( Point( 322.5, 230 ), 'Play Again')
    replay.draw(win)
            
    exxit = Rectangle( Point ( 272.5, 300 ), Point ( 372.5, 360 ))
    exxit.setFill(color_rgb( 60, 130, 130 ))  
    exxit.draw(win)
        
    exxitt = Text( Point( 322.5, 330), 'Exit')
    exxitt.draw(win)
            
    end_seq(playAgain, replay, exxit, exxitt)
    
def set_board():
    global win
    win = GraphWin("Celtica ", 445, 445)
    win.setBackground( color_rgb(20, 50, 220))
    
    title = Text( Point( 222.5, 78), 'Celtica')
    title.setStyle('bold')
    author = Text( Point( 222.5, 95), 'by: Brian Brookwell')
    
    instruct1 = Text( Point (222.5, 140), 'Get all of the circles ')
    instruct2 = Text( Point (222.5, 160), 'to their original positions')
    instruct3 = Text( Point (222.5, 180), 'by clicking on the circles' )
    instruct4 = Text( Point (222.5, 200), 'beside the empty (black) circle' ) 
    
    
    play = Rectangle( Point ( 172.5, 300), Point ( 272.5, 360 ))
    play.setFill( color_rgb(30, 195, 0))
    playnow = Text ( Point( 222.25, 330), 'Play')
    playnow.setStyle('bold')
        
    objList = []
    
    title.draw(win)
    objList.append(title)
    
    author.draw(win)
    objList.append(author)
    
    play.draw(win)
    objList.append(play)
    
    playnow.draw(win)
    objList.append(playnow)
    
    instruct1.draw(win)
    objList.append(instruct1)
    
    instruct2.draw(win)
    objList.append(instruct2)
    
    instruct3.draw(win)
    objList.append(instruct3)
        
    instruct4.draw(win)
    objList.append(instruct4)
    
    return objList 
    
    
def swap(i, j, board):
    
    if i == 32 and j in (4, 12, 20, 28) or i in (4, 12, 20, 28) and j == 32:
        board = exchange(board, i, j)
        color_swap(marbleList, board, i, j)
        return
            
    elif i == 32 or j == 32:
        return

    elif abs(j-i) > 16:
        if j > i:
            for x in range((31 - j) + (i + 1)):
                if j == 31:
                    k = 0
                else:
                    k = j+1
                board = exchange(board, j, k)
                color_swap(marbleList, board, j, k)
                
                time.sleep(.1)
                j = j+1
                if j == 32:
                    j = 0
            return 
          
        if i > j:
            for x in range((j +1) + (31 - i)):
                
                if j == 0:
                    k = 31
                    board = exchange(board, j, k)
                    color_swap(marbleList, board, j, k)   

                    time.sleep(.1)
                    j = 31
                    
                else:
                    k = j-1
                    board = exchange(board, j, k)
                    color_swap(marbleList, board, j, k)
                
                    time.sleep(.1)
                    j = j-1
                
            return               
 
    elif i > j:
        while i > j:
            board = exchange(board, j, j+1)
            color_swap(marbleList, board, j, j+1)
            time.sleep(.1)
            j = j+1
        return
            
    elif j > i:
        while j > i:
            board = exchange(board, j, j-1)
            color_swap(marbleList, board, j, j-1)
            time.sleep(.1)
            j = j-1   
        return
            
            
#   syntax: exchange(board, first, second)
#   parameters: list, int, int 
#   returns: list
#   swaps the position of two pieces on the game board
def exchange(board, first, second):
    while first > 32:
        first = first - 33
    while second > 32:
        second = second - 33
    placeHolder = board[first]
    board[first] = board[second]
    board[second] = placeHolder
    return board

#   syntax:     color_swap(marbleList, board, i, j)
#   parameters: marbleList, board, i, j
#   returns:    none
#    changes the colors of Circle objects to match the manipulation of board
def color_swap(marbleList, board, i, j):
    while i > 32:
        i = i - 33
    while j > 32:
        j = j - 33
    colorDict = { 'G': 'lightgreen', 'R': 'Red', 'Y': 'Yellow', 'B': 'Cyan', 'X': 'Black'}
    marbleList[i].setFill(colorDict[board[i]])
    marbleList[j].setFill(colorDict[board[j]])
    

    
#   syntax:     end_seq(playAgain, replay, exxit, exxitt)
#   parameters: playAgain, replay, exxit, exxitt
#   returns:    none
#    upon completion of the gameplay, prompts user to play again or exit
def end_seq(playAgain, replay, exxit, exxitt):
    endAct = win.getMouse()
    clickx = endAct.getX()
    clicky = endAct.getY()
    replayX = playAgain.getCenter().getX()
    replayY = playAgain.getCenter().getY()
    
    exxitX = exxit.getCenter().getX()
    exxitY = exxit.getCenter().getY()
    
    if clickx > (replayX - 50 ) and clickx < (replayX + 30) and clicky > (replayY - 50) and clicky < (replayY + 50): 
        playAgain.undraw()
        replay.undraw()
        exxit.undraw()
        exxitt.undraw()
        run_game()
        
    elif clickx > (exxitX - 50 ) and clickx < (exxitX + 30) and clicky > (exxitY - 50) and clicky < (exxitY + 50):
        
        win.close()  
    
    else:
        end_seq(playAgain, replay, exxit, exxitt)
    
    
#   syntax:     shuffle_board(board, marbleList)
#   parameters: board, marbleList
#   returns:     board
#    randomizes the game board for play
def shuffle_board(board, marbleList):
    
    paintBucket = { 'R':'red', 'B':'cyan', 'G':'lightgreen', 'Y':'yellow', 'X': 'black' }
    
    random.shuffle(board)
    for i in range(len(board)):
        color_swap( marbleList, board, i, i)
        
       # move = random.choice([4, 12, 20, 28])
       # board = exchange(board, move, 32)
       # color_swap(marbleList, board, move, 32)
       # move = board.index('X')
        #for j in range((random.randint(1, 8) * 8)):
          #  board = exchange(board, move, move + 1)
           # color_swap(marbleList, board, move, move + 1)
           # move += 1
            
    return board
                                   
#   syntax: setup_game()
#   parameters: none
#   returns: list
def setup_game():
    
    board = []
    gryb = 'GRYB'   # Green Red Yellow Blue -> to be used in
    for i in range(5):
        board.append(gryb[3])
    for i in range(8):
        board.append(gryb[0])
    for i in range(8):
        board.append(gryb[1])
    for i in range(8):
        board.append(gryb[2])
    for i in range(3):
        board.append(gryb[3])
    board.append('X')
    return board

#   syntax: display(board)
#   parameters: list
#   returns: none
#   prints the board in a square, all character placements 
#    correspond to their respective list indicies
def display():
    
    global marbleList
    
    win.setBackground('navy')
    background()
    
    marbleTrack = []
    marbleList = []
    
    for i in range(9):
        marbleTrack.append( Point( ((i * 44.5) + 44.5), 44.5) )
        
    for i in range(8):
        marbleTrack.append( Point( 400.5, ((i * 44.5) + 89)) )
    
    for i in range(8):
        marbleTrack.append( Point( (356 - (i * 44.5)), 400.5) )
        
    for i in range(7):
        marbleTrack.append( Point( 44.5, (356 - (i * 44.5))) )
        
    marbleTrack.append( Point( 222.5, 222.5))
    
    for i in range( 5 ):
        make_circ( marbleTrack[i], 'cyan')
        
    for i in range ( 8 ):
        make_circ( marbleTrack[i+5], 'lightgreen')
        
    for i in range ( 8 ):
        make_circ( marbleTrack[i+13], 'red')
        
    for i in range ( 8 ):
        make_circ( marbleTrack[i+21], 'yellow')
        
    for i in range ( 3 ):
        make_circ( marbleTrack[i+29], 'cyan')
        
    make_circ( marbleTrack[32], 'black') 
    
    return marbleList

def make_circ( x, fill):
    circle = Circle(x, 18)
    circle.setWidth(2)
    circle.setOutline('white')
    circle.setFill(fill)
    circle.draw(win)
    marbleList.append(circle)
    
def background():
    pointA = Point(25, 25)
    pointB = Point(200, 200)
    rect = Rectangle(pointA, pointB)
    rect.setFill('blue')
    rect.draw(win)
    
    pointA = Point(245, 25)
    pointB = Point(420, 200)
    rect = Rectangle(pointA, pointB)
    rect.setFill('green')
    rect.draw(win)
    
    pointA = Point(25, 245)
    pointB = Point(200, 420)
    rect = Rectangle(pointA, pointB)
    rect.setFill('yellow4')
    rect.draw(win)
    
    pointA = Point(245, 245)
    pointB = Point(420, 420)
    rect = Rectangle(pointA, pointB)
    rect.setFill('red4')
    rect.draw(win)  
    
#   syntax:     play_button(play, title, author, playnow, instruc1, instruct2)
#   parameters: play, title, author, playnow, instruct1, instruct2 (graphics objects)
#   returns:    none
#    if the play button is clicked, undraws the objects and calls run_game()
def play_button(objList):
    while True:
        playClick = win.getMouse()
        clickx = playClick.getX()
        clicky = playClick.getY()
        rectX = objList[2].getCenter().getX()
        rectY = objList[2].getCenter().getY() 
    
        if clickx > (rectX - 30 ) and clickx < (rectX + 30) and clicky > (rectY - 50) and clicky < (rectY + 50):
            for i in range(len(objList)):
                objList[i].undraw()
            break
    
                
#   syntax: is_game_over(board)
#   parameters: list
#   returns: True or False
#   compares the current game board to a completed one and returns True if
#    they are the same and False if they are not
def is_game_over(board):
    correctBoard = setup_game()
    if correctBoard == board:
        return True
    else:
        return False
    