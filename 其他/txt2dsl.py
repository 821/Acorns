import re

srcfile = 'E:/王力古漢語字典.txt'
srcencode = 'utf-8'
outfile = "E:/王力古漢語字典.dsl"
name = '王力古漢語字典'
prefix ='WL'
totalpg = 1791
n = len(str(totalpg))
index = 90
fow = 20
att = 0

getzi = re.compile(r'^\S+(?=\t)')
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
		output.write(zi + '\n\t<<' + prefix + str(pg).zfill(n) + '>>之' + no + '。\n\t')
	else:
		output.write(zi + '\n\t<<' + prefix + str(pg).zfill(n) + '>>。\n\t')
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

output.write(name + '\n\t')
output.write('版權[s]leg001.tif[/s]\n\t')
if fow > 0:
	fows = ''
	for pg in range (1, fow + 1):
		fows += '[s]fow' + str(pg).zfill(3) + '.tif[/s]'
	output.write('前言' + fows + '\n\t')
if att > 0:
	atts = ''
	for pg in range (1, att + 1):
		atts += '[s]att' + str(pg).zfill(3) + '.tif[/s]'
	output.write('附錄' + atts)
