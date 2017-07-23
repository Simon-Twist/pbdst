#10369980

# open the file - and read all of the lines.
changes_file = 'changes_python.log'
# use strip to strip out spaces and trim the line.

#my_file = open(changes_file, 'r')
#data = my_file.readlines()

data = [line.strip() for line in open(changes_file, 'r')]

sep = 72*'-'

# create the commit class to hold each of the elements - I am hoping there will be 422
# otherwise I have messed up.
class Commit:
    'class for commits'
   
    def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment

    def get_commit_comment(self):
        return 'svn merge -r' + str(self.revision-1) + ':' + str(self.revision) + ' by ' \
                + self.author + ' with the comment ' + ','.join(self.comment) \
                + ' and the changes ' + ','.join(self.changes)

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

#Build a list of authors
authors=[]
for c in commits:
	found=False
	for a in authors:
		if c.author==a:
			found=True
	if found==False:
		authors.append(c.author)

#Count the commits by each author
def perauthor(commits,authors):
	per_author=[]
	for i in range(len(authors)):
		per_author.append(0)
		for c in commits:
			if c.author==authors[i]:
				per_author[i]+=1
			
	#sort
	per_author_dec=sorted(per_author)
	per_author_dec.reverse()
	
	return per_author,per_author_dec

perauthorlists=perauthor(commits,authors)
authors_dec=[]

for i in range(len(authors)):
	for k in range(len(authors)):
		if perauthorlists[1][i]==perauthorlists[0][k] and (i==0 or authors_dec[i-1]!=authors[k]):
			authors_dec.append(authors[k])
			break

#display
print			
for i in range(len(authors)):
		print "   %47s %d" % (authors_dec[i],perauthorlists[1][i])

#output to CSV
authorsfile=open("authors.csv","w")
authorsfile.write("Author,Commits\n")
for i in range(len(authors)):
	authorsfile.write(authors_dec[i]+","+str(perauthorlists[1][i])+"\n")
authorsfile.close()

#day of the week
#build a list of days
days=["Mon","Tue","Wed","Thu","Fri"]

#count the commits per day
def perday(commits,days):
	per_day=[]
	for i in range(len(days)):
		per_day.append(0)
		for c in commits:
			date=c.date.split("(")
			day=date[1][0:3]
			if day==days[i]:
				per_day[i]+=1
	return per_day
	
#display
print			
for i in range(len(days)):
		print "   %47s %d" % (days[i],perday(commits,days)[i])

#output to CSV
daysfile=open("days.csv","w")
daysfile.write("Day,Commits\n")
for i in range(len(days)):
	daysfile.write(days[i]+","+str(perday(commits,days)[i])+"\n")
daysfile.close()

#time of day
#build a list of times
times=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]

#count the commits at each time of day
def pertime(commits,times):
	per_time=[]
	for i in range(len(times)):
		per_time.append(0)
		for c in commits:
			time=c.date[11:13]
			if time==times[i]:
				per_time[i]+=1
	return per_time

per_time=pertime(commits,times)
#display
print			
for i in range(len(times)):
		print "   %47s %d" % (times[i],per_time[i])

#output to CSV
timesfile=open("times.csv","w")
timesfile.write("Time,Commits\n")
for i in range(len(times)):
	timesfile.write(times[i]+","+str(per_time[i])+"\n")
timesfile.close()

#write out commits
output_file = "changes.csv"
my_file=open(output_file,"w")
my_file.write("Revision,Author,Date,# Lines,Comment,Files Changed\n")
for commit in commits:
	my_file.write(str(commit.revision)+","+commit.author+',"'+commit.date+'",'+str(commit.comment_line_count)+','+"".join(commit.comment)+'\n')
my_file.close()
