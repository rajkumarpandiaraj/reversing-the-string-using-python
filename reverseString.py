word = input('Enter the word you want to reverse : ')
reversedWord = ''
for i in range(1, len(word) + 1) :
    reversedWord += word[-i]
print(reversedWord)