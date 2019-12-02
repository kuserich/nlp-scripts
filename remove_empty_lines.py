import sys
import os

def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)


files = sys.argv[1:]
references = []

for file in files:
    outfile = file + ".out"
    remove_file(outfile)
    handler = open(file, 'r')
    references.append(handler.readlines())

num_files = len(files)
line_lengths = [len(lines) for lines in references]
max_length = min(line_lengths)

print("Processing %d files:" % num_files)
print(" %s" % '\n '.join(files))

print("Max line length detected: %s" % max_length)

for i in range(max_length):
    min_l = min([0 if x[i] == '\n' else len(x[i]) for x in references])
    has_empty_lines = min_l == 0

    if not has_empty_lines:
        for j in range(num_files):
            handler = open(files[j]+'.out', 'a')
            handler.write(references[j][i])
