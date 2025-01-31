import os
import pandas as pd


def read_polish_dir():
    polish_dir_file = pd.read_csv("..//poliMorf//PoliMorf-0.6.7.tab").to_string().splitlines()
    prev_word = ""
    saved_polish_dir_file = open('saved_polish_dir.txt', 'a', encoding='utf-8')
    for row in polish_dir_file:
        row = row.replace(' ', '')
        columns = row.split('\\t')
        word = columns[0]
        for char in word:
            if char.isdigit():
                word = word[1:]
        if word != prev_word:
            saved_polish_dir_file.write(word+"\n")
            prev_word = word


def get_polish_dir():
    if not os.path.exists('.//saved_polish_dir.txt'):
        read_polish_dir()
    polish_dir = open('.//saved_polish_dir.txt', 'r', encoding='utf-8').read().splitlines()
    print("\t__polish dir is loaded__")
    return polish_dir


def maxMatchAlgorithm(str, dir):
    tokens = []
    while len(str) > 0:
        word_found = False
        for i in range(len(str), 0, -1):
            first_word = str[:i]
            print(first_word)
            if first_word in dir:
                tokens.append(first_word)
                str = str[i:]
                word_found = True
                break
        if not word_found:
            tokens.append(str[0])
            str = str[1:]
    print(tokens)


def main():
    polish_dir = get_polish_dir()
    while True:
        polish_string = input("enter string without spaces: ")
        maxMatchAlgorithm(polish_string, polish_dir)


if __name__ == "__main__":
    main()
