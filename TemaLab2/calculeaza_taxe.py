def calculate_tax(pret, tva):
	return pret * (1 + tva/100)


def main():
	pret = 100
	tva = 19	# adica 19%
	print(calculate_tax(pret, tva))


if(__name__ == "__main__"):
	main()
