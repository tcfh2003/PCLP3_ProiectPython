unu = 3
doi = 3.2
trei = 1+1j
patru = "George"
cinci = '5'

#3.1
print("\n3.1: \n")

print(type(unu))	# int
print(type(doi))	# float
print(type(trei))	# complex
print(type(patru))	# string
print(type(cinci))	# string

#3.2
print("\n3.2: \n")

print(unu + doi)	# 6.2
print(patru + cinci)	# George5

#3.3
print("\n3.3: \n")

print(unu*3)	# 9
print(unu**unu)	# 27
print(patru*3)	# GeorgeGeorgeGeorge

#3.4
print("\n3.4: \n")

print(patru + str(doi))	# George3.2

#3.5
print("\n3.5: \n")

print(help(patru))
'''
No Python documentation found for 'George'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

None
'''

#3.6
print("\n3.6: \n")

print(type(int(cinci)))		# int
print(type(complex(cinci)))	# complex
print(type(float(cinci)))	# float
