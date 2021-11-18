import string
alphabet = string.ascii_lowercase
cipheredLetters = [20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
decryptedLetters = []
for letter in cipheredLetters:
	decryptedLetters.append(alphabet[letter - 1])
print("".join(decryptedLetters))