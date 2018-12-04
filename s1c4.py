import s1c1
import s1c3

def topFromList(iterable, total, depth):
    topLines = [""] * total
    topOutputs = [""] * total
    topScores = [0] * total
    topChars = [""] * total
    for line in iterable:
        arrays, scores, chars = s1c3.findCharacter(
                                     s1c1.hexStringToByteArray(line.strip()),
                                     depth)
        for i in range(len(scores)):
            if scores[i] > topScores[-1]:
                index = s1c3.updateTopList(topScores, scores[i])
                s1c3.insertTopList(topLines, line, index)
                s1c3.insertTopList(topOutputs, arrays[i], index)
                s1c3.insertTopList(topChars, chars[i], index)
            else:
                break
    return topLines, topOutputs, topScores, topChars


if __name__ == "__main__":
    lines = open("4.txt","r")
    total = 2 
    topLines, topOutputs, topScores, topChars = topFromList(lines, total, 3)  
    for i in range(total):
        print("\n",topOutputs[i])
        print("\n| Score: ",topScores[i], "\n| Using:", topChars[i], "\n| In", topLines[i], "\n___________")         
