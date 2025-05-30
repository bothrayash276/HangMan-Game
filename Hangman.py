'''
* I have to create a list of fruits for the computer to choose
 I have to create a system which checks the letter entered by user matches the answer 
 I have to create a lives system to track the chances of user
'''
from random import randint as rd

# getting a random fruits and converting letters of fruit into list
fruits = ["Mango", "Banana", "Apple", "Orange", "Pineapple", "Watermelon"]
a = rd(0, (len(fruits)-1))
fruit = fruits[a]
fList = []
for i in fruit:
    fList.append(i)
l = len(fList)

userList = [fList[0]]
for i in range(1, l-1):
    userList.append("-")
userList.append(fList[-1])
# print(userList)



def printingSystem(l):
    st1 =""
    for i in l:
        st1 = st1 + i
    print(st1)

def gameLogic(uL, fL, l):
    
    o = 3
    print("You are given 3 Chances to guess the Letter")
    while o>0:
        user = input("Enter the letter: ")
        u = user.lower()
        b = False
        for i in range(1, l):
            if (u==fL[i]):
                uL[i] = u
                b = True
                
        
        a = uL.copy()
        a.sort()
        if(a[0]!='-'):
            break
        else:
            pass        
                
        if(b == True):
            printingSystem(uL)
        else:
            print("Wrong Guess")
            print(f"{o-1} Chances Remaining")
            o = o-1
    if (o==0):
        print("You Lost the Game")
        print("The word was: ")
        printingSystem(fL)
        
    else:
        print("Contrags, You Guessed the word: ")
        printingSystem(fL)
printingSystem(userList)
gameLogic(userList, fList, l)
