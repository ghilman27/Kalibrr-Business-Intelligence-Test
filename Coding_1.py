# ------------- DEFINE FUNCTION ---------------
def div3(A,B,K):
    value = A
    sum = 0
    while value <= B:
        if value%K == 0:
            sum = sum + 1  
        value = value + 1
    return sum

# ------------- DEFINE INPUT AND OUTPUT ----------------
file = open("input1.in", "r")
out  = open("output1.in", "w")

# ----------- THE MAIN PROGRAM ----------------------
j = 1
N = int(file.readline().strip('\n'))

while j <= N:
    A = int(file.readline().strip('\n'))
    B = int(file.readline().strip('\n'))
    K = int(file.readline().strip('\n'))
    sum = div3(A,B,K)
    if j != N:
        out.write('Case ' + str(j) + ': ' + str(sum) + '\n')
    else:
        out.write('Case ' + str(j) + ': ' + str(sum))
    j = j+1
file.close()
out.close()