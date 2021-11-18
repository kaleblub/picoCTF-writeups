def seperator():
	print("\n\n-------------------------------------------\n\n")

def binaryToUnicode():
	binary = input("Input the string of binary numbers\n: ")
	binary = [chr(int("0b" + i, 2)) for i in binary.split(" ")]
	print("Result: ", "".join(binary))

def ASCIIToUnicode():
	asciiCodedNums = input("Input the string of ASCII Numbers\n: ")
	asciiCodedNums = [chr(int(i)) for i in asciiCodedNums.split(" ")]
	print(asciiCodedNums)
	print("Result: ", "".join(asciiCodedNums))


if __name__ == "__main__":
	while True:
		print("What do you need?\n1) Binary to text?\n2) ASCII Coded numbers to text?\n3) Hexidecimal to text?")
		option = int(input(": "))
		if option == 1:
			binaryToUnicode()
		if option == 2:
			ASCIIToUnicode()
		if option == 3:
			pass
		seperator()