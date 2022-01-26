# Read the file
fname = input('Enter File Name ')

# Default file to test optional: mbox-short.txt
if len(fname) < 1: fname = 'clown.txt'

hand = open(fname)

dicc = dict()

for line in hand:
    words = line.split()
    for word in words:
        #Verify if the word exist, else, create  and count it
        dicc[word] = dicc.get(word,0) + 1
# print ( dicc)

bigWord = None
bigCount = None

# Go through the dictionary by keys and values (words and times) 
for word, times in dicc.items(): 
    # compare and save 
    if bigCount is None or times > bigCount:
        bigWord = word
        bigCount = times

print('The common word is "'+bigWord+'" with',bigCount,'times')
