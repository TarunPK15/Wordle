#WORDLE Program
import random
print("Welcome to WORDLE!!!")
f = open(r"D:\Tarun\Class 11\Computer\PYTHON\Self\words2.txt","r")
print()
guesses = 6
words = []
data=1
for i in f:
    i=i.replace("\n","")
    words.append(i)
f.close()
for i in range(len(words)):
    words[i] = words[i].lower()
word2 = random.choice(words)
for i in range(len(words)):
    words[i] = list(words[i])
word = list(word2)
while 1:
    print("1. Rules")
    print("2. Attempt WORDLE")
    print("3. Exit")
    ch = (input("Enter 1/2/3: "))
    rules = "There will be a random 5 letter word selected every time you play!\nYou will get 6 tries to guess this word correctly.\nIf a letter in the word you guess is in the correct word, the alphabet will appear within brackets as such: (letter)\nIf the word you guess has an alphabet in the same position as it is in the final word, it will be displayed as: |letter|"
    if ch == '1':
        print(rules)
    elif ch == '2':
        while guesses > 0:
            print("You have {} guesses left!!! Good luck!!!".format(guesses))
            g = str(input("Enter guess: "))
            g = g.lower()
            g = list(g)
            if g == word:
                for x in range(len(g)):
                    print("|{}|".format(g[x]),end=" ")
                print()
                print("Well Done!!!")
                break
            elif g in words:
                woord = word[:]
                for x in range(len(g)):
                    if g[x] == woord[x]:
                        print("|{}|".format(g[x]),end=" ")
                        woord[x] = " "
                    elif g[x] in woord:
                        print("({})".format(g[x]),end=" ")
                        for y in range(len(woord)):
                            if woord[y]==g[x]:
                                woord[y]=" "
                    else:
                        print(g[x],end=" ")
                guesses = guesses - 1    
                print()
            else:
                print("Word not recognised!")
        else:
            print("Hard Luck! Try Again next time!")
            print("The word was:",word2)
    elif ch == '3':
        print("See you later!")
        break
    else:
        print("Invalid Input!\n")
