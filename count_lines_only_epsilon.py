import sys

"""
Prints the number of lines in a text file that contain
_only_ epsilon tokens.
"""

def clean_line(line):
    line = line.replace("@@@", "")
    line = line.replace("@@@@", "")
    line = line.replace("<eos>", "")
    line = line.replace("@str@@", "")
    return line

file_path = sys.argv[1]

total = 0
with open(file_path, 'r') as infile:
    for line in infile:
        if len(clean_line(line).split()) == 0:
            print(line)
            total += 1

print(total)