import random


def number():
    correct_answer = random.randint(1, 100)
    return correct_answer


def main():
    while True:
        answer1 = input("Do you want to start a game? put in 'y' or 'n'")
        if answer1 is "n":
            print("ok")
            break
        elif answer1 is "y":
            print("let's start")
            answer2 = number()
            while True:
                users_guess = int(input("Give a number you want to guess."))
                if users_guess == answer2:
                    print("Congratulation!")
                    break
                elif users_guess > answer2:
                    print("your guess was too high")
                else:
                    print("Your guess was too low")
        else:
            print("your answer is not valid")


main()