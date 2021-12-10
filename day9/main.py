import collections
import sys


cord = []
cord2=[]

def check_edge(matrix,index,l_l,l_m):

    if index == (0,0):
        if matrix[0][0] < matrix[0][1] and matrix[0][0]< matrix[1][0]:
            return True
    elif index == (0,l_l-1):
        if  matrix[0][l_l-2] > matrix [0][l_l-1] < matrix[1][l_l-1]:
            return True

    elif index == (l_m-1,0):
        if matrix[l_m-2][0] >  matrix[l_m-1][0] <  matrix[l_m-1][1]:
            return True
    elif index == (l_m-1,l_l-1):
        if matrix[l_m-1][l_l-2] > matrix[l_m-1][l_l-1] < matrix[l_m-2][l_l-1]:
            return True

    elif index[0] == 0:
        x = index[0]
        y = index[1]
        curr = matrix[x][y]
        if curr < matrix[x][y-1] and curr < matrix[x+1][y] and curr < matrix[x][y+1]:
            return True

    elif index[0] == l_m-1:
        x = index[0]
        y = index[1]
        curr = matrix[x][y]
        if curr < matrix[x][y-1] and curr < matrix[x][y+1] and curr < matrix[x-1][y]:
            return True


    elif index[1]==l_l-1:
        x= index[0]
        y= index[1]
        curr = matrix[x][y]
        if curr < matrix[x-1][y] and curr < matrix[x+1][y] and curr < matrix[x][y-1]:
            return True

    elif index[1] == 0:
        x= index[0]
        y= index[1]
        curr = matrix[x][y]
        if curr < matrix[x-1][y] and curr < matrix[x+1][y] and curr < matrix[x][y+1]:
            return True

    else:
        x= index[0]
        y= index[1]
        curr = matrix[x][y]
        if curr < matrix[x][y-1] and curr < matrix[x][y+1] and curr < matrix[x+1][y] and curr < matrix[x-1][y]:
            return True

    return False










def sol1():

    with open("input.txt","r") as f:

        matrix =[ [int(i) for i in line] for line in f.read().splitlines()]

        len_matrix = len(matrix)
        len_line = len(matrix[0])
        print(len_matrix,len_line)

        count = 0
        score  = 0
        for i in range(len_matrix):
            for j in range(len_line):
                if check_edge(matrix,(i,j),l_l=len_line,l_m=len_matrix):
                    cord.append((i,j))
                    score += (matrix[i][j]+1)
        print(score)


            



sol1()


#solution from asottile
def sol1_an():
    coords = collections.defaultdict(lambda: sys.maxsize)
    
    with open("input.txt","r") as f:
        s=f.read()


    lines = s.splitlines()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            coords[(y, x)] = int(c)


        

    total = 0
    for (y, x), n in tuple(coords.items()):
        if (
            coords[y, x + 1] > n and
            coords[y, x - 1] > n and
            coords[y + 1, x] > n and
            coords[y - 1, x] > n
        ):
            total += n + 1
            cord2.append((y,x))

    print(total)


def check_edge_nine(matrix,index,l_l,l_m):

    if index == (0,0):
            matrix[0][1]!=9 and 9!= matrix[1][0]:
            return True
    elif index == (0,l_l-1):
        if  matrix[0][l_l-2] !=9 and 9 != matrix[1][l_l-1]:
            return True

    elif index == (l_m-1,0):
        if matrix[l_m-2][0]!=9 and 9 !=  matrix[l_m-1][1]:
            return True
    elif index == (l_m-1,l_l-1):
        if matrix[l_m-1][l_l-2] !=9 and 9!= matrix[l_m-2][l_l-1]:
            return True

    elif index[0] == 0:
        x = index[0]
        y = index[1]
        curr = matrix[x][y]
        if 9 != matrix[x][y-1] and 9 != matrix[x+1][y] and 9 != matrix[x][y+1]:
            return True

    elif index[0] == l_m-1:
        x = index[0]
        y = index[1]
        curr = matrix[x][y]
        if 9 != matrix[x][y-1] and 9 != matrix[x][y+1] and 9 != matrix[x-1][y]:
            return True


    elif index[1]==l_l-1:
        x= index[0]
        y= index[1]
        curr = matrix[x][y]
        if 9 != matrix[x-1][y] and 9 != matrix[x+1][y] and 9 != matrix[x][y-1]:
            return True

    elif index[1] == 0:
        x= index[0]
        y= index[1]
        curr = matrix[x][y]
        if 9 != matrix[x-1][y] and 9 != matrix[x+1][y] and 9 != matrix[x][y+1]:
            return True

    else:
        x= index[0]
        y= index[1]
        curr = matrix[x][y]
        if 9 != matrix[x][y-1] and 9 != matrix[x][y+1] and 9 != matrix[x+1][y] and 9 != matrix[x-1][y]:
            return True

    return False

def sol2():

     with open("input.txt","r") as f:

            matrix =[ [int(i) for i in line] for line in f.read().splitlines()]

            len_matrix = len(matrix)
            len_line = len(matrix[0])
            print(len_matrix,len_line)

            count = 0
            score  = 0
            for i in range(len_matrix):
                for j in range(len_line):
                    seen = set()
                    stack=[(i,j)]

                    while stack:
                        if check_edge(matrix,(i,j),l_l=len_line,l_m=len_matrix):
                            cord.append((i,j))
                            score += (matrix[i][j]+1)
            print(score)



