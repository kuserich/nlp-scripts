import sys
import os


def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)


files = sys.argv[1:]
references = []
outfile_handlers = []

for file in files:
    outfile = file + ".out"
    outfile_handlers.append(open(outfile, 'w'))

    handler = open(file, 'r')
    references.append(handler.readlines())

num_files = len(files)
line_lengths = [len(lines) for lines in references]
max_length = min(line_lengths)

print("Processing %d files:" % num_files)
print(" %s" % '\n '.join(files))

print("Max line length detected: %s" % max_length)

for i in range(max_length):
    if i % 1000 == 0:
        print("%d percent complete" % (i/max_length*100))

    min_l = min([0 if x[i] == '\n' else len(x[i]) for x in references])
    has_empty_lines = min_l == 0

    if not has_empty_lines:
        for j in range(len(outfile_handlers)):
            outfile_handlers[j].write(references[j][i])
    else:
        print("Skipping line %d" % i)
