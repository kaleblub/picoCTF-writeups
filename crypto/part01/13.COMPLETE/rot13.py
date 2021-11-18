import codecs

text = input("What text do you want to run ROT13 on?\n: ")
print(codecs.encode(text, 'rot_13'))