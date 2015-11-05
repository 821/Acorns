import re

srcfile = "E:/本草綱目.txt"
srcencode = 'utf-8'
outfile = "E:/本草綱目.dsl"
name = '本草綱目'
prefix ='BC'
totalpg = 2000
n = len(str(totalpg))
index = 28
fow = 18
att = 224
indexatt = True

getzi = re.compile(r'^[^\t]+(?=\t)')
getpg = re.compile(r'(?<=\t)\d+')
getno = re.compile(r'(?<=\.)\d+$')

src = open(srcfile, 'r', encoding = srcencode)
output = open(outfile, 'w+', encoding = 'utf-16')
lines = src.readlines()

def pages(pg):
	if pg == 1:
		output.write('<<' + prefix + str(pg+1).zfill(n) + '>>[s]' + str(pg).zfill(6) + '.tif[/s]<<' + prefix + str(pg+1).zfill(n) + '>>\n')
	elif pg == totalpg:
		output.write('<<' + prefix + str(pg-1).zfill(n) + '>>[s]' + str(pg).zfill(6) + '.tif[/s]<<' + prefix + str(pg-1).zfill(n) + '>>\n')
	else:
		beaf = '<<' + prefix + str(pg-1).zfill(n) + '>> <<' + prefix + str(pg+1).zfill(n) + '>>'
		output.write(beaf + '[s]' + str(pg).zfill(6) + '.tif[/s]' + beaf + '\n')

output.write('#NAME	"' + name + '"\n#INDEX_LANGUAGE	"Chinese"\n#CONTENTS_LANGUAGE	"Chinese"\n')

for line in lines:
	zi = getzi.search(line).group()
	pg = (int(getpg.search(line).group()))
	if getno.search(line):
		no = getno.search(line).group()
		output.write(zi + '\n\t<<' + prefix + str(pg).zfill(n) + '>>之' + no + '\n\t')
	else:
		output.write(zi + '\n\t<<' + prefix + str(pg).zfill(n) + '>>\n\t')
	pages(pg)

for pg in range (1, totalpg + 1):
	output.write(prefix + str(pg).zfill(n) + '\n\t')
	pages(pg)

for pg in range (1, index + 1):
	output.write(prefix + 'I' + str(pg).zfill(3) + '\n\t')
	if pg == 1:
		output.write('<<' + prefix + 'I' + str(pg+1).zfill(3) + '>>[s]' + str(pg).zfill(6) + '.tif[/s]<<' + prefix + 'I' + str(pg+1).zfill(3) + '>>\n')
	elif pg == index:
		output.write('<<' + prefix + 'I' + str(pg-1).zfill(3) + '>>[s]' + str(pg).zfill(6) + '.tif[/s]<<' + prefix + 'I' + str(pg-1).zfill(3) + '>>\n')
	else:
		bf = '<<' + prefix + 'I' + str(pg-1).zfill(3) + '>> <<' + prefix + 'I' + str(pg+1).zfill(3) + '>>'
		output.write(bf + '[s]!' + str(pg).zfill(5) + '.tif[/s]' + bf + '\n')

if indexatt == True:
	for pg in range (1, att + 1):
		output.write(prefix + 'A' + str(pg).zfill(3) + '\n\t')
		if pg == 1:
			output.write('<<' + prefix + 'A' + str(pg+1).zfill(3) + '>>[s]att' + str(pg).zfill(3) + '.tif[/s]<<' + prefix + 'A' + str(pg+1).zfill(3) + '>>\n')
		elif pg == att:
			output.write('<<' + prefix + 'A' + str(pg-1).zfill(3) + '>>[s]att' + str(pg).zfill(3) + '.tif[/s]<<' + prefix + 'A' + str(pg-1).zfill(3) + '>>\n')
		else:
			bf = '<<' + prefix + 'A' + str(pg-1).zfill(3) + '>> <<' + prefix + 'A' + str(pg+1).zfill(3) + '>>'
			output.write(bf + '[s]att' + str(pg).zfill(3) + '.tif[/s]' + bf + '\n')

output.write(name + '\n\t')
output.write('版權[s]leg001.tif[/s]')
if fow > 0:
	fows = ''
	for pg in range (1, fow + 1):
		fows += '[s]fow' + str(pg).zfill(3) + '.tif[/s]'
	output.write('\n\t前言' + fows)
if indexatt != True and att > 0:
	atts = ''
	for pg in range (1, att + 1):
		atts += '[s]att' + str(pg).zfill(3) + '.tif[/s]'
	output.write('\n\t附錄' + atts)