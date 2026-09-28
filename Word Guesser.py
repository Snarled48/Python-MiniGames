from random import randint

WORD_LENGTH = 5
MAX_TRIES = 14

mot = "".join(chr(randint(65, 90)) for _ in range(WORD_LENGTH))
ch = "*" * WORD_LENGTH

for nb in range(1, MAX_TRIES + 1):
    essai = input("Your try: ").upper()
    for i in range(min(len(essai), WORD_LENGTH)):
        if essai[i] == mot[i]:
            ch = ch[:i] + essai[i] + ch[i+1:]
    print(ch)
    if essai == mot:
        print("You Won!")
        print("Number Of Tries:", nb)
        break
else:
    print("You Lost!! The Word Was", mot)
    print("Number Of Tries:", MAX_TRIES)
