import argparse

def get_argument_parser():
    parser = argparse.ArgumentParser(description="Convert Alignments File to CSV")
    parser.add_argument("--align",
                        type=str,
                        help="Path to the file containing the alignment pairs.")
    parser.add_argument("--out",
                        type=str,
                        help="Output file path")
    return parser


def get_alignment_pairs_from_line(line):
    """
    Generates an iterable of integer pairs given a line from
    an alignment file of the following structure

    >>> "0-0 4-1 3-2 2-3"

    :param line:
    :return:
    """
    pairs = line.split()
    for pair in pairs:
        yield [int(x) for x in pair.split("-")]

"""
Transforms alignments output file from fast_align into a
CSV file.
"""

parser = get_argument_parser()
args = parser.parse_args()

alignments_file = args.align
output_file_path = args.out

with open(output_file_path, 'w') as outfile:
    outfile.write("line_index,token_index,src,trg\n")
    with open(alignments_file, 'r') as infile:
        for index, line in enumerate(infile):
            for token_index, (i, j) in enumerate(get_alignment_pairs_from_line(line)):
                outfile.write("%s,%s,%s,%s\n" % (index, token_index, i, j))