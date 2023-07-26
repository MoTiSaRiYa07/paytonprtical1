print("enter a values:")
a = float(input())

print("enter b values:")
b = float(input())

print("enter x values:")
x = float(input())

print("enter y values:")
y = float(input())

print("enter z values:") 
z = float(input())

#(1) x+yz
res = x + y * z
print("\n x+yz  = ", res )

#(2)xy + ab2 
res = x * y + a * b**2
print("\n xy+abserue = ", res )

#(3)asequre+ 2ab + bsequre
res = a**2 + 2*a*b + b**2
print("\n asequre+ 2ab + bsequre = ", res)

#(4)asequre - 2ab + bsequre
res = a**2 - 2*a*b + b**2
print("\n asequre- 2ab + bsequre = ", res)

#(5)(a – b)(a + b)
res = (a - b) * (a + b)
print("\n (a – b)(a + b) = ", res)

#(6) a3seure + b3squre + 3ab(a + b)
res = a**3 + b**3 + 3*a*b*(a + b)
print("\n a3seure + b3squre + 3ab(a + b) = ", res)

#(7) a3seure - b3squre - 3ab(a - b)
res = a**3 - b**3 - 3*a*b*(a - b)
print("\n a3seure - b3squre - 3ab(a - b) = ", res)

#(8) (a – b)(a2sequre + ab + b2squre )
res = (a - b) * (a**2 + a*b + b**2)
print("\n (a – b)(a2sequre + ab + b2squre ) = ", res)


#(9) (a + b)(a2sequre - ab + b2squre )
res = (a + b) * (a**2 - a*b + b**2)
print("\n (a + b)(a2sequre - ab + b2squre ) = ", res)


#(10) 3xy3squre + 9x2squre y3squre + 5y3 squre x
res =  3*x*y**3 + 9*x**2*y**3 + 5*y**3*x
print("\n 3xy3squre + 9x2squre y3squre + 5y3 squre x = ", res)


