def isSafe(Map, i, j, visited): 
    return (i >= 0 and i < N and 
            j >= 0 and j < M and 
            not visited[i][j] and Map[i][j] != '#') 

def DFS(Map, i, j, visited, factions, foundFactions):
    rowNbr = [-1, 0, 0, 1]
    colNbr = [0, -1, 1, 0]
    
    stack = [[i,j]]
    while stack:
        loc = stack.pop()         # loc = [i,j]
        visited[loc[0]][loc[1]] = True
        if Map[loc[0]][loc[1]] in factions:
            foundFactions.append(Map[loc[0]][loc[1]])
        
        for k in range(4):
            next_i = loc[0] + rowNbr[k]
            next_j = loc[1] + colNbr[k]
            if isSafe(Map, next_i, next_j, visited) and ([next_i, next_j] not in stack):
                stack.append([loc[0] + rowNbr[k], loc[1] + colNbr[k]])

def FactionSearch(Map, N, M): 
    visited = [[False for j in range(M)]for i in range(N)] 
    
    factions = sorted({l for word in Map for l in word})
    factions = [l for l in factions if l!='#' and l!='.']
    factions.append('contested')
    dictFactions = dict((l,0) for l in factions)
    
    for i in range(N): 
        for j in range(M): 
            foundFactions = []
            
            if visited[i][j] == False and (Map[i][j] != '#'): 
                DFS(Map, i, j, visited, factions, foundFactions) 
                
                foundFactions = sorted(set(foundFactions))
                
                if len(foundFactions) > 1:
                    dictFactions['contested'] +=1
                if len(foundFactions) == 1:
                    dictFactions[foundFactions[0]] += 1
  
    return dictFactions
	
file = open("input3.in", "r")
out  = open("output3.in", "w")

T = int(file.readline().strip('\n'))

for CaseNumber in range(1,T+1):
    N = int(file.readline().strip('\n'))   
    M = int(file.readline().strip('\n'))   
    
    Map = []
    for i in range(N):
        Map.append(file.readline().strip('\n'))
    
    dictFactions = FactionSearch(Map, N, M)
    
    dictFactions = {k:v for k,v in dictFactions.items() if v!=0 or k=='contested'}
    
    out.write('Case ' + str(CaseNumber) + ':' + '\n')
    if CaseNumber != T:
        for k,v in dictFactions.items():
            out.write(k + ' ' + str(v) + '\n')
    else:
        i = 1
        for k,v in dictFactions.items():
            if i != len(dictFactions):
                out.write(k + ' ' + str(v) + '\n')
            else:
                out.write(k + ' ' + str(v))
            i = i + 1

file.close()
out.close()