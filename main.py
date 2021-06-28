import functools
import sympy

arr=[1,2,3,4,5,6,7,8,9,10]

print(sum(arr))
print(functools.reduce(lambda a, b: a+b, arr))

x=sympy.S('x')
m,n,j=sympy.S([3,6,38])
equation=sympy.Eq(m*(x-n),x+j)
print(sympy.solve(equation))

##(alter-n)*m= alter+j
##wenn k heute 3mal(m) so alt wäre wie vor 6Jahren (n) dann wäre K nun 38Jahre (j) älter
