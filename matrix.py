# This is module for some vector and matrix operations

# dot product of 2 vectors
def dot(v1, v2):
    if (len(v1)!=len(v2)):
        return None
    else:
        res = 0
        for i in range(len(v1)):
            res += v1[i]*v2[i]
        return res

# get matrix with R rows and C columns,
# elements of which are all equal to 0
def zeros(r,c):
    mat = []
    for i in range(r):
        row = []
        for j in range(c):
            row += [0]
        mat += [row]
    return mat

# get matrix with R rows and C columns,
# elements of which are all equal to 1

def ones(r,c):
    mat = []
    for i in range(r):
        row = []
        for j in range(c):
            row += [1]
        mat += [row]
    return mat

# get matrix with R rows and C columns,
# elements of which are all equal to 0, except the
# diagonal elements, which are equal to 1

def eye(r,c):
    mat = []
    for i in range(r):
        row = []
        for j in range(c):
            if (i==j):
                row +=[1]
            else:
                row += [0]
        mat += [row]
    return mat


# turn your array into matrix (R by C), if number of elements is enough
def mat(r,c,arr):
    if (r*c != len(arr)):
        return None
    else:
        mat = []
        k = 0
        for i in range(r):
            row = []
            for j in range(c):
                row += [arr[k]]
                k += 1
            mat += [row]
        return mat

# transpose matrix
def transp(mat):
    c = len(mat)
    r = len(mat[0])
    tran = []
    for i in range(r):
        row = []
        for j in range(c):
            row += [mat[j][i]]
        tran += [row]
    return tran

# find the determinant of square matrix
def det(mat):
    r = len(mat)
    c = len(mat[0])
    d = 0
    if ( r != c ):
        return None
    elif (r==2 and c==2):
        return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
    else:
        for i in range(r):
            m = 1
            for j in range(c):
                x = j
                y = (i + j)%r
                m *= mat[x][y]
            d += m
        for i in range(r):
            m = 1
            for j in range(c):
                x = j
                y = (3 - i - j) % r
                m *= mat[x][y]
            d -= m
        return d

# multiply all elements of matrix by a number
def matByNum(mat,num):
    r = len(mat)
    c = len(mat[0])
    for i in range(r):
        for j in range(c):
            mat[i][j] *= num
    return mat

# cross product of 2 vectors with 3 elements each
def cross3(v1,v2):
    v3 = []
    if (len(v1)!= 3 or len(v2)!= 3):
        return None
    else:
        v3 += [  det( [ [v1[1],v1[2]] , [v2[1],v2[2]] ] )  ]
        v3 += [  (-1)*det( [ [v1[0],v1[2]] , [v2[0],v2[2]] ] )  ]
        v3 += [  det( [ [v1[0],v1[1]] , [v2[0],v2[1]] ] )  ]
    return v3


print(dot([2,2,0],[2,-2,0]))

