import time
import sys

# Modify before each use, Shift + Right Click > Copy as path and paste here
# Add double '\\' for correct path to file
filePath = 'c:\\users\\xxFranciscoxx\\Desktop\\testuru\\Logs\\perimeter.log'
fileOutput = 'C:\\Users\\xxFranciscoxx\\Desktop\\Test.txt'

# Variables used
camPoints = 0
cont = 0

# Requires debbuging
def save_coord(latlonalt, fpath,j):
	fileOpen = open(fpath,'a')
	if (j == 0):
		fileOpen.write("\n" + latlonalt)
	else:
		fileOpen.write("\n" + latlonalt)
	j += 1
	return 0

# Intro, this looks pretty
print("*******************")
print("***   CLASSIC   ***")
print("*******************")
print("\n*************** WARNING ***************")
print("Running the script will modify the original Shotlog file.")
print("Please create a backup just in case.")
print("***************************************")
print("\nSearching for camPoints on Shotlog...")

# Look for camPoint messages on Shotlog
with open(filePath) as x:
	for line in x:
		if "navPoints" in line:
			print("\n"+line[53:])

# Ask the user to select camPoint extraction and validate input
while True:
	try:
		camPoints = int(input("\nPlease type in the desired camPoints to extract and press Enter: "))
	except ValueError:
		print("*** Type in a valid number ***")
		continue
	else:
		print("\nExtracting " + str(camPoints) +" coordinates to text file...")
		break		
	
# Progress bar, looks fancy but it's pointless, remove if you want to
toolbar_width = 40

sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1))

for i in range(toolbar_width):
    time.sleep(0.075)
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("\n")
# Progress bar ends here

	
# Look for coordinates in Shotlog and save into target Text file
with open(filePath) as f:
	for line in f:
		if ") at" in line:
			if "[perimeter]" in line:
				coordinate = line[57:87]
				save_coord(coordinate,fileOutput,cont)
				print(coordinate + " perimeter")
			elif ") at" in line:
				coordinate = line[54:84]
				save_coord(coordinate,fileOutput,cont)
				print(coordinate + " survey")
			
# Ending
print("\nCoordinates saved in output file.")
print("File saved in: " + fileOutput)
