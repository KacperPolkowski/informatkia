def wb(x):
    return abs(x)
P = 9
E = 0.0001
a = 1
a2 = P
while wb (a - a2) > E:
    a = (a + a2) / 2
    a2 = P / a
print(a)


