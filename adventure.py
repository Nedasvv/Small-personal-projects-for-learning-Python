def retry_or_quit():
    answer = input("Would you like to try again? ").lower()
    if answer == "yes":
        game()
    else:
        quit()
def game():
     while True:
        while True:
            name = input("Choose your name: ")
            print("Welcome ", name, " to your own adventure! ")

            answer = input("You are on a dirt road, it has come to an end and you can choose to go left or right. Type in 'left' to choose the left side, 'right' for the right side. ").lower()

            if answer == "left":
                answer = input("You come across a river, type in 'swim' to swim across and 'walk' to walk around it. ").lower()

                if answer == "swim":
                    print("You were caught and eaten by an alligator. ")
                    retry_or_quit()
                
                elif answer == "walk":
                    answer = input("While walking, you've stumbled upon a humble village, type 'stay' to sleep there for a night or 'leave' to walk past it. ").lower()
                    if answer == "stay":
                        print("You were intentionally poisoned by the villagers and died. ")
                        retry_or_quit()
                    elif answer == "leave":
                        print("You were too dehydrated to keep walking and passed out in the middle of nowhere, died to malnutrition and dehydration. ")
                        retry_or_quit()

            elif answer == "right":
                answer = input("You've met a mysterious old man, type in 'talk' to speak with him and 'walk' to walk past him. ").lower()
                if answer == "walk":
                    print("You walk past him and glance at him, he notices you looking at him and shoots you. ")
                    retry_or_quit()
                elif answer == "talk":
                    answer = input("You grab a beer with the old man, he asks you to help him rob a bank 'agree' to rob a bank with him, 'disagree' to disagree. ").lower()
                    if answer == "agree":
                        print("You both attempted to rob a nearby bank, the security guards shot you on the spot. ")
                        retry_or_quit()
                    elif answer == "disagree":
                        print("He walks away and you feel a sharp pain in your neck, a knife has been lodged into your body and you bleed out. ")
                        retry_or_quit()                 
if __name__ == '__main__':
  game()