import json

file_path_translations = "input/translations/default.txt"
# file_path_translations_kd = "input/translations/kd.txt"
# file_path_translations_tf = "input/translations/tf.txt"

file_path_sources = "input/translations/sources.txt"
file_path_targets = "input/translations/targets.txt"

translations = open(file_path_translations, 'r').readlines()
# translations_kd = open(file_path_translations_kd, 'r').readlines()
# translations_tf = open(file_path_translations_tf, 'r').readlines()

sources = open(file_path_sources, 'r').readlines()
targets = open(file_path_targets, 'r').readlines()

sentences = []
for i in range(len(sources)):
    sentences.append({
        "sources": sources[i],
        "targets": targets[i],
        "translation": translations[i],
    })


translations_with_epsilon_tokens = []

for sentence in sentences:
    translation = sentence['translation']

    default_has_eps = False
    kd_has_eps = False
    tf_has_eps = False

    have_same_translation = False

    if "@@@" in translation:
        translations_with_epsilon_tokens.append(sentence)

with open('output/translations_single.json', 'w') as outfile:
    json.dump(translations_with_epsilon_tokens, outfile, indent=4)

