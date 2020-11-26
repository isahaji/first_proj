#isa haji llc

#isahaji.com
#26th novemebr 2020
print('hello there')


num1 = input('what is the numer you would like to convert ')

dn = int(num1)


b1 = 0
b2 = 0
b3 = 0
b4 = 0
b5 = 0
b6 = 0
b7 = 0
b8 = 0

if dn >= 128:
	dn = dn -128 
	b1 = b1 + 1
else:
	b1 = 0

print(b1)



if dn >= 64:
	dn = dn -64 
	b2 = b2 + 1
else:
	b2 = 0

print(b2)


if dn >= 32:
	dn = dn -32 
	b3 = b3 + 1
else:
	b3 = 0

print(b3)

if dn >= 16:
	dn = dn -16 
	b4 = b4 + 1 
else:
	b4 = 0

print(b4)


if dn >= 8:
	dn = dn -8 
	b5 = b5 + 1
else:
	b5 = 0

print(b5)

if dn >= 4:
	dn = dn -4 
	b6 = b6 + 1
else:
	b6 = 0

print(b6)


if dn >= 2:
	dn = dn -2 
	b7 = b7 + 1
else:
	b7 = 0


print(b7)


if dn >= 1:
	dn = dn -1 
	b8 = b8 + 1
else:
	b8 = 0

print(b8)

print(f"{b1}{b2}{b3}{b4}{b5}{b6}{b7}{b8} is the bunary number ")