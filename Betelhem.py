import random
#iteration = input("How many times do you want to play: ")
count_user = 0
count_computer = 0
count_draw = 0
Game_list = ["rock","scissor","paper"]
#for i in range(int(iteration)):
while(True):
    computer_choice = random.choice(Game_list)
    user_choice =input("Enter your choice from [Rock, Scissor, Paper]: ")
    if user_choice.lower() == computer_choice.lower():
        print("draw")
        count_draw = count_draw + 1
    elif user_choice.lower() == "rock" and computer_choice == "scissor":
        print("You win me, because I choice " + computer_choice)
        count_user = count_user + 1
    elif user_choice.lower() == "paper" and computer_choice == "rock":
        print("You win me, because I choice " + computer_choice)
        count_user = count_user + 1
    elif user_choice.lower() == "scissor" and computer_choice == "paper":
        print("You win me, because I choice " + computer_choice)
        count_user = count_user + 1
    elif user_choice.lower() == "scissor" and computer_choice == "rock":
        print("I win you, because I choice " + computer_choice)
        count_computer = count_computer + 1
    elif user_choice.lower() == "rock" and computer_choice == "paper":
        print("I win you, because I choice " + computer_choice)
        count_computer = count_computer + 1
    elif user_choice.lower() == "paper" and computer_choice == "scissor":
        print("I win you, because I choice " + computer_choice)
        count_computer = count_computer + 1
    elif user_choice.lower()!="paper" and user_choice.lower()!="rock" and user_choice.lower()!="scissor":
        print("You do not choice the right thing, please try again")
        continue
    user_want = input("Do you want to play again(y/n): ")
    if user_want == 'y':
        continue
    else:
        break  
print("***************** RESULT ******************")
print("you win me " + str(count_user) + " times")
print("I win you " + str(count_computer) + " times")
print("we choice the same thing " + str(count_draw) + " times")