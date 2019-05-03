import dis

def magic_calculation(a, b, c):
    return(a + b * c)

dis.dis(magic_calculation)
