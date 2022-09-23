# ôn tập kiểu chuỗi
print ('hello Thanh ')
a = 'Thanh Nguyen '
b = ' Sinh nam 1991 '
c = '30 tuổi '
print(a )
print(b )
print(c )

print(a,b,c )

a = '''
123
321
231
132
'''
print(a )
a = '123\'456\'789 '
print(a )

a= 'abc\"def\"ghi\" '
print (a )

# ôn tập dữ liệu kiểu số, quên hết sạch rồi

a = 1000
b = 20000
c= a+b
print('a là:', a )
print('b là:', b  )
print( a,'+',b,'=',c )
import math 
a = 1000
b = 20000
print(math.gcd(a,b ))

#số phức 

import math
a= 5 
b= 7 
c= complex(a,b )
print(c )
print('phần thực là', c.real )
print('phần ảo là', c. imag )
from fractions import*
d = Fraction(a,b )
print(d )

from decimal import*
getcontext().prec = 3
print(Decimal(a)/b )
a =123.234567768 
print(math.trunc(a))