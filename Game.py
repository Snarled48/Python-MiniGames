import random

pc = random.randint(10, 99)
player = 0
essai = 0

while player != pc and essai < 10:
    try:
        player = int(input("Devine le nombre compose de 2 chiffres: "))
    except ValueError:
        print("Entre un nombre valide.")
        continue
    essai += 1
    if player < pc:
        print("Le nombre est plus grand. Essais :", essai)
    elif player > pc:
        print("Le nombre est plus petit. Essais :", essai)

if player == pc:
    print("Félicitations, vous avez deviné le nombre en", essai, "essais!")
else:
    print("Désolé, vous avez atteint le nombre maximum d'essais. Le nombre était", pc)
