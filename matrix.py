"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for row in matrix:
        for col in row:
            print(col, end=" ")
        print()

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    i = 0;
    for row in matrix:
        for col in range(len(row)):
            if col == i:
                row[col] = 1
            else:
                row[col] = 0
        i += 1
    return

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    # rows of m2 must be equal to the columns in m1
    if (len(m2) != len(m1[0])):
        raise ValueError("These matrices cannot be multiplied")
    m2_cols = len(m2[0])
    m1_rows = len(m1)
    ans = [[] for _ in range(m1_rows)]
    for i in range(m1_rows):
        row = m1[i]
        for j in range(m2_cols):
            arr = []
            for col in m2:
                arr.append(col[j])
            ans[i].append(dot(row, arr))
    for i in range(len(m2)):
        m2[i] = []
    for i in range(len(ans)):
        for j in range(len(ans[0])):
            m2[i].append(ans[i][j])
def dot(a1, a2):
    total = 0
    for i in range(len(a1)):
        total += (a1[i] * a2[i])
    return total
    


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( rows ):
        m.append( [] )
        for r in range( cols ):
            m[c].append( 0 )
    return m
