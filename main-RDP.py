
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
#basically run through a loop to check if current token is a number if yes then return that 
# if bracket then the next token is a number so just call expression to calculate it
    global position
    global tempvar
    print("factor ",position," token: ",tokens_value[position])
    
    if(tokens_value[position][0]=="NUMBERS"):
        #tempvar=tokens_value[position][1]
        
        return tokens_value[position][1]   
    if(tokens_value[position][0]=="BR_OPEN"): #changing position-1 to position since we are checking for the current token not the previous one
        position+=1
        return expr()
    

def term():
    global position
    print("term ",position," token: ",tokens_value[position])

    
    total=factor()
    position+=1
    
    while position<len(tokens_value)-1 and (tokens_value[position][1]=="*" or tokens_value[position][1]=="/"):
        if tokens_value[position][1]== '*':
            position+=1
            temp1=factor()
            total*=temp1 # type: ignore
            position+=1
            
        elif tokens_value[position][1]== '/':
            position+=1
            temp1=factor()
            total/=temp1 # pyright: ignore[reportOperatorIssue]
            position+=1
    return total

    


def expr():
    global position
    print("expr ",position," token: ",tokens_value[position])
    
    total =0
    total = term()
     
    print("expr ",position," token: ",tokens_value[position])
    while position < len(tokens_value)-1 and (tokens_value[position][1]== '+' or tokens_value[position][1]=='-'):
        if tokens_value[position][1]== '+':
            position+=1
            temp1=term()
            total+=temp1 # type: ignore
            
        elif tokens_value[position][1]== '-':
            position+=1
            temp1=term()
            total-=temp1 # type: ignore
            
    
        
  
        
    
tempvar=0
position=0
s=input("Enter an operation ")
tokens_value=tokenization(s)        

result =expr()
print("Output: ", result)
print("tokenization: ",tokens_value)