print("Welcome to my computer quiz!")
score = 0

playing = input ('Do you want to play? (yes/no) ')
if playing.lower() == "no":
    print("fuck you")
    quit()

print("Okay! Let's play :) ")
print("For every question you you answer correctly, you gain a point")
answer = input ("Is deepwoken good? (Yes/No) ")
if answer.lower() == "no":
    print("Correct! ")
    score = score + 1
else:
    print("L bozo, fucking dog, incorrect + ratio ")



answer = input ("Is Kaz gay? (yes/no) ")
if answer.lower() == "yes":
    print("Correct! ")
    score = score + 1
else:
    print("L bozo, fucking dog, incorrect + ratio ")


answer = input ("Are you black? (Yes/No) ")
if answer.lower() == "yes":
    print("Correct! ")
    score = score + 1
else:
    print("L bozo, fucking dog, incorrect + ratio ")
print("You could've gotten up to 3 points")
print("Your score is: " + str(score))
print("You got " + str(int(score / 3 * 100)) + "% correct!")










