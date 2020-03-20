import sys

file_paths = sys.argv[1:3]

print(file_paths)

sentence_groups = []
epsilons_per_sentence = []
at_least_one_epsilon = []

for file_path in file_paths:
    file_handler = open(file_path, 'r')
    sentence_groups.append(file_handler.readlines())
    at_least_one_epsilon.append([])





for i in range(len(sentence_groups[0])):
    epsilons_per_sentence.append([])
    for index, group in enumerate(sentence_groups):
        sentence = group[i]
        number_of_epsilons_in_sentence = sentence.count("@@@")
        epsilons_per_sentence[i].append(number_of_epsilons_in_sentence)
        # if there are no epsilons, this will add 0, otherwise it will add 1
        at_least_one_epsilon[index].append(min(1, number_of_epsilons_in_sentence))

number_sentences_without_epsilons = 0
for sentence in epsilons_per_sentence:
    if sum(sentence) == 0:
        number_sentences_without_epsilons += 1


def number_of_sentences_with_at_least_one_epsilon_token(epsilon_counts, index):
    return sum([min(1, x[index]) for x in epsilon_counts])

def number_of_new_sentences_with_at_least_one_epsilon_token(epsilon_counts, firstIndex, secondIndex):
    total = 0
    for sentence in epsilon_counts:
        num_first = sentence[firstIndex]
        num_second = sentence[secondIndex]

        if num_second > num_first:
            total += 1

    return total
    # return sum([min(1, sentence[secondIndex] - sentence[firstIndex]) for sentence in epsilon_counts])



def number_of_new_sentences_with_at_least_one_fewer_epsilon_token(epsilon_counts, firstIndex, secondIndex):
    total = 0
    for sentence in epsilon_counts:
        num_first = sentence[firstIndex]
        num_second = sentence[secondIndex]

        if num_second < num_first:
            total += 1

    return total


print(number_of_sentences_with_at_least_one_epsilon_token(epsilons_per_sentence, 0))
print(number_of_sentences_with_at_least_one_epsilon_token(epsilons_per_sentence, 1))

print(number_of_new_sentences_with_at_least_one_epsilon_token(epsilons_per_sentence, 0, 1))
print(number_of_new_sentences_with_at_least_one_fewer_epsilon_token(epsilons_per_sentence, 0, 1))
