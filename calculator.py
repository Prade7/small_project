
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1//n2
first = True
while(True):   
    if(first):
        first = False
        n1 = eval(input("Please enter a value - "))
        n2 = eval(input("please enter a value - "))
        action = input(" type add , sub , mul, div and q for quit ")
        if(action =="add"):
            result = add(n1,n2)
            print(result)
        elif(action == "sub"):
            result = subtract(n1,n2)
            print(result)
        elif(action == "mul"):
            result = multiply(n1,n2)
            print(result)
        elif(action == "div"):
            result = div(n1,n2)
            print(result)
        elif(action =="q"):
            break
        else:
            print("error")
    else:
        func = input("type add , sub , mul, div and q for quit ")
        if(func == "add"):
            inp = eval(input())
            result = add(inp,result)
            print(result)
        elif(func == "sub"):
            inp = eval(input())
            result= subtract(result,inp)
            print(result)
        elif(func == "mul"):
            inp = eval(input())
            result = multiply(result,inp)
            print(result)
        elif(func == "div"):
            inp = eval(input())
            result = div(result,inp)
        elif(func =="q"):
            break
