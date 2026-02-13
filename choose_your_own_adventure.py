name = input("Type your name? ")

print("Welcome", name, "to this adventure")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around or swim accross, type walk to walk around or swim to swim accross")

    if answer == "walk":
        print("Yoy walked for many miles, ran out of water and died from dehydration")

    elif answer == "swim":
        print("You swam accross and were eaten by an alligator")

    else:
        print("Not a valid answer, you lose.")


elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it, or head back? (cross/back)")

    if answer == "cross":
        print("A killer was on the loose and killed you")
    
    elif answer == "back":
        answer = input("On your way back you see a new path, do you want to follow it? (yes/no)")

        if answer == "yes":
            ...
        
        elif answer == "no":
            ...
        
        else:
            print("Not a valid answer, you lose.")

    else:
        print("Not a valid answer, you lose.")





else:
    print("Not a valid answer, you lose.")