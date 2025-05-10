def word_count(text):
        words =  text.split()
        return len(words)
	#this is the function that counts the number of words in a text


def letter_count(text):
	lowercase = text.lower()
	count = {}
	for letter in lowercase:
		if letter in count:
			count[letter] += 1
		else:
			count[letter] = 1
	return count
# this function takes the text and converts all letters to lowercase so that it can return a count of each character

def sorted_list(letters_count):
	letters_list = []
	for letter, num in letters_count.items():
		letters_list.append({"letter" : letter, "num" : num})
#this top part takes a dictionary of letter counts and turns it into a list and defines the keys

	def sort_on(item):
        	return item["num"] #this lets the function know which key to sort by
	letters_list.sort(reverse=True, key=sort_on) #this lets .sort know to gvo from high to low
	return letters_list
