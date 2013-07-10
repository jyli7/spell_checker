import string, collections, itertools

EXCLUDE = set(string.punctuation)

def depunctuate(s):
	return "".join(ch for ch in s if ch not in EXCLUDE)

def tokens():
	return depunctuate(file('big.txt').read()).split()

def language_histogram():
	tkns = tokens()
	counts = collections.defaultdict(lambda:0)

	for token in tkns:
		counts[token] += 1
	return counts

def one_edit_distance(word):
	'''make suggestions for 1 deletion, 1 addition, 1 replacement'''
	results = set()

	for i in range(1, len(word)):
		results.add(word[:i-1] + word[i:]) # deletion
		for letter in string.ascii_letters:
			results.add(word[:i] + letter + word[i:]) # addition
			results.add(word[:i-1] + letter + word[i:])	# replacement

	return results

def two_edit_distance(word):
	words = one_edit_distance(word)
	results = map(one_edit_distance, words)
	return set(itertools.chain(*results))

def suggest(word, model):
	if word in model:
		return word
	else:
		word_options = two_edit_distance(word)
		sorted_opts = sorted([(model[option], option) for option in word_options], reverse=True)
		best_word = sorted_opts[0][1]
		return best_word

def main():
	model = language_histogram()
	chosen_word = raw_input("What would would you like me to correct? ")
	print suggest(chosen_word, model)

if __name__ == "__main__":
	main()

	

