"""
Given a string, you need to reverse the order of characters in each word within a sentence 
while still preserving whitespace and initial word order.
"""

def reverse_word(word):
	if len(word) == 1:
		return word
	return str(reverse_word(word[1:])) + word[0]

def reverse_string(string):
	list_of_words = string.split(" ")
	new_list = []
	for word in list_of_words:
		new_word = reverse_word(word)
		print(new_word)
		new_list.append(new_word)
	return " ".join(new_list)

def reverse_string_pythonic(string):
	# Pythonic
	return " ".join(word[::-1] for word in string.split(" "))

# driver code
print(reverse_string_pythonic("Take a string and return reversed words in string in their original order"))
print(reverse_string("Take a string and return reversed words in string in their original order"))

