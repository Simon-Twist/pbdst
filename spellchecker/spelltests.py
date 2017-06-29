#Simon Twist
#10369980

import unittest
from spell import SpellChecker
class TestSpellChecker(unittest.TestCase):

	def setUp(self):
		self.spellChecker = SpellChecker()
		self.spellChecker.load_words('spell.words')

	def test_spell_checker(self):
		self.assertEqual(True,self.spellChecker.check_word("zygotic"))
		
		failed_words=self.spellChecker.check_words("zygotic mistasdas elementary")
		self.assertEqual(1,len(failed_words))
		self.assertEqual("mistasdas",failed_words[0])
		self.assertEqual(0,len(self.spellChecker.check_words("our first correct sentence")))
		self.assertEqual(0,len(self.spellChecker.check_words("Our first correct sentence")))
		self.assertEqual(0,len(self.spellChecker.check_words("Our first correct sentence.")))
		
		failed_words=self.spellChecker.check_words("zygotic mistasdas spelllleeeing elementary")
		self.assertEqual(2,len(failed_words))
		self.assertEqual("mistasdas",failed_words[0])
		self.assertEqual("spelllleeeing",failed_words[1])
		
		self.assertEqual(0, len(self.spellChecker.check_document('spell.words')))

if __name__ == "__main__":
	unittest.main()
