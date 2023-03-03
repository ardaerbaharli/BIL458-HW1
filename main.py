def isVowel(ch):

	# Make the list of vowels
	str = "aeiouAEIOU"
	return (str.find(ch) != -1)


# Take input
ch = input("Enter a character: ")

# Check if the character is a vowel
if (isVowel(ch)):
	print(ch, "is a vowel.")
else:
	print(ch, "is a consonant.")
