import sys

files = sys.argv[1:]
references = []

for file in files:
    handler = open(file, 'r')
    references.append(handler.readlines())

num_files = len(files)
max_length = min([len(lines) for lines in references])

for i in range(max_length):
    min_l = min([0 if x[i] == '\n' else len(x[i]) for x in references])
    has_empty_lines = min_l == 0

    if not has_empty_lines:
        for j in range(num_files):
            handler = open(files[j]+'.out', 'a')
            handler.write(references[j][i])
