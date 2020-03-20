import json

file_path_translations_default = "input/translations/default.txt"
file_path_translations_kd = "input/translations/kd.txt"
file_path_translations_tf = "input/translations/tf.txt"

file_path_sources = "input/translations/sources.txt"
file_path_targets = "input/translations/targets.txt"

translations_default = open(file_path_translations_default, 'r').readlines()
translations_kd = open(file_path_translations_kd, 'r').readlines()
translations_tf = open(file_path_translations_tf, 'r').readlines()

sources = open(file_path_sources, 'r').readlines()
targets = open(file_path_targets, 'r').readlines()

sentences = []
for i in range(len(sources)):
    sentences.append({
        "sources": sources[i],
        "targets": targets[i],
        "translations": {
            "default": translations_default[i],
            "kd": translations_kd[i],
            "tf": translations_tf[i],
        }
    })


eps_in_default = 0
eps_in_kd = 0
eps_in_tf = 0

eps_in_all = 0

same_translation_all = 0
same_translation_with_eps_all = 0

translations_with_epsilon_tokens = []

for sentence in sentences:
    default_translation = sentence['translations']['default']
    kd_translation = sentence['translations']['kd']
    tf_translation = sentence['translations']['tf']

    default_has_eps = False
    kd_has_eps = False
    tf_has_eps = False

    have_same_translation = False

    if "@@@" in default_translation:
        default_has_eps = True
        eps_in_default += 1

    if "@@@" in kd_translation:
        kd_has_eps = True
        eps_in_kd += 1

    if "@@@" in tf_translation:
        tf_has_eps = True
        eps_in_tf += 1

    if default_translation == kd_translation and kd_translation == default_translation:
        same_translation_all += 1
        have_same_translation = True

    if default_has_eps and kd_has_eps and tf_has_eps:
        eps_in_all += 1

        translations_with_epsilon_tokens.append(sentence)

        if have_same_translation:
            same_translation_with_eps_all += 1


print("Epsilon Tokens in DEFAULT: %s" % eps_in_default)
print("Epsilon Tokens in KD: %s" % eps_in_kd)
print("Epsilon Tokens in TF: %s" % eps_in_tf)
print("Epsilon Tokens in ALL: %s" % eps_in_all)
print("Number of identical translations: %s" % same_translation_all)
print("Number of identical translations WITH EPSILON: %s" % same_translation_with_eps_all)

with open('output/translations.json', 'w') as outfile:
    json.dump(translations_with_epsilon_tokens, outfile, indent=4)

