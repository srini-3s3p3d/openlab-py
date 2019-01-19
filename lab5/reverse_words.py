def reverseWordSentence(Sentence):
    words = Sentence.split(" ")

    newWords = [word[::-1] for word in words]

    newSentence = " ".join(newWords)

    return newSentence


infile = open('input.txt', 'r')
outfile = open('output.txt', 'w')
data = infile.read()
outfile.write(reverseWordSentence(data))