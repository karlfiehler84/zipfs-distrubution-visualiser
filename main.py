from operator import itemgetter
import matplotlib.pyplot as plt

def main(file):
    wordList = []
    indexList = []
    numOnly = []
    inFile = open(file, "r", encoding="utf8")

    for line in inFile:
        for word in line.split():
            wordList.append(word)
            print("read through " + str(len(wordList)) + " words")

    for word in wordList:
        if [word, wordList.count(word)] not in indexList:
            x = wordList.count(word)
            pair = [word, x]
            indexList.append(pair)
            print("indexed " + str(len(indexList)) + " words")

    for item in indexList:
        numOnly.append(item[1])

    z = sorted(numOnly)
    plt.plot(z)
    plt.ylabel("amount of occurences")
    plt.xlabel("index of word")
    plt.gca().invert_xaxis()
    plt.show()

x = input("specify file name: ")
main(x)