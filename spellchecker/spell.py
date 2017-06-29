#Simon Twist
#10369980

class SpellChecker:
	def __init__(self):
		self.words = []
		
	def load_file(self, file_name):
		lines = open(file_name).readlines()
		lines = map(lambda x: x.strip(), lines)
		return lines
	
	def load_words(self,file_name):
#		self.words = self.load_file(file_name)
		self.words = open(file_name).readlines()
		self.words = map(lambda x: x.strip().lower(), self.words)

	def check_word(self,word):
		return word.strip(".").lower() in self.words

	def check_words(self,sentence,index=0):
		words_to_check = sentence.split(" ")
		caret_position=0
		failed_words=[]
		for word in words_to_check:
			if not self.check_word(word):
#				print "Word is misspelt :",word
				print 'Word is misspelt',word,'at line :',str(index+1),'pos',str(caret_position+1)
				failed_words.append(word)
			caret_position = caret_position + len(word) + 1
		return failed_words

	def check_document(self, file_name):
		self.sentences = self.load_file(file_name)
		failed_words_in_sentences = []
		index = 0
		for sentence in self.sentences:
			failed_words_in_sentences.extend(self.check_words(sentence,index))
			index = index + 1
		return failed_words_in_sentences