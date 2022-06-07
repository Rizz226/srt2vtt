import os
import webvtt
from pathlib import Path
from time import sleep as sleep

def convert(path):
	ext = ('.srt')
	path = path
	if path:
		ensurePathSep(path)
	else:
		path = os.getcwd()
		ensurePathSep(path)
	for file in os.listdir(path):
		if os.path.isfile(file) and file.endswith(ext):
			webvtt.from_srt(file).save()
			print("Successfully converted '" + file + "'")
		else:
			print("Skipping '" + file + "'")
	print("The conversion is complete")
	print("Please ensure the accuracy of the timing and the content before use.")
	try:
		input("Press 'Enter' or 'CTRL+C' to close. ")
	except KeyboardInterrupt:
		print("\n\nExiting...")
		sleep(3)
		exit()

def ensurePathSep(path):
	if path:
		if os.name == 'nt' and path[-1] != '\\':
			path = path + '\\'
		elif os.name == 'posix' and path[-1] != '/':
			path = path + '/'
		return path

def getInput():
	path = None
	cpath = os.getcwd()
	print("\n\nThis script will convert all '.srt' files in the chosen directory in to '.vtt' files.\nIf you do not choose a directory, it will default to the current directory of the Terminal.")
	try:
		uIN = input(f"\nThe present directory is: \n{cpath}\nPress enter to continue or enter an alternate directory then press enter.\n")
	except KeyboardInterrupt:
		print("\n\nExiting...")
		sleep(3)
		exit()
	path = uIN if len(uIN) > 4 else cpath
	try:
		input(f"The target directory is:\n{path}\nPress 'Enter' to continue or 'CTRL+C' to quit.")
		if path != None:
			return path
	except KeyboardInterrupt:
		print("\n\nExiting...")
		sleep(3)
		exit()

def main():
	path = getInput()
	convert(path)


if __name__ == '__main__':
	main()
