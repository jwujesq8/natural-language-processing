# na wykładzie był przykład, który rozumiałam jako " Hurry on, Harry, hurry on! "


import re


def prepareGoodString(str):
    string_list = []
    str = str.lower()
    str = re.sub("[^\w\s]", "", str)
    str = re.sub("\s", "<w>", str)
    for index, char in enumerate(str):
        if char == '<' and str[index + 1] == 'w' and str[index + 2] == '>':
            string_list.append('<w>')
        elif (char == 'w' and str[index + 1] == '>' and str[index - 1] == '<') or (
                char == '>' and str[index - 2] == '<' and str[index - 1] == 'w'):
            continue
        else:
            string_list.append(char)
    return string_list


def countBiagramsInString(str):
    biagrams = {}
    for index, char in enumerate(str):
        if index<len(str)-1:
            seq = ''.join(str[index:index+2])
            biagrams[seq] = biagrams.get(seq, 0) + 1
    return biagrams


def mergeBiagramInStringAndCountItsFrequancy(biagram, biagrams, str):
    i=0
    length=len(str)
    while i<=length-2:
        new_seq = str[i] + str[i+1]
        if new_seq==biagram:
            str = str[:i] + [new_seq] + str[i+2:]
            length = length-1
        i=i+1
    return str, countBiagramsInString(str)


def bpe(str, num):
    str = prepareGoodString(str)
    vocab = list(set(str))
    biagrams = countBiagramsInString(str)

    while len(vocab)<=num:
        most_freq_biagram = max(biagrams, key=biagrams.get)
        str, biagrams = mergeBiagramInStringAndCountItsFrequancy(most_freq_biagram, biagrams, str)
        vocab.append(most_freq_biagram)

    return vocab


def main():
    while True:
        string_input = input("enter string: ")
        num_input = int(input("enter the number of subwords: "))
        if len(string_input)>0 and num_input>-1:
            vocab = bpe(string_input, num_input)
            for index, value in enumerate(vocab):
                print("\t" + str(index) + ": " + value)


if __name__=="__main__":
    main()

