from math import floor
"""
As a visual aid, here is a matrix:
0,0  1,0  2,0  3,0  4,0  5,0  6,0  7,0  8,0  9,0  
0,1  1,1  2,1  3,1  4,1  5,1  6,1  7,1  8,1  9,1  
0,2  1,2  2,2  3,2  4,2  5,2  6,2  7,2  8,2  9,2  
0,3  1,3  2,3  3,3  4,3  5,3  6,3  7,3  8,3  9,3  
0,4  1,4  2,4  3,4  4,4  5,4  6,4  7,4  8,4  9,4  
0,5  1,5  2,5  3,5  4,5  5,5  6,5  7,5  8,5  9,5  
0,6  1,6  2,6  3,6  4,6  5,6  6,6  7,6  8,6  9,6  
0,7  1,7  2,7  3,7  4,7  5,7  6,7  7,7  8,7  9,7  
0,8  1,8  2,8  3,8  4,8  5,8  6,8  7,8  8,8  9,8  
0,9  1,9  2,9  3,9  4,9  5,9  6,9  7,9  8,9  9,9
"""

def spiral(matrix_size: int) -> None:
    """
    Given the size of a matrix, output the coordinates of a spiral pattern
    Args:
        matrix_size: int
    Returns:
        None (print statement)
    """
    x = -1
    y = 0
    x_direction = 1
    y_direction = 1
    # total runs depending on the matrix size
    runs = matrix_size * 2 - 1
    # initial distance is always the matrix size
    distance = matrix_size
    for run in range(1, runs + 1):
        floor_distance = floor(distance)
        for _ in range(floor_distance):
            # if the runs are odd, change the x value
            if run % 2 == 1:
                x += x_direction
            # if the runs are even, change the y value
            else:
                y += y_direction
            # print the results
            print(f"({x}, {y})")

        # changing the distance by -0.5 allows for the desired ditances when using math.floor(distance)
        # ex: matrix_size = 2 we want the distances to be 2, 1, 1
        distance -= .5
        # if run is odd, change sign of x
        if run % 2 == 1:
            x_direction *= -1
        # if run is even, change sign of y
        else:
            y_direction *= -1
    

# Change matrix_size for testing
matrix_size = 3
spiral(matrix_size)

# (method)  # (runs)-> (distances per run)
# spiral(1) # 1     -> 1
# spiral(2) # 3     -> 2, 1, 1
# spiral(3) # 5     -> 3, 2, 2, 1, 1
# spiral(4) # 7     -> 4, 3, 3, 2, 2, 1, 1
# spiral(5) # 9     -> 5, 4, 4, 3, 3, 2, 2, 1, 1
# spiral(6) # 11    -> 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1


# simple nested loop to create a matrix:
# for i in range(10):
#     text = ""
#     for j in range(10):
#         text += (str)(j)
#         text += ","
#         text += (str)(i)
#         text += "  "
#     print(text)