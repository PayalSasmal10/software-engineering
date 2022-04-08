from cv2 import reduce


import functools
ls = [5,4,6,7]
m = list(map(lambda x: x*x, ls))
print(m)

f = list(filter(lambda x:x>4, ls))
print(f)

print(functools.reduce(lambda x,y: x+y, ls))



