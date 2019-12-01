import argparse
from mosestokenizer import *

def de_preprocess(item, language):
    clean_references = []
    # for item in references:
    item = item.replace("@@ ", "")
    item = item.replace("@@@", "")
    item = item.replace("@@@@", "")
    item = item.replace("<eos>", "")
    item = item.replace("@str", "")

    item = item.replace("&amp;", "")
    item = item.replace("# 160 ;", "")

    item = item.replace("\n", "")
    with MosesDetokenizer(language) as detokenize:
        item_clean = detokenize(item.split(" "))
        clean_references.append(item_clean)
    return clean_references

parser = argparse.ArgumentParser(description="Compute BLEU score")
parser.add_argument("--src", type=str, help="path to source file")
parser.add_argument("--out", type=str, help="path to output file")
parser.add_argument("--language", type=str, nargs="?", help="Language of the source translation (needed for tokenizer)")

args = parser.parse_args()

language = args.language
source_file_path = args.src
output_file_path = args.out

with open(output_file_path, 'w') as output_file:
    for clean_line in [de_preprocess(line, language) for line in open(source_file_path, 'r')]:
        output_file.write(' '.join(clean_line))
