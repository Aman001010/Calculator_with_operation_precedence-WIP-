expression = input()

from operator import add, mul, sub, floordiv
operation_dictionary = {'*': mul, '/': floordiv, '+': add, '-': sub}

def evaluate_bracketless(tokens: list[str]) -> list[str]:
    index_subtractor = 0
    for index in range(len(tokens)):
        current_index = index - index_subtractor 
        current_token = tokens[current_index]        
        
        if current_index == len(tokens)-1:
            break
        
        if tokens[current_index+1] in ['*', '/']:
            tokens.insert(current_index+3, str(operation_dictionary[tokens[current_index+1]](int(current_token),int(tokens[current_index+2])) ))
            tokens.pop(current_index)
            tokens.pop(current_index)
            tokens.pop(current_index)
            
            index_subtractor += 1
        
    index_subtractor = 0
    for index in range(len(tokens)):
        current_index = index - index_subtractor 
        current_token = tokens[current_index]
        
        if current_index == len(tokens)-1:
            break
    
        if tokens[current_index+1] in ['+', '-']:
            tokens.insert(current_index+3, str(operation_dictionary[tokens[current_index+1]](int(current_token),int(tokens[current_index+2])) ))
            tokens.pop(current_index)
            tokens.pop(current_index)
            tokens.pop(current_index)
            
            index_subtractor += 1
    
    
    return tokens


print(evaluate_bracketless([i for i in expression]))