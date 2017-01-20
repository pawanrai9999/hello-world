import os, os.path

root = os.path.dirname(os.path.realpath(__file__))
size = 10
for root, _, files in os.walk(check):
	for f in files:
		fullpath = os.path.join(root, f)
		if os.path.getsize(fullpath) < size * 1024
			os.remove(fullpath)
