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
    buckets = {}
    for border in borders:
        buckets[border] = []
    return buckets


def split_file_by_sentence_length(filename, borders):
    lines = read_file(filename)
    buckets = get_empty_bucket(borders)
    for line in lines:
        index = get_index_from_line(line, borders)
        buckets[borders[index]].append(line)

    for key in buckets.keys():
        with open(filename + "_" + str(key) + ".txt", "w") as outfile:
            for line in buckets[key]:
                outfile.write(line)




def main():
    if len(sys.argv) < 2:
        print("Error! Please provide a file")
        exit()

    filename = sys.argv[1]
    borders = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    split_file_by_sentence_length(filename, borders)


if __name__ == '__main__':
    main()