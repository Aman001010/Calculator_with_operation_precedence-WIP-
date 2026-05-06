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
        
print(tokenization("123.4 * (12+10)"))        
