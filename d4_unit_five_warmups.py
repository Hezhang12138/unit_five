while True:
    answer = input("Do you want to start a game? put in 'y' or 'n'")
    if answer is "n":
        print("ok")
        break
    elif answer is "y":
        print("let's start")
        break
    else:
        print("that is not valid")

print("you did it")