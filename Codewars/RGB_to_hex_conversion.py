def rgb(r, g, b):
    values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    result = ""
    aux = ""
    
    if r < 0: 
        r = 0
    elif r > 255:
        r = 255
    for i in range(2):
        aux = values[r%16] + aux
        r //= 16
    result += aux
    
    aux = ""
    if g > 255:
        g = 255
    elif g < 0:
        g = 0
    for i in range(2):
        aux = values[g%16] + aux
        g //= 16
    result += aux
    
    aux = ""
    if b > 255:
        b = 255
    elif b < 0:
        b = 0
    for i in range(2):
        aux = values[b%16] + aux
        b //= 16
    result += aux
        
    return result    
    pass