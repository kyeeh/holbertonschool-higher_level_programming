#!/usr/bin/python3
def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if (n <= 0):
        return []
    matrix = [[1], [1, 1]]
    vector = [1, 1]
    for i in range(3, n):
        top = int(i / 2)
        matrix.append(pt_rec(i, top, vector))
    return (matrix)

def pt_rec(idx, top, vector):
    """
    Pascal’s triangle of n in a recursive way
    """    
    
    if (idx >= top):
        vector[idx - 1] = vector[idx - 1] + vector[idx - 2]
        return vector
    else:
        vector.append(1)
        pt_rec(idx + 1, top, vector)
