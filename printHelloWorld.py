# Prints Hello World with date and time

# Module required to get current date and time
import datetime
# Module to get location of file
import os

#Gets current directory path
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
print('Hello World')
print(datetime.datetime.now()) # Presents current date and time.
