import re
import string
import sys
from itertools import repeat

def add_endsDNA(line, end):
	return end.upper()+line.upper()
def revDNA(line):
	return line[::-1]
def complementDNA(line):
	complement = {'A': 'T', 'C':'G', 'G':'C', 'T':'A'}
	bases = list(line.upper())
	bases = [complement[base] for base in bases]
	return ''.join(bases) 
def checkDNA(myline):
	pattern = re.compile(r"[atcg]")	# match bases
	npattern = re.compile(r"[^atcg]")
	if (len(pattern.findall(myline.lower())) > 0) & (len(npattern.findall(myline.lower()))==0):
		return 1
	else:
		return 0
if __name__ == '__main__':
	try:
		myfile = str(sys.argv[1])
		end = str(sys.argv[2])
	except:
		print 'Usage: python crispr_primer.py inputprimers.txt REsites'
    		sys.exit()

    	f = open(myfile, "r")

	for line in iter(f):
 		line = line.strip()	# Remove whitespace!
		outF = open(myfile + "_outfile.txt", "a")		
		if checkDNA(line) == 1:
			# Write sense strand with ends using print (5->3)
			print >> outF, add_endsDNA(line, end)
			# Write antisense strand with ends using print (5->3)
			print >> outF, str(" "*len(end))+revDNA(add_endsDNA(revDNA(complementDNA(line)), complementDNA(end)))
		else:
			print >> outF, "ERROR " + line
