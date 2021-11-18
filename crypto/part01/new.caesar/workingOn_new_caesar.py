import string

LOWERCASE_OFFSET = ord("a") # 97
ALPHABET = string.ascii_lowercase[:16] # 'a'-'p'

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c)) # Turns each letter into binary
		enc += ALPHABET[int(binary[:4], 2)] # Add the integer version of the binary's first 4 digits
		enc += ALPHABET[int(binary[4:], 2)] # Add the integer version of the binary's last 4 digits
	return enc # Gives back "{letter of binary first 4 digits}{letter of binary last 4 digits}"

def decode_to_b16(encryptedText):
	pass

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	print(f"t1 = {t1}\nt2 = {t2}")
	print(ALPHABET[(t1 + t2) % len(ALPHABET)])
	return ALPHABET[(t1 + t2) % len(ALPHABET)]
	#								^ 16

def unshift():
	pass

flag = "a"
key = "a"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

def encode_flag_with_key(flag, key):
	b16 = b16_encode(flag)
	# print("Enumerated b16 = ", enumerate(b16))
	enc = ""
	for i, c in enumerate(b16):
		# print(f"i = {i}, c = {c}")
		# print(f"{key[i % len(key)]}")
		# print("Shifted value = ", shift(c, key[i % len(key)]))
		enc += shift(c, key[i % len(key)])
		# 					^ just equals the key
	print(enc) # = mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj

for letter in string.ascii_lowercase:
	encode_flag_with_key(flag, letter)
	print()