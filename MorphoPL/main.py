import os
import pandas as pd


def read_polish_dir():
    polish_dir_file = pd.read_csv("..//poliMorf//PoliMorf-0.6.7.tab").to_string().splitlines()
    saved_polish_dir_file = open('saved_polish_dir.txt', 'a', encoding='utf-8')
    for row in polish_dir_file:
        row = row.replace(' ', '')
        columns = row.split('\\t')
        word_info = columns[:3]
        word = word_info[0]
        for char in word:
            if char.isdigit():
                word = word[1:]
        word_info[0] = word
        for i in range(len(word_info)):
            if i == len(word_info) - 1:
                saved_polish_dir_file.write('\n')
            else:
                saved_polish_dir_file.write(word_info[i] + '\t')


def get_polish_dir():
    if not os.path.exists('.//saved_polish_dir.txt'):
        read_polish_dir()
    polish_dir = open('.//saved_polish_dir.txt', 'r', encoding='utf-8').read().splitlines()
    print("\t__polish dir is loaded__")
    return polish_dir


def get_polish_language_parts():
    lang_p = {
        "impt": "czasownik",
        "fin": "czasownik",
        "inf": "czasownik",
        "praet": "czasownik",
        "imps": "czasownik",
        "bedzie": "czasownik",

        "pact": "przymiotnik",
        "ppas": "przymiotnik",
        "adj": "przymiotnik",
        "adjc": "przymiotnik",
        "winien": "przymiotnik",

        "depr": "rzeczownik nazwisko",

        "ger": "rzeczownik",
        "subst": "rzeczownik",
        "adjp": "rzeczownik",
        "ppron12": "rzeczownik",
        "ppron3": "rzeczownik",

        "adv": "przysłówek",
        "qub": "przysłówek",
        "adja": "przysłówek",

        "conj": "spójnik",
        "comp": "spójnik",

        "prep": "przyimek",

        "pant": "imiesłowów",
        "pcon": "imiesłowów",

        "interj": "wykrzyknik parentetyczny/onomatopeiczny",

        "burk": "człon nazwy",

        "num": "liczebnik",

        "pred": "partykuła",

        "aglt": "końcówka przeszłego czasu"
    }
    return lang_p


def pos_tagging(str, dir, polish_language_parts):
    word_found = False
    for row in dir:
        row_by_col = row.split('\t')
        if row_by_col[0] == str:
            if not word_found:
                print("possible versions:")
                word_found = True
            partLanguage = row_by_col[2]
            partLanguage = partLanguage.split(':')
            partLanguage = partLanguage[0]
            print(polish_language_parts.get(partLanguage))
            print("\t" + str + ": " + row_by_col[1] + ", " + polish_language_parts.get(partLanguage))
    if not word_found:
        print("\tsorry, there is no word like this in the PoliMorf..")


def main():
    polish_dir = get_polish_dir()
    polish_language_parts = get_polish_language_parts()
    while True:
        polish_word = input("enter word: ")
        pos_tagging(polish_word, polish_dir, polish_language_parts)


if __name__ == "__main__":
    main()
