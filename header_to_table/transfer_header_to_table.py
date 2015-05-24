import sys, os
import re

def transfer(result, outfile):
	type = result.group(1).replace("<", "&lt;").replace(">", "&gt;")
	var = result.group(2).replace("<", "&lt;").replace(">", "&gt;")
	outfile.write("<tr>\n"+"<td>"+ type + "</td>\n<td>" + var + "</td>\n")

def parsing(infile_name, outfile_name, type):
	t = int(type)
	infile = open(infile_name, "r")
	outfile = open(outfile_name, "w")

	parseVariable = re.compile(r'    ([a-zA-Z0-9<>_]+) ([a-zA-Z0-9<>,* ]+);')
	parseFunction = re.compile(r'    ([a-zA-Z0-9<>,* _]+) ([a-zA-Z0-9<>,* _&\(]+\));')
	parseCFunction = re.compile(r'    ([a-zA-Z0-9<>,* _]+) ([a-zA-Z0-9<>,* _&\(]+\)) const;')
	outfile.write("<table sytle=\"width:100%\">\n");
	for line in infile:
		if t == 0:
			result = parseVariable.search(line)
			if result:
				transfer(result, outfile)
		elif t == 1:
			result = parseFunction.search(line)
			if result:
				transfer(result, outfile)
			result = parseCFunction.search(line)
			if result:
				transfer(result, outfile)

	outfile.write("</table>\n");
	infile.close()
	outfile.close()

if __name__ == "__main__":
	if len(sys.argv) != 4:
		print "usage:"+argv[0]+" infile_name outfile_name type(0:variable, 1:function)"
		quit()
	parsing(sys.argv[1], sys.argv[2], sys.argv[3])
