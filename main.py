print('To deduct area of triangle, please fill up following parameters:')
A = input('Side =')
h = input('Height=')

A = float(A)
h = float(h)

S = A*h/2
print('Area of the triangle is:' + '\n', round(S, 2))
