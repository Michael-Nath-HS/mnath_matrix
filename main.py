from display import *
from draw import *
from matrix import *
screen = new_screen()
color = [ 75,112,221 ]

m2 = new_matrix(4, 0)
m1 = new_matrix()
# Testing add_edge()
print("Testing add_edge: Adding Edges (1,2,3), (4,5,6) to matrix m2...")
add_edge(m2, 1, 2, 3, 4, 5, 6)
print()
# Testing ident()
print("Testing ident(): Transforming Matrix m1 to Identity Matrix...")
ident(m1)
print_matrix(m1)
print()

#Testing matrix_mult():
print("Testing matrix_mult(): Multiplying m1 x m2")
matrix_mult(m1, m2)
print_matrix(m2)
print()

m1 = new_matrix(4, 0)
# Testing matrix_mult() again:
print("m1:")
add_edge(m1, 1, 2, 3, 4, 5, 6)
add_edge(m1, 7, 8, 9, 10, 11, 12)
print_matrix(m1)
print()
print("Multiplying m1 x m2")
matrix_mult(m1, m2)
print_matrix(m2)
print()

# drawing neptune
draw_circle(260, 230, 200, screen, color)

# drawing triton
color = [240, 228, 204]
draw_circle(70, 430, 50, screen, color)
display(screen)