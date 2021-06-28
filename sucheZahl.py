import sympy as sy

x100, x10, x1 = sy.symbols("x100 x10 x1")
equations = [
    sy.Eq(x100+x10+x1,18),
    sy.Eq(x100-6,x10*2),
    sy.Eq(x1-6,x10*3)
]
print(sy.solve(equations))

a,b,c,d,f=18,6,2,6,3
z=(a-b-d)/(c+f+1)
h=z*c+b
e=z*f+d
zahl=h*100+z*10+e
print(zahl)