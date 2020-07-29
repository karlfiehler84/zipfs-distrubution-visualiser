from operator import itemgetter
import matplotlib.pyplot as plt

def main(file):
    wordList = []
    secondList = []
    inFile = open(file, "r", encoding="utf8")

    for line in inFile:
        for word in line.split():
            wordList.append(word)
            print("read through " + str(len(wordList)) + " words")

    for word in wordList:
        if [word, wordList.count(word)] not in secondList:
            x = wordList.count(word)
            pair = [word, x]
            secondList.append(pair)
            print("indexed " + str(len(secondList)) + " words")

    def getNumOnly(list):
        lost = []
        for item in list:
            lost.append(item[1])
        return lost

    z = sorted(getNumOnly(secondList))
    plt.plot(z)
    plt.ylabel("amount of occurences")
    plt.xlabel("index of word")
    plt.gca().invert_xaxis()
    plt.show()

x = input("specify file name: ")
main(x)