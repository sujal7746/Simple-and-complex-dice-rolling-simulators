from itertools import repeat
from  random import randint                   #from the random module import the randint function

repeat = True                                 #Create boolean control variable
while repeat:                                 #endless while loop until repeat no longer is true
    print("you rollled", randint(1, 6)) #random num between 1 to 6
    print("Do you want to roll again?")
    rsp = input().lower().strip()             #read input from console, cast to lower and remove whitespace
    repeat = ("y" == rsp) or ("yes" == rsp)   #continue loop if "y" or "yes"
print("*** End of Game ***")                  #after the loop
