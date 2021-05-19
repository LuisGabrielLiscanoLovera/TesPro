

#51680 

#51700


sumDigit, extNum = 0, 0
numEntero = 51700
while numEntero != 0:
    extNum = numEntero % 10
    numEntero //= 10
    sumDigit += extNum
print("La suma de los digitos es: {}".format(sumDigit))

sumDigit, extNum = 0, 0
numEntero = 51680
while numEntero != 0:
    extNum = numEntero % 10
    numEntero //= 10
    sumDigit += extNum
print("La suma de los digitos es: {}".format(sumDigit))