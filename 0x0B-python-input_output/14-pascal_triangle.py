#!/usr/bin/python3
def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    pt = [[1], [1, 1]]
    cl = [1, 1]
    top = int((n / 2) + 1)
    for i in range(2, top):
        for j in range(1, i):
            #print("{}, {}, {}".format(i, j, top))
            cl[j] = cl[j] + cl[j - 1]
        cl.append(1)
        #print(cl)
        pt.append(cl)
    return (pt)
