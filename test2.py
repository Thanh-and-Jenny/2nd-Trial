print("Hello Thanh Nguyen ")

# ham bien so tu nhien
a = 4
b = 100
c = a + b
print("a =", a )
print("b =", b  )
print ("a", "+", "b", "=", c )
print (type(c ))
  
# ham bien so thap phan
from decimal import*
getcontext().prec = 5
d = Decimal(4 )/ 3 
print(d )

#lay phan nguyen cua phep chia 
print(10//3 )

#lay phan du cua phep chia
print(10%3 )

#so phuc 
e = complex (3,4)
print(e )
print("phan thuc  = ", e.real )
print("phan ao = ", e.imag )

#phan so
from fractions import*
f= Fraction (2,5)
g= Fraction (7,3)
h= f+g 
print(f )
print(g)
print(f,"+",g,"=",h )
i= 10/3
print(type(i ))
j= 9-11
print(j )
print(type(j ))

#luy thua
k= 2**10
print(k )

#su dung thu vien math
import math
a = 3.456789
print("a= ", a)
print("gia tri tuyet doi cua so a la:", math.fabs(a ))

print("phan nguyen cua so a la:", math.trunc(a))

print("so lon nhat lien ke a la:", math.ceil(a))
print("so nho nhat lien ke a la:", math.floor(a)) 

b = 16
print("so b la: ", b )
print("gia tri can bac hai cua b la:" , math.sqrt(b )) 
a = 12
b = 9
print ("So a la: ", a )
print("So b la: ", b )
print("uoc chung lon nhat cua", a, "va", b, "la ", math.gcd(a,b))












