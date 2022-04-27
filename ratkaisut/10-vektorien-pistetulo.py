a = [2, 4, -1]
b = [2, -5, 1]

# a-kohta

def dot(left, right):
    assert(len(left) == len(right))
    sum = 0
    for left, right in zip(left, right):
        sum += left * right
    return sum

apisteb = dot(a, b)
if apisteb == 0:
    print("a ja b ovat kohtisuoria")
else:
    print(f"a ja b eivät ole kohtisuoria, pistetulo on {apisteb}")

# b-kohta

from math import sqrt, acos

def norm(vec):
    sum = 0
    for b in vec:
        sum += b ** 2
    return sqrt(sum)

def angle(left, right):
    return acos(dot(left, right) / (norm(left) * norm(right)))

kulma = angle(a, b)
print(f"a ja b välinen kulma on {kulma} radiaania")
