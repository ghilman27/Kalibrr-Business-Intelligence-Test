# DISCLAIMER
# Created by ghilman27

# Function to determine whether a block should be visited or not
def isSafe(Map, i, j, visited): 
    return (i >= 0 and i < N and 
            j >= 0 and j < M and 
            not visited[i][j] and Map[i][j] != '#') 

# DFS Function			
def DFS(Map, i, j, visited, factions, foundFactions):
    rowNbr = [-1, 0, 0, 1]
    colNbr = [0, -1, 1, 0]
    
	# I'm using "stack" for iteration, cause python has recursive limit
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

## MAIN FUNCTION
#  Function for searching and counting number of factions				
def FactionSearch(Map, N, M): 
	# Initially all cells are unvisited 
    visited = [[False for j in range(M)]for i in range(N)] 
    
	# Create factions dictionary
    factions = sorted({l for word in Map for l in word})
    factions = [l for l in factions if l!='#' and l!='.']
    factions.append('contested')
    dictFactions = dict((l,0) for l in factions)
    
	# Count how many region ruled by every factions
    for i in range(N): 
        for j in range(M): 
			# initially no factions found in the region
            foundFactions = []
            
			# If a cell with value != # is not visited yet, then a new region is found
            if visited[i][j] == False and (Map[i][j] != '#'): 
				# Visit all cells in this region
                DFS(Map, i, j, visited, factions, foundFactions) 
                
				# found distinct factions who rule this region
                foundFactions = sorted(set(foundFactions))
                
				# if > 1 factions rule, this is a contested region
                if len(foundFactions) > 1:
                    dictFactions['contested'] +=1
				# if only 1 faction rules, this region belongs to that faction
                if len(foundFactions) == 1:
                    dictFactions[foundFactions[0]] += 1
  
    return dictFactions

## MAIN PROGRAM

# INPUT	
file = open("input3.in", "r")
out  = open("output3.in", "w")

# Cleaning the enter character
T = int(file.readline().strip('\n'))

# Main Program
for CaseNumber in range(1,T+1):
	# Row (N) and Column (M) Parameters
    N = int(file.readline().strip('\n'))   
    M = int(file.readline().strip('\n'))   
    
	# Create Grid
    Map = []
    for i in range(N):
        Map.append(file.readline().strip('\n'))
    
	# Apply function
    dictFactions = FactionSearch(Map, N, M)
    
	# Select factions that have a ruled region
    dictFactions = {k:v for k,v in dictFactions.items() if v!=0 or k=='contested'}
    
	# Output
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
