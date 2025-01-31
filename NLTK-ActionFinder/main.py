import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')


def check_sentence(sentence):
    tokens = word_tokenize(sentence)
    parts_of_speech = pos_tag(tokens, lang='eng')
    print("token -> part of speech:")

    action_found = False
    for seq in parts_of_speech:
        print("\tword: " + seq[0] + " -> " + seq[1])
        if action_found:
            obj += seq[0] + " "
        if not action_found and seq[1].startswith('VB'):
            action = seq[0]
            obj = ""
            action_found = True

    if action_found:
        print("The sentence contains an action:\n\tAction: " + action + "\n\tObject: " + obj)
    else:
        print("The sentence doesn't contain an action")


print("\nFOR EXAMPLE: turn down the music")
sentence = "turn down the music"
check_sentence(sentence)
while True:
    sentence = input("\nenter the sentence (q for exit): ")
    if sentence == "q":
        exit(0)
    check_sentence(sentence)


