from operator import itemgetter
import matplotlib.pyplot as plt

def main(file):
    wordList = []
    secondList = []
    distrList = []
    inFile = open(file, "r", encoding="utf8")

    for line in inFile:
        for word in line.split():
            wordList.append(word)

    for word in wordList:
        if [word, wordList.count(word)] not in secondList:
            x = wordList.count(word)
            pair = [word, x]
            secondList.append(pair)

    def getDist(sum, item):
        return item / sum * 100

    for pair in secondList:
        distr = (getDist(len(wordList), pair[1]))
        distrList.append([pair[0], distr])

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