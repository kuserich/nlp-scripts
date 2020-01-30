import argparse


def get_argument_parser():
    parser = argparse.ArgumentParser(description="Compare best values of two phrase tables")
    parser.add_argument("--one",
                        type=str,
                        help="Path to the first phrase table")
    parser.add_argument("--two",
                        type=str,
                        help="Path to the first phrase table")
    parser.add_argument("--out",
                        type=str,
                        help="Output file path")
    return parser


def get_values_from_line(line):
    src, trg, probs, *rest = line.split('|||')
    src = src.strip()
    trg = trg.strip()
    probs = probs.strip()
    probs = [float(x) for x in probs.split()]

    return src, trg, probs


parser = get_argument_parser()
args = parser.parse_args()

one_handler = open(args.one, "r")
two_handler = open(args.two, "r")

store = {}
for one, two in zip(one_handler, two_handler):
    one_src, one_trg, one_probs = get_values_from_line(one)
    two_src, two_trg, two_probs = get_values_from_line(two)

    if not one_src in store:
        store[one_src] = {"one": one_probs[2]}
    else:
        if one_probs[2] > store[one_src]["one"]:
            store[one_src]["one"] = one_probs[2]

    if not two_src in store:
        store[two_src] = {"two": two_probs[2]}
    else:
        if two_probs[2] > store[two_src]["two"]:
            store[two_src]["two"] = two_probs[2]


with open(args.out, "w") as outfile:
    for key in store.keys():
        if "one" in store[key] and "two" in store[key]:
            outfile.write("%s,%s\n" % (store[key]["one"], store[key]["two"]))

