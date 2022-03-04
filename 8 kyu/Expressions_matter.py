#Given three integers a ,b ,c, return the largest number obtained after inserting the following operators and brackets: +, *, ()
#In other words , try every combination of a,b,c with [*+()] , and return the Maximum Obtained

#try all combinations
#append them to a list
#print the max of that list
a = 1 
b = 2 
c = 3

def expression_matter(a, b, c):
    v = a + b + c
    w = a * (b + c)
    x = a * b * c
    y = a + b * c
    z = (a + b) * c
    return (max(v, w, x, y, z))

def expression_matter(a, b, c):
    return max(a*b*c, a+b+c, (a+b)*c, a*(b+c))

