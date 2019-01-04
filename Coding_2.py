# DISCLAIMER
# Program by: Ghilman Al Fatih
# Not really a good code because of too much iteration

# ------------ DEFINE FUNCTION ------------

# Define a possible direction of box in grid height x width
def direction(i,j,height,width,wordLength):
    # Define Direction (xchanges, ychanges)
    # x (right+) (left-)
    # y (up-) (down+)
    # 0   1   2
    # 3 init  4
    # 5   6   7
    xchange = [-1, 0, 1, -1, 1, -1, 0, 1]
    ychange = [-1, -1, -1, 0, 0, 1, 1, 1]
    
    # Define possible direction
    vect = [0,1,2,3,4,5,6,7]
    if i==0  or (i-(wordLength-1)<0):
        vect = [x for x in vect if (x != 0) and (x != 1) and (x != 2)]
    if i==height-1 or (i+(wordLength-1)>height-1):
        vect = [x for x in vect if (x != 5) and (x != 6) and (x != 7)]
    if j==0 or (j-(wordLength-1)<0):
        vect = [x for x in vect if (x != 0) and (x != 3) and (x != 5)]
    if j==width-1 or (j+(wordLength-1)>width-1):
        vect = [x for x in vect if (x != 2) and (x != 4) and (x != 7)]
    
    xchange = [xchange[x] for x in vect]
    ychange = [ychange[x] for x in vect]
    
    return xchange, ychange

# Search how many distinct instance that a word found in a grid
# IF YOU INPUT PALINDROMES WORDS, IT WILL GIVE WRONG RESULT
def WordSearch(grid, word):
    # Dimension Parameters
    height = len(grid)
    width = len(grid[0])
    wordLength = len(word)
    
    # Iteration for counting 'sum'
    sum = 0
    for init_i in range(height):
        for init_j in range(width):
            xchange, ychange = direction(init_i, init_j, height, width, wordLength)
            n_posDir = len(xchange)
            
            # explanation for i and j
            # i is row (y direction), i+1 = i+ychange
            # j is column (x direction), j+1 = j+xchange
            for k in range(n_posDir):
                current_i = init_i
                current_j = init_j
                foundWord = ''
                for l in range(wordLength):
                    foundWord = foundWord + grid[current_i][current_j]
                    current_i = current_i + ychange[k]
                    current_j = current_j + xchange[k]
                if foundWord == word:
                    sum = sum + 1
    return sum

# ------------ DEFINE INPUT OUTPUT ------------ 
file = open("input2.in", "r")
out  = open("output2.in", "w")

# ------------ MAIN PROGRAM ------------ 
T = int(file.readline().strip('\n'))

for CaseNumber in range(1,T+1):
    # Row (N) and Column (M) Parameters
    N = int(file.readline().strip('\n'))
    M = int(file.readline().strip('\n'))
    
    # Create Grid
    wordGrid = []
    for i in range(N):
        wordGrid.append(file.readline().strip('\n'))
    
    # Word for search
    word = file.readline().strip('\n')
    
    jumlah = WordSearch(wordGrid, word)
    
    # Output
    if CaseNumber != T:
        out.write('Case ' + str(CaseNumber) + ': ' + str(jumlah) + '\n')
    else:
        out.write('Case ' + str(CaseNumber) + ': ' + str(jumlah))

file.close()
out.close()