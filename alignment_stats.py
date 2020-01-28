import argparse


def get_argument_parser():
    parser = argparse.ArgumentParser(description="Comput Alignment Stats")
    parser.add_argument("--align",
                        type=str,
                        help="Path to the file containing the alignment pairs.")
    parser.add_argument("--corpus",
                        type=str,
                        help="Path to the parallel corpus file.")
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
This script requires both the alignments as well as the parallel corpus.
We noticed in our alignments that the number of alignment pairs does not
match the number of tokens in either of the sequences.
This opens the discussion for how the 'total distance', i.e. the sum of
all non-monotonic alignments, should be normalized.
"""
parser = get_argument_parser()
args = parser.parse_args()

alignments_file = args.align
parallel_corpus_file = args.corpus
output_file_path = args.out

distances = []
with open(alignments_file, "r") as file:
    statistics = []
    corpus = open(parallel_corpus_file, "r").readlines()
    for index, line in enumerate(file):

        total_distance = 0
        number_of_pairs = 0
        src_len = len(corpus[index].split("|||")[0].split())
        trg_len = len(corpus[index].split("|||")[1].split())
        epsilon_required = 0

        for i, j in get_alignment_pairs_from_line(line):
            number_of_pairs += 1
            if i > j:
                total_distance += (i-j)
                # additional epsilon tokens are only needed if the given mismatch
                # still exists previous mismatches were eliminated with epsilon
                # tokens in tokens t_k such that k < j
                #
                # e.g.
                #
                # >>> Madam   President     ,     on    a                  point of order .
                #     Frau    Präsidentin   ,     zur   Geschäftsordnung   .
                #     0-0     0-1           2-2   5-3   7-4                8-5
                #
                # Adding two epsilon tokens before "zur" would already move
                # "Geschäftsordnung" two steps closer to "order" and thus reducing the
                # required number of epsilon tokens in the 2nd mismatch (7-4) to one
                # which then reduces the number of epsilon tokens required to fix the last
                # mismatch (8-5) to zero.
                #
                # The difference between epsilon required and (i-j) might be negative,
                # hence we simply compute the difference and take zero if it zero or
                # negative.
                epsilon_required += max(((i-j) - epsilon_required), 0)
        statistics.append(
            (total_distance, epsilon_required, number_of_pairs, src_len, trg_len)
        )

with open(output_file_path, "w") as outfile:
    outfile.write("total_distance,epsilon_required,num_pairs,src_len,trg_len\n")
    for total_distance, epsilon_required, num_pairs, src_len, trg_len in statistics:
        outfile.write(
            "%s,%s,%s,%s,%s\n" % (total_distance, epsilon_required, num_pairs, src_len, trg_len)
        )