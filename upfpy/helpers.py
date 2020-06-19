  
#import csv, math, pathlib, os.path

loc = str(pathlib.Path(__file__).parent) + "/vectors.txt"

"""
If the file vectors.txt does not exist in the same directory, create it.
This file stores outputs so they don't have to be recacluated.
"""
if os.path.exists(loc) == False:
    with open(loc, 'w') as csv_file:
        writer = (csv.writer(csv_file, delimiter=','))
        writer.writerow('2')
        writer.writerow([])
        writer.writerow('0')
        writer.writerow('1')

def store():
    pass
