def help():
    print("Hello! This is a Turing Machine. A Turing Machine is cool. There is a head which can read, write or move left/right. The head reads and writes on tape which acts as memory. Turing was a cool dude")
    print("If you ever need help, type '-help'")
    print("Commands - xR to move right, xL to move left, Wx to write, S=x")
    print()
    return True

def isInt(numb):
    try:
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
        if action=="H":
            return "halt"
        return False

def identifyAction(command):
    return checkIfValid(command)
    
help()


while True:
    stateAction={} #tuple of (1/0/H,state)

    fileToOpen=input("Which program should I run? ")
    if ".txt" not in fileToOpen:
        fileToOpen+=".txt"
    program=open(fileToOpen,'r')
    contents=program.read()
    program.close()
    contents=contents.split("\n")

    valid_readBits=["H","1","0"]
    name=None
    starting_pos=None
    for line in contents:
        if line=="":
            pass
        elif line[0]=="*":
            if "STARTING_STATE" in line:
                startingState=line.split("=")[-1]
                if startingState[0]==" ":
                    try:
                        startingState=int(startingState[1:])
                    except:
                        print("Invalid starting state - should be int")
                        exit()
            if "NAME" in line:
                name=line.split("=")[-1]
                if name[0]==" ":
                    name=name[1:]
            if "STARTING_POS" in line:
                starting_pos=line.split("=")[-1]
                if starting_pos[0]==" ":
                    starting_pos=starting_pos[1:]
                try:
                    starting_pos=int(starting_pos)
                except:
                    print("Invalid starting pos - should be int")
                    exit()
        else:
            line_temp=line.split()
            if line_temp[0][0]=="S" and line_temp[1][0]=="R":
                stateNumb=line_temp[0][1:]
                readBit=line_temp[1][1:-1]
                if readBit in valid_readBits and stateNumb.isnumeric()==True:
                    stateAction[readBit,int(stateNumb)]=line.split(",")[1][1:]
                else:
                    print("Invalid command 1")
                    print(line)
                    exit()
            else:
                print("Invalid command 2")
                print(line)
                exit()
            
                


    print("Now is the time to input the tape. It may be as long as you want it to be, but it may only contain the following characters")
    print()
    print("'H' - halt bit \n 0 \n 1")

    print("Example of tape: H 1 0 0 0 0 0 0 1")
    print()
    print("====================================")

    while True:
        tape=input("Input your own tape \n").split()
        for cell in tape:
            if cell!="H" and cell!="1" and cell!="0":
                print("wrong cell: "+cell)
                print("Invalid.. starting over")
                break
        break

    if name!=None:
        print("Running "+name)
        
    print("Initial tape")
    print('|'+'|'.join(tape)+'|')

    posOnTape=starting_pos
    if posOnTape==None:
        posOnTape=int(input("Input the starting position on the tape - indexing starts from 0: "))
    state=startingState
    halt=False


    while halt==False:
        try:
            currentAction=stateAction[int(tape[posOnTape]),int(state)]
        except:
            currentAction=stateAction[tape[posOnTape],int(state)]
        for action in currentAction.split():
            whatAction=identifyAction(action)
            if whatAction=="right":
                posOnTape+=int(action.split("R")[0])
            elif whatAction=="left":
                posOnTape-=int(action.split("L")[0])
            elif whatAction=="write":
                tape[posOnTape]=action.split("W")[-1]
            elif whatAction=="state":
                state=action.split("=")[-1]
            elif whatAction=="halt":
                halt=True
                break

    print("-----------------")
    print("Final tape")
    print('|'+'|'.join(tape)+'|')
