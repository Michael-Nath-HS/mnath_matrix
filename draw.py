from display import *
from matrix import *
from math import sin, cos, pi

def rotate_point(point, theta, origin_x, origin_y):
    point[0], point[1] = (
        ((point[0] - origin_x) * cos(theta)) - ((point[1] - origin_y) * sin(theta))
    ) + origin_x, ((point[1] - origin_y) * cos(theta)) + ((point[0] - origin_x) * sin(theta)) + origin_y
    return point
    
def draw_circle(center_x, center_y, radius, screen, color):
    prev = [center_x, center_y + radius]
    edges = new_matrix()
    theta = 0
    while (theta < 2 * pi):
        theta += pi / 180;
        new_point = rotate_point(prev.copy(), theta, center_x, center_y)
        new_point[0] = round(new_point[0])
        new_point[1] = round(new_point[1])
        add_edge(edges, prev[0], prev[1], 0, new_point[0], new_point[1], 0)
        prev = new_point
    draw_lines(edges, screen, color)

def draw_lines( matrix, screen, color ):
    num_cols = len(matrix[0])
    for i in range(0, num_cols, 2):
        x0 = matrix[0][i]
        x1 = matrix[0][i+1]
        y0 = matrix[1][i]
        y1 = matrix[1][i+1]
        draw_line(x0, y0, x1, y1, screen, color)

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)
    pass

def add_point( matrix, x, y, z=0 ):
    matrix[0].append(x)
    matrix[1].append(y)
    matrix[2].append(z)
    matrix[3].append(1)

def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:            
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
