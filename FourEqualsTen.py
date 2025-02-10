from random import randint as ri
from os import system as sys
from random import shuffle as shuf


goal = 10

def eq10(nums):
    ops = ["+","-","/","*"]
    brac = ["(",  ")",  " "]
    evaled = 0
    tries = 0
    while True:
        shuf(nums)
        num_str = f"{brac[ri(0,2)]}{nums[0]} {ops[ri(0,3)]} {brac[ri(0,2)]}{nums[1]}{brac[ri(0,2)]} {ops[ri(0,3)]} {brac[ri(0,2)]}{nums[2]}{brac[ri(0,2)]} {ops[ri(0,3)]} {nums[3]}{brac[ri(0,2)]}"
        try:
            if num_str.count("(") >= 2 or num_str.count(")") >= 2:
                continue
            else:
                if num_str.count("(") != num_str.count(")"):
                    continue
                evaled = eval(num_str)
        except:
            exit
            sys("clear")
        if evaled == 10:
            sys("clear")
            #debug v
            print(tries)
            print(num_str)
            #debug ^
            return True
        else:
            tries+=1
        if tries >= 500:
            return False

def FourTen():
    fail = False
    nums = [ri(0,9), ri(0,9), ri(0,9), ri(0,9)]
    if not eq10(nums):
        again = str(input("Sorry but something went wrong\nPlease press ENTER: ")).lower()
        if again == "":
            FourTen()
        else:
          print("see ya")
          exit()
    nums[0] = str(nums[0])
    nums[1] = str(nums[1])
    nums[2] = str(nums[2])
    nums[3] = str(nums[3])
    
    print("Characters: + - × ÷ ( )\n")
    print(nums[0], nums[1], nums[2], nums[3])
    user = str(input(": ")).lower()
    user = user.replace("×", "*").replace("÷","/").replace("x","*")
    if (nums[0] not in user) or (nums[1] not in user) or (nums[2] not in user) or (nums[3] not in user) or (len(user) < 4):
        fail = True
        print("You messed up somthing you Typed")
    try:
        eval(user)
    except:
        print('Please try somthing like 1+2+3+4')
    if eval(user) == goal and fail == False:
        print(f"You win! {user} = {eval(user)}\nPlay again?")
        play_ag = input("y/n: ")
        if play_ag == "y":
            sys("clear")
            FourTen()
        else:
            exit()
    elif len(user) <= 6:
        print("Not good enough")
        exit()
    else:
        print(f"You lose, {user} = {eval(user)}\nTry again?")
        play_ag = input("y/n: ")
        if play_ag == "y":
            sys("clear")
            FourTen()
        else:
            exit()

FourTen()