import gzip
import argparse


def get_argument_parser():
    parser = argparse.ArgumentParser(description="Parse best values from phrase table")
    parser.add_argument("--src",
                        type=str,
                        help="Path to the file containing the alignment pairs.")
    parser.add_argument("--out",
                        type=str,
                        help="Output file path")
    return parser


parser = get_argument_parser()
args = parser.parse_args()

def get_values_from_line(line):
    src, trg, probs, *rest = line.split('|||')
    src = src.strip()
    trg = trg.strip()
    probs = probs.strip()
    probs = [float(x) for x in probs.split()]

    return src, trg, probs

store = {}
with gzip.open(args.src) as infile:
    for line in infile:
        src, trg, probs, *rest = get_values_from_line(line)

        if not src in store:
            store[src] = probs[2]
        else:
            if probs[2] > store[src]:
                store[src] = probs[2]

with open(args.out, "w") as outfile:
    for key in store.keys():
        outfile.write("%s\n" % store[key])



