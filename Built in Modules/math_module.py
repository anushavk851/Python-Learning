import math
#provides mathematical functions and constants

# sqrt()--Finds square root.
print("1. sqrt():", math.sqrt(36))            

# pow()--Raises a number to a power.
print("2. pow():", math.pow(3, 2))           

#factorial()--Finds factorial.
print("3. factorial():", math.factorial(5))   

# ceil()--Rounds up.
print("4. ceil():", math.ceil(5.2))          

# floor()--Rounds down.
print("5. floor():", math.floor(5.9))         

# fabs()--Returns absolute value.
print("6. fabs():", math.fabs(-25))

# gcd()--Finds greatest common divisor.
print("7. gcd():", math.gcd(24, 36))

# sin()--Returns sine value.
print("8. sin():", math.sin(math.pi/2))

# cos()--Returns cosine value.
print("9. cos():", math.cos(0))

# log()--Returns logarithm.
print("10. log():", math.log(10))

# exp()--Return e raised to power of x,(eulers number e=2.71828)
print("11. exp():",math.exp(1))

print("12. math.pi: ",math.pi) #gives pi value


#import math as m (here insted of using word math we can type m eg m.log(10))
# as-alias(alias in Python,is a way to give a module or function a short or different name using the as keyword)
#from math import sqrt,pow--pow(4,5) here we dont have to mention math.pow(4,5) because we are importing a function as it is.
