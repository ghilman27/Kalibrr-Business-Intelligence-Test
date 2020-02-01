def direction(i,j,height,width,wordLength):
    xchange = [-1, 0, 1, -1, 1, -1, 0, 1]
    ychange = [-1, -1, -1, 0, 0, 1, 1, 1]
    
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

def WordSearch(grid, word):
    height = len(grid)
    width = len(grid[0])
    wordLength = len(word)
    
    sum = 0
    for init_i in range(height):
        for init_j in range(width):
            xchange, ychange = direction(init_i, init_j, height, width, wordLength)
            n_posDir = len(xchange)
            
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

file = open("input2.in", "r")
out  = open("output2.in", "w")

T = int(file.readline().strip('\n'))

for CaseNumber in range(1,T+1):
    N = int(file.readline().strip('\n'))
    M = int(file.readline().strip('\n'))
    
    wordGrid = []
    for i in range(N):
        wordGrid.append(file.readline().strip('\n'))
    
    word = file.readline().strip('\n')
    jumlah = WordSearch(wordGrid, word)

    if CaseNumber != T:
        out.write('Case ' + str(CaseNumber) + ': ' + str(jumlah) + '\n')
    else:
        out.write('Case ' + str(CaseNumber) + ': ' + str(jumlah))

file.close()
out.close()