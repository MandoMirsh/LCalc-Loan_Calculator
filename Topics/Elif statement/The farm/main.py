CHICKEN_PRICE = 23
GOAT_PRICE = 678
PIG_PRICE = 1296
COW_PRICE = 3848
SHEEP_PRICE = 6769

money = int(input())
if money < GOAT_PRICE:
    if money < CHICKEN_PRICE:
        print("None")
    else:
        chickens = money // CHICKEN_PRICE
        print(chickens, "chicken" if chickens == 1 else "chickens")
elif money < COW_PRICE:
    if money < PIG_PRICE:
        goats = money // GOAT_PRICE
        print(goats, "goat" if goats == 1 else "goats")
    else:
        pigs = money // PIG_PRICE
        print(pigs, "pig" if pigs == 1 else "pigs")
else:
    if money < SHEEP_PRICE:
        cows = money // COW_PRICE
        print(cows, "cow" if cows == 1 else "cows")
    else:
        sheep = money // SHEEP_PRICE
        print(sheep, "sheep")
