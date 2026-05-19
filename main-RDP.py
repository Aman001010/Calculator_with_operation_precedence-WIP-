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
    
    if(tokens_value[position][0]=="NUMBERS"):
        position+=1
        return tokens_value[position-1][1]   
    if(tokens_value[position-1][0]=="BR_OPEN"):
        position+=1
        return term()
    

def term():
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
            position-=1
            expr()
        elif(tokens_value[position-1][0]=="BR_OPEN"):
            position+=1
            return expr()


def expr():
    temp1=term()
    if(tokens_value[position][0]=="OP"):
        if(tokens_value[position][1]=='+'):
            position+=1
            if(tokens_value[position][0]=="NUMBERS"):
                temp2=term()
                temp1+=temp2
                return temp1
            else:
                print("invalid operation")
        elif(tokens_value[position][1]=='-'):
            position+=1
            if(tokens_value[position][0]=="NUMBERS"):
                temp2=term()
                temp1-=temp2
                
                return temp1 
        
    

position=0
tokens_value=tokenization("123.4 * (12+10)")        