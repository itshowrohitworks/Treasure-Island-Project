# Welcome Message:
print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")

# Inputs:
leftorright = input("You're at a cross road. Where do you want to go?\nType 'left' or 'right'")
if leftorright == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    waitorswim = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    if waitorswim == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        print("One red, one yellow and one blue.")
        doorcolour = input("Which colour do you choose?")
        if doorcolour == "red":
            print("It's a room full of fire. Game Over!")
        elif doorcolour == "yellow":
            print("You found the treasure! You win lol!")
        elif doorcolour == "blue":
            print("You enter a room of beasts. Game Over!")
        else:
            print("Please type a colour...! Sorry mate, I understand you can't even choose this lol!")
    elif waitorswim == "swim":
        print("You get attacked by an angry trout. Game Over!")
    else:
        print("Please type a wait to move forward in life lol!")
elif leftorright == "right":
    print("You fell into a hole. Game Over!")
else:
    print("You can't even decide left or right, What's you gonna do with your life lol!")