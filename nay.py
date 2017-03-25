# made by Mauri Vanoro

import glob # for the file dir.
import random

print 'Enter Directory.'
path_to_check = raw_input('>>> ')


words = ['Hell is empty and all the devils are here.', 'We are such stuff as dreams are made on, and our little life is rounded with a sleep.', 'Me, poor man, my library\nWas dukedom large enough', 'Now I will believe that there are unicorns...', 'How beauteous mankind is! O brave new world, that has such people in it!', 'Doubt thou the stars are fire;\nDoubt that the sun doth move;\nDoubt truth to be a liar;\nBut never doubt I love', 'Conscience doth make cowards of us all', 'One may smile, and smile, and be a villain.', 'This above all: to thine own self be true.', 'Madness in great ones must not unwatched go.', '\"Seems,\" madam? Nay, it is. I know not \"seems.\"']
# customize for your own preferences. demo is from 'The Tempest' and 'Hamlet'


print '\nWhat Filetype?'
print 'e.g.     *.txt'
print 'For all :   .*'

ft = raw_input('\n\n>>> ')


check_path_ft = path_to_check + '\\*'+ ft
print check_path_ft
gvpath = glob.glob(check_path_ft)
# finding the dir and putting it into a list.

print '\n' + str(len(gvpath)) + ' files\n'


# main
i = 0
for i in range(len(gvpath) - 1):
	ope = str(gvpath[i])
	targ = open(ope, 'w')
	y = 0
	for y in range(random.randint(len(gvpath),(len(gvpath) * 9))):
		targ.write(random.choice(words))
		targ.write('\n\n')
		y = y+1
		random.shuffle(gvpath)
	i = i + 1
	print '['+str(i)+'] ' + gvpath[i] + ' Finished'


