#10369980

import unittest
from CA5 import Commit, perauthor, perday, pertime

#tests
class TestCA5(unittest.TestCase):

	changes_file = 'changes_python.log'
	data = [line.strip() for line in open(changes_file, 'r')]
	sep = 72*'-'

	commits = []
	current_commit = None
	index = 0

	author = {}
	while True:
		try:
			# parse each of the commits and put them into a list of commits
			current_commit = Commit()
			details = data[index + 1].split('|')
			current_commit.revision = int(details[0].strip().strip('r'))
			current_commit.author = details[1].strip()
			current_commit.date = details[2].strip()
			current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
			current_commit.changes = data[index+2:data.index('',index+1)]
			#print(current_commit.changes)
			index = data.index(sep, index + 1)
			current_commit.comment = data[index-current_commit.comment_line_count:index]
			commits.append(current_commit)
		except IndexError:
			break

	commits.reverse()

	authors=[]
	for c in commits:
		found=False
		for a in authors:
			if c.author==a:
				found=True
		if found==False:
			authors.append(c.author)

	def testperauthor(self):
		self.assertEqual([191,152,26,24,9,7,5,5,2,1], perauthor(self.commits,self.authors)[1])
	
	days=["Mon","Tue","Wed","Thu","Fri"]
	
	def testperday(self):
		self.assertEqual([53,80,76,118,95], perday(self.commits,self.days))
		
	times=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
		
	def testpertime(self):
		self.assertEqual([0,0,0,0,0,1,3,2,12,33,30,57,31,56,96,52,39,4,2,1,3,0,0,0], pertime(self.commits,self.times))

if __name__ == '__main__':
    unittest.main()