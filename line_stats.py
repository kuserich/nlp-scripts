import sys


def read_file(filename):
    filehandler = open(filename, 'r')
    lines = filehandler.readlines()
    clean_lines = [line.replace('\n', '') for line in lines]
    return clean_lines


def compute_line_stats(lines):
    token_counts = []
    total = 0
    for line in lines:
        tokens = line.split()
        num_tokens = len(tokens)
        token_counts.append(num_tokens)
        total += num_tokens
    return total, token_counts


def main():
    if len(sys.argv) < 2:
        print("Error! Please provide a file")
        exit()

    filename = sys.argv[1]
    total, counts = compute_line_stats(read_file(filename))

    with open(filename + '.lstats', 'w') as outfile:
        outfile.write('index,count\n')
        for index, line in enumerate(counts):
            outfile.write('%s,%s\n' % (index, line))


if __name__ == '__main__':
    main()
