import sys

input_file_path = sys.argv[1]

num_lines = 0
sum_scores = 0
sum_probs = 0
with open(input_file_path, "r") as infile:
    for line in infile:
        _, score, log_prob = line.split("|||")
        score = score.strip()
        score = float(score)

        log_prob = log_prob.strip()
        log_prob = float(log_prob)

        num_lines += 1
        sum_scores += score
        sum_probs += log_prob

print(num_lines, sum_scores, sum_probs)
print(num_lines, sum_scores / num_lines, sum_probs / num_lines)
