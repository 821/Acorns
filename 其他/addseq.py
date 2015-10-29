import re

srcfile = "E:/本草.txt"
srcencode = 'utf-8'
outfile = "E:/本草綱目.txt"
outencode = 'utf-8'

getzi = re.compile(r'^[^\t]+(?=\t)')
getpg = re.compile(r'(?<=\t)\d+')
pgold = ''
index = 1

src = open(srcfile, 'r', encoding = srcencode)
output = open(outfile, 'w+', encoding = outencode)
lines = src.readlines()

for line in lines:
	zi = getzi.search(line).group()
	pg = getpg.search(line).group()
	if pg == pgold:
		index += 1
	else:
		index = 1
		pgold = pg
	output.write(zi + '\t' + pg + '.' + str(index) + '\n')
