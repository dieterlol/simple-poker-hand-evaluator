# made by dieter
# started on 8/21/20

import random
import statistics

startgame = input("press enter to play. ")
while startgame != "":
    startgame = input("press enter to play. ")

while True:
    while True:
        cardranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        cardsuits = ["hearts", "diamonds", "spades", "clubs"]

        randomranks = random.choices(cardranks, k=5)
        randomsuits = random.choices(cardsuits, k=5)

        # making sure no 5 of a kind
        popnumber = random.randint(0, 4)
        while randomranks.count(randomranks[0]) == 5:
            randomranks[popnumber] = random.choice(cardranks)
        # making sure no duplicate cards
        cardlist = [
            [randomranks[0], randomsuits[0]],
            [randomranks[1], randomsuits[1]],
            [randomranks[2], randomsuits[2]],
            [randomranks[3], randomsuits[3]],
            [randomranks[4], randomsuits[4]],
        ]
        for x in cardlist:
            if cardlist.count(x) > 1:
                duplicates = True
                break
            else:
                duplicates = False

        if duplicates is True:
            continue
        else:
            break

    # dictionary for every card rank
    cardconvert = {
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "Jack",
        12: "Queen",
        13: "King",
        14: "Ace"
    }
    print("\nyour cards are:")
    print(cardconvert[(randomranks[0])] + " of " + str(randomsuits[0]))
    print(cardconvert[(randomranks[1])] + " of " + str(randomsuits[1]))
    print(cardconvert[(randomranks[2])] + " of " + str(randomsuits[2]))
    print(cardconvert[(randomranks[3])] + " of " + str(randomsuits[3]))
    print(cardconvert[(randomranks[4])] + " of " + str(randomsuits[4]))


    # sorting cards to make them easier to calculate
    randomranks.sort()
    randomsuits.sort()
    if randomsuits[0] == randomsuits[4]:
        samesuit = True
    else:
        samesuit = False



    ranksum = sum(randomranks)
    rankaverage = ranksum / 5

    # checking every type of hand
    def check_royal():
        if samesuit is True and rankaverage == 12 and randomranks[4] - randomranks[0] == 4 and randomranks[4] - randomranks[1] == 3:
            return True
        else:
            return False

    def check_straight_flush():
        if samesuit is True and rankaverage == randomranks[2] and randomranks[4] - randomranks[0] == 4 and randomranks[4] - randomranks[1] == 3:
            return True
        else:
            return False

    def check_four_of_a_kind():
        if randomranks.count(statistics.mode(randomranks)) == 4:
            return True
        else:
            return False

    def check_full_house():
        if randomranks[0] == randomranks [1] == randomranks [2] and randomranks [3] == randomranks[4]:
            return True
        elif randomranks [2] == randomranks[3] == randomranks [4] and randomranks[0] == randomranks[1]:
            return True
        else:
            return False

    def check_flush():
        if samesuit is True:
            return True
        else:
            return False

    def check_straight():
        if rankaverage == randomranks[2] and randomranks[4] - randomranks[0] == 4 and randomranks[4] - randomranks[1] == 3:
            return True
        else:
            return False

    def check_three_of_a_kind():
        if randomranks.count(statistics.mode(randomranks)) == 3:
            return True
        else:
            return False

    def check_two_pairs():
        if randomranks[0] == randomranks[1] and randomranks[2] == randomranks[3]:
            return True
        elif randomranks[0] == randomranks[1] and randomranks[3] == randomranks[4]:
            return True
        elif randomranks[1] == randomranks[2] and randomranks[3] == randomranks[4]:
            return True
        else:
            return False

    def check_pair():
        if randomranks.count(statistics.mode(randomranks)) == 2:
            return True
        else:
            return False

    if check_royal() is True:
        print("\nRoyal flush! The odds of this hand are 1 in 649,740.\n")
    elif check_straight_flush() is True:
        print("\nStraight flush! The odds of this hand are 1 in 72,193.\n")
    elif check_four_of_a_kind() is True:
        print("\nFour of a kind! The odds of this hand are 1 in 4,166.\n")
    elif check_full_house() is True:
        print("\nFull house! The odds of this hand are 1 in 694.\n")
    elif check_flush() is True:
        print("\nFlush! The odds of this hand are 1 in 510.\n")
    elif check_straight() is True:
        print("\nStraight! The odds of this hand are 1 in 235.\n")
    elif check_three_of_a_kind() is True:
        print("\nthree of a kind! The odds of this hand are 1 in 47.\n")
    elif check_two_pairs() is True:
        print("\nTwo pairs! The odds of this hand are 1 in 21.\n")
    elif check_pair() is True:
        print("\nPair! The odds of this hand are ~42%.\n")
    else:
        print("\nhigh card ("+ cardconvert[(randomranks[4])] +")! The odds of this hand are ~50%.\n")

    # play again
    playagain = input("press enter to play again. ")
    while playagain != "":
        playagain = input("press enter to play again. ")
