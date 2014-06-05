# I have no idea what I'm doing.
import sys, getopt
from dxfwrite import DXFEngine as dxf

offsetX = 7.08
offsetY = 22.03

# Pinched from http://www.tutorialspoint.com/python/python_command_line_arguments.htm
def main(argv):
	datafile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"ho:d:",["ofile=","dfile="])
	except getopt.GetoptError:
		print 'barcamp-tags.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'barcamp-tags.py -i <inputfile> -o <outputfile>'
			sys.exit()
		elif opt in ("-o", "--ofile"):
			outputfile = arg
		elif opt in ("-d", "--dfile"):
			datafile = arg

	# Open the DXF file...
	drawing = dxf.drawing(outputfile)

	row = 1
	column = 1
	with open(datafile, 'rb') as csvfile:
		data = csvfile.read().split(',')
		# I don't understand python.
		for item in data:
			x = row * 85.6
			y = column * 53.98

			print item

			# Append \n to long names
			item = item.replace(' ', '\r\n', 1)

			text = dxf.mtext(item, (x+offsetX, y+offsetY), height=8.5, rotation=0)
			text.layer = 'TEXT'
			text.color = 5 # Blue
			drawing.add(text)

			# Increment rows and columns (lim 6 rows)
			row = row + 1
			if row == 7:
				row = 1
				column = column + 1


	drawing.saveas(outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])