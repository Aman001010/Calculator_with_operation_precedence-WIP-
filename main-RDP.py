
from typing import TypeAlias


Token: TypeAlias = tuple[str, str | float]
tokens_value: list[Token] = []
position = 0


class ParseError(ValueError):
    """Raised when an expression cannot be parsed."""


def tokenization(token_text: str) -> list[Token]:
    tokens: list[Token] = []
    i = 0
    while i<len(token_text):

        if token_text[i].isdigit() or token_text[i] == '.':
            char = token_text[i]
            i += 1
            while i < len(token_text) and (
                token_text[i].isdigit() or token_text[i] == '.'
            ):
                char += token_text[i]
                i += 1
            if char.count('.') > 1 or char == '.':
                raise ParseError(f"Invalid number: {char!r}")
            tokens.append(("NUMBERS", float(char)))
        elif token_text[i] in '+*/-':
            tokens.append(("OP",token_text[i]))
            i+=1
        elif token_text[i] == '(':
            tokens.append(("BR_OPEN",token_text[i]))
            i+=1 
        elif token_text[i] == ')':
            tokens.append(("BR_CLOSE",token_text[i]))
            i+=1 
        elif token_text[i].isspace():
            i+=1
        else:
            raise ParseError(f"Unexpected character: {token_text[i]!r}")
    return tokens


def factor() -> float:
#basically run through a loop to check if current token is a number if yes then return that 
# if bracket then the next token is a number so just call expression to calculate it
    global position

    if position >= len(tokens_value):
        raise ParseError("Expected a number or '('")

    if tokens_value[position][0] == "OP" and tokens_value[position][1] in ("+", "-"):
        operator = tokens_value[position][1]
        position+=1
        value = factor()
        return value if operator == "+" else -value

    token_type, value = tokens_value[position]
    position += 1
    if token_type == "NUMBERS":
        return float(value)
    if token_type == "BR_OPEN":
        result = expr()
        if position >= len(tokens_value) or tokens_value[position][0] != "BR_CLOSE":
            raise ParseError("Missing closing parenthesis")
        position += 1
        return result
    raise ParseError(f"Expected a number or '(', got {value!r}")


def term() -> float:
    global position
    total = factor()
    while position < len(tokens_value) and tokens_value[position][0] == "OP" and tokens_value[position][1] in ("*", "/"):
        operator = tokens_value[position][1]
        position += 1
        temp1 = factor()
        if operator == '*':
            total *= temp1
        elif temp1 == 0:
            raise ParseError("Division by zero")
        else:
            total /= temp1
    return total


def expr() -> float:
    global position
    total = term()
    while position < len(tokens_value) and tokens_value[position][0] == "OP" and tokens_value[position][1] in ("+", "-"):
        operator = tokens_value[position][1]
        position += 1
        temp1 = term()
        if operator == '+':
            total += temp1
        else:
            total -= temp1
    return total


def evaluate(expression: str) -> float:
    """Evaluate an expression while enforcing complete token consumption."""
    global position, tokens_value
    tokens_value = tokenization(expression)
    if not tokens_value:
        raise ParseError("Expression cannot be empty")
    position = 0
    result = expr()
    if position != len(tokens_value):
        raise ParseError(f"Unexpected token: {tokens_value[position][1]!r}")
    return result


if __name__ == "__main__":
    s = input("Enter an operation ")
    try:
        result = evaluate(s)
    except ParseError as error:
        print(f"Error: {error}")
    else:
        print("Output:", result)