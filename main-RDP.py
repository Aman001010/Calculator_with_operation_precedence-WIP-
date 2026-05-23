""" for 12+10:
expr 0 token numbers 12
factor 0 token numbers 12
factor 2 token numbers 10
output 22.0

for 123*4+7-(23+4):
expr 0 token numbers 123
factor 0 token numbers 123
term 1 token op *
output none

debug/solve tomm ahead
"""
def tokenization(token_text):
    tokens=[]
    i=0
    while i<len(token_text):
        
        if token_text[i].isdigit():
            char=token_text[i]
            i+=1
            while i<len(token_text) and (token_text[i].isdigit() or token_text[i]=='.'):
                char+=token_text[i]
                i+=1
            tokens.append(("NUMBERS",float(char)))
        elif token_text[i] in '+*/-':
            tokens.append(("OP",token_text[i]))
            i+=1
        elif token_text[i] == '(':
            tokens.append(("BR_OPEN",token_text[i]))
            i+=1 
        elif token_text[i] == ')':
            tokens.append(("BR_CLOSE",token_text[i]))
            i+=1 
        elif token_text[i] == ' ': 
            i+=1
            pass
        else:
            raise ValueError(("Wrong input"))
    return tokens


def factor():
#basically run through a loop to check if current token is a number if yes then return that if bracket then the next token is a number so just call expression to calculate it
    global position
    print("factor ",position," token: ",tokens_value[position])
    
    if(tokens_value[position][0]=="NUMBERS"):
        position+=1
        return tokens_value[position-1][1]   
    if(tokens_value[position][0]=="BR_OPEN"): #changing position-1 to position since we are checking for the current token not the previous one
        position+=1
        return term()
    

def term():
    global position
    print("term ",position," token: ",tokens_value[position])

    if(tokens_value[position][0]=="NUMBERS"):
        temp1=factor()
        if(tokens_value[position][0]=="OP"):
            if(tokens_value[position][1]=='*'):
                position+=1
                if(tokens_value[position][0]=="NUMBERS"):
                    temp2=factor()
                    temp1*=temp2
                    return temp1
                else:
                    print("invalid operation")
            elif(tokens_value[position][1]=='/'):
                position+=1
                if(tokens_value[position][0]=="NUMBERS"):
                    temp2=factor() 
                    temp1/=temp2
                
                    return temp1 
            elif(tokens_value[position][1]=='+' or tokens_value[position][1]=='-'):
                position -=1
                return expr()
        elif(tokens_value[position][0]=="BR_OPEN"):
            position+=1
        return expr()


def expr():
    global position
    print("expr ",position," token: ",tokens_value[position])

    if(tokens_value[position][0]=="BR_OPEN"):
        position+=1
        return expr()
    if(tokens_value[position][0]=="NUMBERS"):
        temp1=factor()
    
        if(tokens_value[position][0]=="OP"):
            if(tokens_value[position][1]=='+'):
                position+=1
                if(tokens_value[position][0]=="NUMBERS"):
                    temp2=factor()
                    temp1+=temp2
                    return temp1
                else:
                    print("invalid operation")
            elif(tokens_value[position][1]=='-'):
                position+=1
                if(tokens_value[position][0]=="NUMBERS"):
                    temp2=factor()
                    temp1-=temp2
                
                    return temp1 
            else:
                return term()

  
        
    

position=0
s=input("Enter an operation ")
tokens_value=tokenization(s)        

result =expr()
print("Output: ", result)
print("tokenization: ",tokens_value)