import sys


def read_file(filename):
    handler = open(filename, 'r')
    lines = handler.readlines()
    return lines


def get_index_from_line(line, borders):
    tokens = line.split()
    index_from_length = int(len(tokens) / 10)
    max_index = int(borders[-1] / 10) - 1
    index = min(max_index, index_from_length)
    return index


def get_empty_bucket(borders):
    buckets = {
        "src": {},
        "other": {}
    }
    for border in borders:
        buckets["src"][border] = []
        buckets["other"][border] = []
    return buckets


def split_file_by_sentence_length(src, other, borders):
    src_lines = read_file(src)
    other_lines = read_file(other)
    buckets = get_empty_bucket(borders)
    for i, line in enumerate(src_lines):
        index = get_index_from_line(line, borders)
        buckets["src"][borders[index]].append(line)
        buckets["other"][borders[index]].append(other_lines[i])

    for key in borders:
        with open(other + "_" + str(key) + ".txt", "w") as other_outfile:
            with open(src + "_" + str(key) + ".txt", "w") as src_outfile:
                for line in buckets["src"][key]:
                    src_outfile.write(line)

                for line in buckets["other"][key]:
                    other_outfile.write(line)


def main():
    if len(sys.argv) < 2:
        print("Error! Please provide a file")
        exit()

    src = sys.argv[1]
    other = sys.argv[2]
    borders = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    split_file_by_sentence_length(src, other, borders)


if __name__ == '__main__':
    main()
