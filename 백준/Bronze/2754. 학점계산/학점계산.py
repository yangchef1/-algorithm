a = input() + ' '
d = {'A' : 3.0, 'B' : 2.0, 'C' : 1.0, '+' : 1.3, '0' : 1, '-' : 0.7}
print(d.get(a[0], 0.0) + d.get(a[1], 0.0))