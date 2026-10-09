def equilateral(sides):
    if not is_valid_triangle(sides): 
        return False 
        
    a = sides[0]
    b = sides[1]
    c = sides[2]

    return a == b and b == c
        


def isosceles(sides):
    if not is_valid_triangle(sides): 
        return False 
        
    a = sides[0]
    b = sides[1]
    c = sides[2]

    return a==b or a == c or b == c


def scalene(sides):
    if not is_valid_triangle(sides): 
        return False 
        
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a != b and a != c and b != c:
        return True
    else:
        return False
        


def is_valid_triangle(sides): 
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a <= 0 or b <= 0 or c <= 0: 
        return False 

    if a+b<c or a+c<b or b+c< a : 
        return False

    return True


