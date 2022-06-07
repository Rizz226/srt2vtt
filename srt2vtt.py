import os
import webvtt
from pathlib import Path



def getPath():
	if os.name == 'nt' and path[-1] != '\\':
		path = path + '\\'
	elif os.name == 'posix' and path[-1] != '/':
		path = path + '/'
	return path

# print("This will convert all '.srt' files in the present directory in to '.vtt' files. ")
print("\n\nThis script will convery all '.srt' files in the chosen directory in to '.vtt' files.\nIf you do not choose a directory, it will default to the current directory of the Terminal.")
path = input("Please enter the location of the file you want to convert (ex: C:\\Users\\%USERNAME%\\Videos\\Subtitles\\): ")
print("The present directory is: " + path)
input("Press 'Enter' to continue or 'CTRL+C' to quit.")
if path:
	getPath()
else:
	path = os.getcwd()
	getPath()
for file in os.listdir(path):
	if Path(file).suffix == '.srt':
		webvtt.from_srt(file).save()
		print("Successfully converted '" + file + "'")
	else:
		print("Skipping " + file)
print("The conversion is complete")
print("Please ensure the accuracy of the timing and the content before use.")