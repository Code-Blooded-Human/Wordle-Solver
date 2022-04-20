

wordlist = []
with open('data/Wordle Answers.txt','r') as f:
    for line in f:
        temp = line.split('\t')
        wordlist.append(temp[2])
textfile = open("words.txt", "w")
for element in wordlist:
    textfile.write(element)
textfile.close()