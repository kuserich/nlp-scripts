import sys

src = sys.argv[1]
trg = sys.argv[2]

src_handler = open(src, 'r')
trg_handler = open(trg, 'r')

src_lines = src_handler.read().split('\n')
trg_lines = trg_handler.read().split('\n')

print("Found %s lines in SRC" % len(src_lines))
print("Found %s lines in TRG" % len(trg_lines))

min_len = min(len(src_lines), len(trg_lines))

wc_src = 0
wc_trg = 0

for i in range(min_len):
    src_tokens = src_lines[i].split()
    trg_tokens = trg_lines[i].split()

    wc_src += len(src_tokens)
    wc_trg += len(trg_tokens)

    if wc_src != wc_trg:
        print("Lines at index %s have different lenghts" % i)
        print("    " + src_lines[i])
        print("    " + trg_lines[i])

print("Word Count Source: %s, Word Count Target: %s" % (wc_src, wc_trg))