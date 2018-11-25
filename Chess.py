'''
    15-112: Principles of Programming and Computer Science
    Project: Chess 
    Name      : Abdul Manaam
    AndrewID  : amanaam
'''
##############################  Helper Functions  ##############################
def printBoard(b):
    print '  |a b c d e f g h|'
    print '  -----------------'
    print '8 |'+b[7][0]+' '+b[7][1]+' '+b[7][2]+' '+b[7][3]+' '+b[7][4]+' '+b[7][5]+' '+b[7][6]+' '+b[7][7]+'| 8'
    print '7 |'+b[6][0]+' '+b[6][1]+' '+b[6][2]+' '+b[6][3]+' '+b[6][4]+' '+b[6][5]+' '+b[6][6]+' '+b[6][7]+'| 7'
    print '6 |'+b[5][0]+' '+b[5][1]+' '+b[5][2]+' '+b[5][3]+' '+b[5][4]+' '+b[5][5]+' '+b[5][6]+' '+b[5][7]+'| 6'
    print '5 |'+b[4][0]+' '+b[4][1]+' '+b[4][2]+' '+b[4][3]+' '+b[4][4]+' '+b[4][5]+' '+b[4][6]+' '+b[4][7]+'| 5'
    print '4 |'+b[3][0]+' '+b[3][1]+' '+b[3][2]+' '+b[3][3]+' '+b[3][4]+' '+b[3][5]+' '+b[3][6]+' '+b[3][7]+'| 4'
    print '3 |'+b[2][0]+' '+b[2][1]+' '+b[2][2]+' '+b[2][3]+' '+b[2][4]+' '+b[2][5]+' '+b[2][6]+' '+b[2][7]+'| 3'
    print '2 |'+b[1][0]+' '+b[1][1]+' '+b[1][2]+' '+b[1][3]+' '+b[1][4]+' '+b[1][5]+' '+b[1][6]+' '+b[1][7]+'| 2'
    print '1 |'+b[0][0]+' '+b[0][1]+' '+b[0][2]+' '+b[0][3]+' '+b[0][4]+' '+b[0][5]+' '+b[0][6]+' '+b[0][7]+'| 1'
    print '  -----------------'
    print '  |a b c d e f g h|'
    print '_____________________'
#_______________________________________________________________________________
def takeInput():
    validAlphabets   = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']   
    validPieces = ['P', 'R', 'B', 'N', 'K', 'Q','p','r', 'b', 'n', 'k', 'q']
    pieceToMove = raw_input('Enter the name and position of piece to move i.e Re4: ')
    while (pieceToMove[0].isalpha()==False or pieceToMove[0] not in validPieces) or (pieceToMove[1].isalpha() == False or pieceToMove[1] not in validAlphabets) or (pieceToMove[2].isdigit() == False or int(pieceToMove[2]) > 8):
        pieceToMove = raw_input('Invalid Command, enter the name and position of piece to move i.e Re4: ')    
    moveTo = raw_input('Where do you want the piece to move i.e e6: ')
    d = int(moveTo[1])
    while (moveTo[0].isalpha() == False or moveTo[0] not in validAlphabets) or d > 8:
        moveTo = raw_input('Invalid Command, where do you want the piece to move i.e e6: ')
    return pieceToMove, moveTo
#_______________________________________________________________________________  
def convertToList(a):
    moveCommand = []
    for i in range(len(a)):
        moveCommand.append(str(a[i]))
    while ' ' in moveCommand:
        moveCommand.remove(' ')
    return moveCommand
#_______________________________________________________________________________ 
def convertToCoordinates(a):
    coordinates = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    dictOfCoordinates = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7}
    if len(a) == 2:
        if a[0] in dictOfCoordinates:
            b = dictOfCoordinates[str(a[0])]
        pieceAndCoordinates = [int(a[1]) -1, int(b)]
    if len(a) == 3:
        if a[1] in coordinates:
            b = dictOfCoordinates[str(a[1])]
        pieceAndCoordinates = [a[0], int(a[2]) -1, int(b)]
    return pieceAndCoordinates
    
#_______________________________________________________________________________
def isEmpty(b,x,y):
    if b[x][y] == '0':
        return True
    return False
#_______________________________________________________________________________
def piecePresent(b,x,y):
    if b[x][y] != 0:
        return b[x][y]
#_______________________________________________________________________________
def WhitepawnMoves(b, x, y, moveToX, moveToY):
    piecesWhite = ['P', 'R', 'B', 'N', 'K', 'Q']
    piecesBlack = ['p','r', 'b', 'n', 'k', 'q']
    if [moveToX, moveToY] == [x+1, y] and isEmpty(b,moveToX,moveToY):
        b[x][y] = '0'
        b[moveToX][moveToY] = 'P'
        return b
    if piecePresent(b,x+1,y+1) in piecesBlack and [moveToX, moveToY] == [x+1, y+1]:
        b[x][y] = '0'
        b[moveToX][moveToY] = 'p'
        return b
    if piecePresent(b,x+1,y-1) in piecesBlack and [moveToX, moveToY] == [x+1, y-1]:
        b[x][y] = '0'
        b[moveToX][moveToY] = 'p'
        return b
    if x == 1 and [moveToX, moveToY] == [x+2, y] and isEmpty(b,moveToX,moveToY):
        b[x][y] = '0'
        b[moveToX][moveToY] = 'p'
        return b
    return 'Invalid move'
#_______________________________________________________________________________
def BlackpawnMoves(b, x, y, moveToX, moveToY):
    piecesWhite = ['P', 'R', 'B', 'N', 'K', 'Q']
    piecesBlack = ['p','r', 'b', 'n', 'k', 'q']
    if [moveToX, moveToY] == [x - 1, y] and isEmpty(b,moveToX,moveToY):
        b[x][y] = '0'
        b[moveToX][moveToY] = 'p'
        print b
        return b
    if piecePresent(b,x-1,y+1) in piecesWhite and [moveToX, moveToY] == [x-1, y+1]:
        b[x][y] = '0'
        b[moveToX][moveToY] = 'p'
        return b
    if piecePresent(b,x-1,y-1) in piecesWhite and [moveToX, moveToY] == [x-1, y-1]:
        b[x][y] = '0'
        b[moveToX][moveToY] = 'p'
        print b
        return b
    if x == 6 and [moveToX, moveToY] == [x - 2, y] and isEmpty(b,moveToX,moveToY):
        b[x][y] = '0'
        b[moveToX][moveToY] = 'p'
        print b
        return b
    return 'Invalid move'
#_______________________________________________________________________________
def BlackkingMoves(b, x, y, moveToX, moveToY):
    piecesWhite = ['P', 'R', 'B', 'N', 'K', 'Q']
    piecesBlack = ['p','r', 'b', 'n', 'k', 'q']
    if [moveToX,moveToY] == [x+1,y] and isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite and [moveToX,moveToY] == [x+1,y]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x-1,y] and isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite and [moveToX,moveToY] == [x-1,y]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x+1,y+1] and isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite and [moveToX,moveToY] == [x+1,y+1]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x+1,y-1] and isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite and [moveToX,moveToY] == [x+1,y-1]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x-1,y+1] and isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite and [moveToX,moveToY] == [x-1,y+1]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x-1,y-1] and isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite and [moveToX,moveToY] == [x-1,y-1]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x,y+1] and isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite and [moveToX,moveToY] == [x,y+1]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
    if [moveToX,moveToY] == [x,y-1] and isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite and [moveToX,moveToY] == [x,y-1]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    return 'Invalid Move'
#_______________________________________________________________________________
def whiteKingMoves(b, x, y, moveToX, moveToY):
    piecesWhite = ['P', 'R', 'B', 'N', 'K', 'Q']
    piecesBlack = ['p','r', 'b', 'n', 'k', 'q']
    if [moveToX,moveToY] == [x+1,y] and isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack and [moveToX,moveToY] == [x+1,y]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x-1,y] and isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack and [moveToX,moveToY] == [x-1,y]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x+1,y+1] and isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack and [moveToX,moveToY] == [x+1,y+1]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x+1,y-1] and isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack and [moveToX,moveToY] == [x+1,y-1]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x-1,y+1] and isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack and [moveToX,moveToY] == [x-1,y+1]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x-1,y-1] and isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack and [moveToX,moveToY] == [x-1,y-1]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x,y+1] and isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack and [moveToX,moveToY] == [x,y+1]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
    if [moveToX,moveToY] == [x,y-1] and isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack and [moveToX,moveToY] == [x,y-1]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    return 'Invalid Move'
#_______________________________________________________________________________
def whiteRookMoves(b, x, y, moveToX, moveToY):
    piecesWhite = ['P', 'R', 'B', 'N', 'K', 'Q']
    piecesBlack = ['p','r', 'b', 'n', 'k', 'q']
    a = x
    c = y
    solutionMoves = []
    for j in range(8):
        if j != x:
            solutionMoves.append([j, y])

    for i in range(8):
        if i != y:
           solutionMoves.append([x, i])
    if [moveToX, moveToY] in solutionMoves:
        if moveToX == a:
            print 'yes'
            if moveToY > c:
                while isEmpty(b, x, y+1) and (y+1) < moveToY :
                    print 'hello'
                    y += 1
                if y+1 < moveToY:
                    return "Invalid Move"
                if isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack:
                    temp = b[a][c]
                    b[a][c] = '0'
                    b[moveToX][moveToY] = temp
                    return b
            if moveToY < c:
                while isEmpty(b, x, y-1) and (y-1) > moveToY :
                    print 'aaaaa'
                    y -= 1
                if y-1 > moveToY:
                    return "Invalid Move"
                if isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack:
                    temp = b[a][c]
                    b[a][c] = '0'
                    b[moveToX][moveToY] = temp
                    return b
        if moveToY == c:
            if moveToX > a:
                while isEmpty(b, x + 1, y) and (x+1) < moveToX:
                    x += 1
                if x+1 < moveToX:
                    return "Invalid Move"
                if isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack:
                    temp = b[a][c]
                    b[a][c] = '0'
                    b[moveToX][moveToY] = temp
                    return b
            if moveToX < a:
                while isEmpty(b, x - 1, y) and (x-1) > moveToX:
                    x += 1
                if x-1 > moveToX:
                    return "Invalid Move"
                if isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack:
                    temp = b[a][c]
                    b[a][c] = '0'
                    b[moveToX][moveToY] = temp
                    return b
#_______________________________________________________________________________
def blackRookMoves(b, x, y, moveToX, moveToY):
    piecesWhite = ['P', 'R', 'B', 'N', 'K', 'Q']
    piecesBlack = ['p','r', 'b', 'n', 'k', 'q']
    a = x
    b = y
    solutionMoves = []
    for j in range(8):
        if j != x:
            solutionMoves.append([j, y])

    for i in range(8):
        if i != y:
           solutionMoves.append([x, i])
    if [moveToX, moveToY] in solutionMoves:
        if moveToX == a:
            print 'yes'
            if moveToY > c:
                while isEmpty(b, x, y+1) and (y+1) < moveToY :
                    print 'hello'
                    y += 1
                if y+1 < moveToY:
                    return "Invalid Move"
                if isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite:
                    temp = b[a][c]
                    b[a][c] = '0'
                    b[moveToX][moveToY] = temp
                    return b
            if moveToY < c:
                while isEmpty(b, x, y-1) and (y-1) > moveToY :
                    print 'aaaaa'
                    y -= 1
                if y-1 > moveToY:
                    return "Invalid Move"
                if isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite:
                    temp = b[a][c]
                    b[a][c] = '0'
                    b[moveToX][moveToY] = temp
                    return b
        if moveToY == c:
            if moveToX > a:
                while isEmpty(b, x + 1, y) and (x+1) < moveToX:
                    x += 1
                if x+1 < moveToX:
                    return "Invalid Move"
                if isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite:
                    temp = b[a][c]
                    b[a][c] = '0'
                    b[moveToX][moveToY] = temp
                    return b
            if moveToX < a:
                while isEmpty(b, x - 1, y) and (x-1) > moveToX:
                    x += 1
                if x-1 > moveToX:
                    return "Invalid Move"
                if isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite:
                    temp = b[a][c]
                    b[a][c] = '0'
                    b[moveToX][moveToY] = temp
                    return b

#_______________________________________________________________________________
def blackBishopMoves(b, x, y, moveToX, moveToY):
    piecesWhite = ['P', 'R', 'B', 'N', 'K', 'Q']
    piecesBlack = ['p','r', 'b', 'n', 'k', 'q']
    a = x
    c = y
    solutionMoves = []
    while x+1>=0 and x+1<=8 and y+1>=0 and y+1<=8:
        x += 1
        y += 1
        solutionMoves.append([x,y])
    x = a
    y = c
    while x-1>=0 and x-1<=8 and y-1>=0 and y-1<=8:
        x -= 1
        y -= 1
        solutionMoves.append([x,y])
    x = a
    y = c
    while x+1>=0 and x+1<=8 and y-1>=0 and y-1<+8:
        x += 1
        y -= 1
        solutionMoves.append([x,y])
    x = a
    y = c    
    while x-1>=0 and x-1<=8 and y+1>=0 and y-1<8:
        x -= 1
        y += 1
        solutionMoves.append([x,y])
    x = a
    y = c
    if [moveToX, moveToY] in solutionMoves:
        if moveToX > a and moveToY >c:
            while isEmpty(b, x+1, y+1) and (y+1) < moveToY and (x+1) < moveToX:
                y += 1
                x += 1
            if y+1 < moveToY or (x+1) < moveToX:
                return "Invalid Move"
            if isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite:
                temp = b[a][c]
                b[a][c] = '0'
                b[moveToX][moveToY] = temp
                return b
        if moveToX < a and moveToY <c:
            while isEmpty(b, x - 1, y - 1) and (x - 1) > moveToX and (y - 1) > moveToY:
                x -= 1
                y -= 1
            if (x - 1) > moveToX or (y - 1) > moveToY:
                return "Invalid Move"
            if isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite:
                temp = b[a][c]
                b[a][c] = '0'
                b[moveToX][moveToY] = temp
                return b
        if moveToX < a and moveToY >c:
            while isEmpty(b, x - 1, y + 1) and (x - 1) > moveToX and (y + 1) < moveToY:
                x -= 1
                y += 1
            if (x - 1) > moveToX or (y + 1) < moveToY:
                return "Invalid Move"
            if isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite:
                temp = b[a][c]
                b[a][c] = '0'
                b[moveToX][moveToY] = temp
                return b
        if moveToX > a and moveToY <c:
            while isEmpty(b, x + 1, y - 1) and (x + 1) < moveToX and (y - 1) > moveToY:
                x += 1
                y -= 1
            if (x + 1) < moveToX or (y - 1) > moveToY:
                return "Invalid Move"
            if isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite:
                temp = b[a][c]
                b[a][c] = '0'
                b[moveToX][moveToY] = temp
                return b

#_______________________________________________________________________________
def whiteBishopMoves(b, x, y, moveToX, moveToY):
    piecesWhite = ['P', 'R', 'B', 'N', 'K', 'Q']
    piecesBlack = ['p','r', 'b', 'n', 'k', 'q']
    a = x
    c = y
    solutionMoves = []
    while x+1>=0 and x+1<=8 and y+1>=0 and y+1<=8:
        x += 1
        y += 1
        solutionMoves.append([x,y])
    x = a
    y = c
    while x-1>=0 and x-1<=8 and y-1>=0 and y-1<=8:
        x -= 1
        y -= 1
        solutionMoves.append([x,y])
    x = a
    y = c
    while x+1>=0 and x+1<=8 and y-1>=0 and y-1<+8:
        x += 1
        y -= 1
        solutionMoves.append([x,y])
    x = a
    y = c    
    while x-1>=0 and x-1<=8 and y+1>=0 and y-1<8:
        x -= 1
        y += 1
        solutionMoves.append([x,y])
    x = a
    y = c
    if [moveToX, moveToY] in solutionMoves:
        if moveToX > a and moveToY >c:
            print 'alpha'
            while isEmpty(b, x+1, y+1) and (y+1) < moveToY and (x+1) < moveToX:
                y += 1
                x += 1
            if y+1 < moveToY or (x+1) < moveToX:
                return "Invalid Move"
            if isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack:
                temp = b[a][c]
                b[a][c] = '0'
                b[moveToX][moveToY] = temp
                return b
        if moveToX < a and moveToY <c:
            print 'alpha'
            while isEmpty(b, x - 1, y - 1) and (x - 1) > moveToX and (y - 1) > moveToY:
                x -= 1
                y -= 1
            if (x - 1) > moveToX or (y - 1) > moveToY:
                return "Invalid Move"
            if isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack:
                temp = b[a][c]
                b[a][c] = '0'
                b[moveToX][moveToY] = temp
                return b
        if moveToX < a and moveToY >c:
            print 'alpha'
            while isEmpty(b, x - 1, y + 1) and (x - 1) > moveToX and (y + 1) < moveToY:
                x -= 1
                y += 1
            if (x - 1) > moveToX or (y + 1) < moveToY:
                return "Invalid Move"
            if isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack:
                temp = b[a][c]
                b[a][c] = '0'
                b[moveToX][moveToY] = temp
                return b
        if moveToX > a and moveToY <c:
            print 'alpha'
            while isEmpty(b, x + 1, y - 1) and (x + 1) < moveToX and (y - 1) > moveToY:
                x += 1
                y -= 1
            if (x + 1) < moveToX or (y - 1) > moveToY:
                return "Invalid Move"
            if isEmpty(b,moveToX,moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack:
                temp = b[a][c]
                b[a][c] = '0'
                b[moveToX][moveToY] = temp
                return b

#_______________________________________________________________________________
def whiteQueenMoves(b, x, y, moveToX, moveToY):
    whiteBishopMoves(b, x, y, moveToX, moveToY)
    whiteRookMoves(b, x, y, moveToX, moveToY)
    
    
#_______________________________________________________________________________
def blackQueenMoves(b, x, y, moveToX, moveToY):
    blackBishopMoves(b, x, y, moveToX, moveToY)
    blackRookMoves(b, x, y, moveToX, moveToY)
#_______________________________________________________________________________
def whiteknightMoves(b, x, y, moveToX, moveToY):
    piecesWhite = ['P', 'R', 'B', 'N', 'K', 'Q']
    piecesBlack = ['p','r', 'b', 'n', 'k', 'q']
    if [moveToX,moveToY] == [x+1,y+2] and isEmpty(b,moveToX, moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack and [moveToX,moveToY] == [x+1,y+2]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x+1,y-2] and isEmpty(b,moveToX, moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack and [moveToX,moveToY] == [x+1,y-2]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x+2,y+1] and isEmpty(b,moveToX, moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack and [moveToX,moveToY] == [x+2,y+1]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x+2,y-1] and isEmpty(b,moveToX, moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack and [moveToX,moveToY] == [x+2,y-1]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x-1,y+2] and isEmpty(b,moveToX, moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack and [moveToX,moveToY] == [x-1,y+2]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x-1,y-2] and isEmpty(b,moveToX, moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack and [moveToX,moveToY] == [x-1,y-2]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x-2,y+1] and isEmpty(b,moveToX, moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack and [moveToX,moveToY] == [x-2,y+1]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x-2,y-1] and isEmpty(b,moveToX, moveToY) or piecePresent(b,moveToX, moveToY) in piecesBlack and [moveToX,moveToY] == [x-2,y-1]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    return True
#_______________________________________________________________________________
def blackknightMoves(b, x, y, moveToX, moveToY):
    piecesWhite = ['P', 'R', 'B', 'N', 'K', 'Q']
    piecesBlack = ['p','r', 'b', 'n', 'k', 'q']
    if [moveToX,moveToY] == [x+1,y+2] and isEmpty(b,moveToX, moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite and [moveToX,moveToY] == [x+1,y+2]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x+1,y-2] and isEmpty(b,moveToX, moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite and [moveToX,moveToY] == [x+1,y-2]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x+2,y+1] and isEmpty(b,moveToX, moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite and [moveToX,moveToY] == [x+2,y+1]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x+2,y-1] and isEmpty(b,moveToX, moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite and [moveToX,moveToY] == [x+2,y-1]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x-1,y+2] and isEmpty(b,moveToX, moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite and [moveToX,moveToY] == [x-1,y+2]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x-1,y-2] and isEmpty(b,moveToX, moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite and [moveToX,moveToY] == [x-1,y-2]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x-2,y+1] and isEmpty(b,moveToX, moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite and [moveToX,moveToY] == [x-2,y+1]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    if [moveToX,moveToY] == [x-2,y-1] and isEmpty(b,moveToX, moveToY) or piecePresent(b,moveToX, moveToY) in piecesWhite and [moveToX,moveToY] == [x-2,y-1]:
        temp = b[x][y]
        b[x][y] = '0'
        b[moveToX][moveToY] = temp
        return b
    return True
#_______________________________________________________________________________
def movePiece(b,whereToMove, fromWhereToMove):
    piece = fromWhereToMove[0]
    if piece == 'p':
        BlackpawnMoves(b,fromWhereToMove[1], fromWhereToMove[2], whereToMove[0], whereToMove[1])
    if piece == 'P':
        WhitepawnMoves(b,fromWhereToMove[1], fromWhereToMove[2], whereToMove[0], whereToMove[1])
    if piece == 'K':
        whiteKingMoves(b,fromWhereToMove[1], fromWhereToMove[2], whereToMove[0], whereToMove[1])
    if piece == 'k':
        BlackkingMoves(b,fromWhereToMove[1], fromWhereToMove[2], whereToMove[0], whereToMove[1])
    if piece == 'N':
        whiteknightMoves(b,fromWhereToMove[1], fromWhereToMove[2], whereToMove[0], whereToMove[1])
    if piece == 'n':
        blackknightMoves(b,fromWhereToMove[1], fromWhereToMove[2], whereToMove[0], whereToMove[1])
    if piece == 'B':
        whiteBishopMoves(b,fromWhereToMove[1], fromWhereToMove[2], whereToMove[0], whereToMove[1])
    if piece == 'b':
        blackBishopMoves(b,fromWhereToMove[1], fromWhereToMove[2], whereToMove[0], whereToMove[1])
    if piece == 'R':
        whiteRookMoves(b,fromWhereToMove[1], fromWhereToMove[2], whereToMove[0], whereToMove[1])
    if piece == 'r':
        blackRookMoves(b,fromWhereToMove[1], fromWhereToMove[2], whereToMove[0], whereToMove[1])
    if piece == 'q':
        blackQueenMoves(b,fromWhereToMove[1], fromWhereToMove[2], whereToMove[0], whereToMove[1])
    if piece == 'Q':
        whiteQueenMoves(b,fromWhereToMove[1], fromWhereToMove[2], whereToMove[0], whereToMove[1])
    printBoard(b)
#_______________________________________________________________________________
def checkMate():
    return True
#_______________________________________________________________________________
def castling():
    return True
#_______________________________________________________________________________
def draw():
    return True
#_______________________________________________________________________________

#_______________________________________________________________________________

piecesWhite = ['P', 'R', 'B', 'N', 'K', 'Q']
piecesBlack = ['p','r', 'b', 'n', 'k', 'q']

b = [['R','N','B','Q','K','B','N','R'],
     ['P','P','P','P','P','P','P','P'],
     ['0','0','0','0','0','0','0','0'],
     ['0','0','0','0','0','0','0','0'],
     ['0','0','0','0','0','0','0','0'],
     ['0','0','0','0','0','0','0','0'],
     ['p','p','p','p','p','p','p','p'],
     ['r','n','b','q','k','b','n','r']]
printBoard(b)
for i in range(50):
    fromp, to = takeInput()
    listOfPieceCoordinates = convertToCoordinates(convertToList(fromp))
    listOfEndCoordinates = convertToCoordinates(convertToList(to))
    movePiece(b,listOfEndCoordinates, listOfPieceCoordinates)

