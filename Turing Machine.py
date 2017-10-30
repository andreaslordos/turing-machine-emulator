'''
Turing machine emulator
Allows you to input different paremeters (e.g rules, tape length, original tape), and runs your program on a virtual Turing Machine to give you a result
Uncomment all commented lines below to test a binary addition program, and if you do that then comment any line that has input() in it
'''
#responses=["7","3R S=5","3R S=5 RB","W1 5L S=5","W0 5L S=4","W0 5L S=5","W1 5L S=5","4R S=7","4R S=6","4R S=3","4R S=2","W0 5L S=4","W1 5L S=4","W1 5L S=5","W0 5L S=4","1","H 0 0 0 1 1 1 0 1 H","1"]

def help():
    print("Hello! This is a Turing Machine. A Turing Machine is cool. There is a head which can read, write or move left/right. The head reads and writes on tape which acts as memory. Turing was a cool dude")
    print("If you ever need help, type '-help'")
    print("Commands - xR to move right, xL to move left, Wx to write, S=x, RB")
    print()
    return True

def isInt(numb):
    try:
        int(numb)
        int(numb)%1
        return True
    except:
        return False
    
def checkIfValid(command):
    for action in command.split():
        if ((isInt(action.split("R")[0])==True) and (len(action.split("R"))==2) and (action.split("R")[-1]=='')):
            return "right"
        if ((isInt(action.split("L")[0])==True) and (len(action.split("L"))==2) and (action.split("L")[-1]=='')):
            return "left"
        if ((isInt(action.split("W")[-1])==True) and (len(action.split("W"))==2) and (action.split("W")[0]=='')):
            return "write"
        if ((isInt(action.split("=")[-1])==True) and (len(action.split("="))==2) and (action.split("=")[0]=="S")):
            return "state"
        if action=="RB":
            return "read"
        return False

def identifyAction(command):
    return checkIfValid(command)
    
help()
stateNumb=int(input("How many states exist? "))
#stateNumb=int(responses[0])
#responses.pop(0)

stateAction={} #tuple of (1/0,state)

for x in range(stateNumb):
    for y in range(2):
            while True:
                print("What should I do if the state is "+str(x+1)+" and I'm reading a "+str(y)+"?")
                #command=input()
                command=responses[0]
                responses.pop(0)
                if command=="-help":
                    help()
                else:
                    if checkIfValid(command)!=False:
                        stateAction[(y,x+1)]=command.split()
                        break
                    else:
                        print("Invalid! Lets try that again.")

startingState=int(input("Starting state: "))
3startingState=int(responses[0])
#responses.pop(0)

print("Now is the time to input the tape. It may be as long as you want it to be, but it may only contain the following characters")
print()
print("'H' - halt bit \n 0 \n 1")

print("Example of tape: H 1 0 0 0 0 0 0 1")
print()
print("====================================")

while True:
    tape=input("Input your own tape \n").split()
    #tape=responses[0].split()
    #responses.pop(0)
    for cell in tape:
        if cell!="H" and cell!="1" and cell!="0":
            print("wrong cell: "+cell)
            print("Invalid.. starting over")
            break
    break
print("Initial tape")
print('|'+'|'.join(tape)+'|')
posOnTape=int(input("Input the starting position on the tape - indexing starts from 0"))
#posOnTape=int(responses[0])
#responses.pop(0)
state=startingState
halt=False


while True:
    if halt==True:
        break
    currentAction=stateAction[int(tape[posOnTape]),int(state)]
    for action in currentAction:
        whatAction=identifyAction(action)
        if whatAction=="read":
            pass
        elif whatAction=="right":
            posOnTape+=int(action.split("R")[0])
            if tape[posOnTape]=="H":
                for x in range(4):
                    tape[x+1]="0"
                    halt=True
        elif whatAction=="left":
            posOnTape-=int(action.split("L")[0])
            if tape[posOnTape]=="H":
                for x in range(4):
                    tape[x+1]="0"
                halt=True
        elif whatAction=="write":
            tape[posOnTape]=action.split("W")[-1]
        elif whatAction=="state":
            state=action.split("=")[-1]
print("-----------------")
print("Final tape")
print('|'+'|'.join(tape)+'|')
