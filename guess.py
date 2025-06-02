import random

def randomword(list):
    with open(list, 'r') as file:
        line = file.readlines()
        return random.choice(line).strip()
    
word = randomword('words.txt')
word2 = randomword('words.txt')
word3 = randomword('words.txt')
word4 = randomword('words.txt')
word5 = randomword('words.txt')
word6 = randomword('words.txt')
word7 = randomword('words.txt')
word8 = randomword('words.txt')
word9 = randomword('words.txt')
word10 = randomword('words.txt')
words = [word, word2, word3, word4, word5, word6, word7, word8, word9, word10]
length = len(words)
choice = words[random.randint(0, len(words) - 1)]
lifes = 9

while lifes > 0:
    print("im thinking of a word, lets guess the word")
    wordofchoice = random.choice(words)
    print("You have " + str(lifes) + " lifes left\nq = quit\n")
    for x in words:
        print(x)
    pick = input("\nEnter word:   ")
    if pick == wordofchoice:
        print("you got it!")
        break
    


    if pick == "q":
        break

    else:
        print("nope  try again!!")
        lifes -= 1
        if pick in words:
            words.remove(pick)

    if lifes == 0:
        print("You have no lifes left, the word was: " + wordofchoice)
        input("Press enter to exit")
        break
