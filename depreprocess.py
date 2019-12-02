import argparse
from mosestokenizer import *

def de_preprocess(references, language):
    clean_references = []
    for item in references:
        # item = item.replace("@@ ", "")
        item = item.replace("@@@", "")
        item = item.replace("@@@@", "")
        item = item.replace("<eos>", "")
        item = item.replace("@str@@", "")

        if len(item) > 0:
            clean_references.append(item)

    # item = item.replace("\n", "")
    # with MosesDetokenizer(language) as detokenize:
    #     item_clean = detokenize(item.split(" "))
    #     clean_references.append(item_clean)
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
    for line in open(source_file_path, 'r'):
        clean_line = de_preprocess(line.split(), language)
        output_file.write(" ".join(clean_line) + "\n")
