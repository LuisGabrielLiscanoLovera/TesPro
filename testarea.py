

#51680 

#51700

sumDigitU, extNumU = 0, 0
sumDigitD, extNumD = 0, 0
numEnteroU = 51700
numEnteroD = 51680

ranges=20

if numEnteroU % ranges==0 & numEnteroD % ranges==0:
	print(ranges)
	print('numEnteroU :'+str(numEnteroU))
	print('numEnteroD :'+str(numEnteroD))

	numEnteroU=numEnteroU/ranges
	numEnteroD=numEnteroU/ranges
	print('r d r U :'+str(numEnteroU))
	print('r d r D :'+str(numEnteroD))
	while numEnteroU != 0:
	    extNumU = numEnteroU % 10
	    numEnteroU //= 10
	    sumDigitU += extNumU
	while numEnteroD != 0:
	    extNumD = numEnteroD % 10
	    numEnteroD //= 10
	    sumDigitD += extNumD

	print("La suma de los digitos es: {}".format(sumDigitU))
	print("La suma de los digitos es: {}".format(sumDigitD))
	print("La suma total: {}".format(sumDigitU + sumDigitD))
	nf=sumDigitU + sumDigitD
	print('digito 1'+str(sumDigitU))
	print('digito 2'+str(sumDigitD))		
	print ('numero nf '+str(nf))
else:
	print('no pasa: {}'.format(ranges))
	
