def has_balanced_brackets(phrase: str) -> bool:
    """
    Does a given string have balanced pairs of brackets?
    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.
    Args:
        phrase: str
    Returns:
        bool
    """
    
    # This list will keep track of the next bracket that needs to close
    next_to_close = []
    # go through each character of the phrase
    for bracket in phrase:
        match bracket:
            # if the bracket is an opening bracket, add the closing braket to next_to_close
            case "(":
                next_to_close.append(")")
            case "{":
                next_to_close.append("}")
            case "[":
                next_to_close.append("]")
            case "<":
                next_to_close.append(">")
            case ")" | "}" | "]" | ">":
                # If there is a closing bracket, but no brackets are stored, return False 
                # This happens when the string begins with a closing bracket and not an opening bracket
                if len(next_to_close) > 0:
                    # Checks if the current closing bracket is equal to the last bracket saved in the array
                    if bracket == next_to_close[-1]:
                        # If correct bracket is present, remove from array and continue
                        next_to_close.pop()
                    # If the wrong bracket is found, the brackets are out of order. Return False
                    else:
                        return False
                else:
                    return False
            case _:
                continue
        
    # Return true only if the length of the array is 0 meaning that all brackets have been closed or no opening brackets have been stored
    return not(len(next_to_close))

# Test the code
print(1, has_balanced_brackets("<[{()}]>")) # True
print(2, has_balanced_brackets("<[{(yay)}]>")) # True
print(3, has_balanced_brackets("{[[This has too many open square brackets.]}")) # False
print(4, has_balanced_brackets("(This has {too many} ) closers. )")) # False
print(5, has_balanced_brackets("There(is{text[between<most>of]the}brackets)to{see(if)the}code<can>handle it!")) # True

# Test edge cases
print(6, has_balanced_brackets(" ")) # True
print(7, has_balanced_brackets(".")) # True
print(8, has_balanced_brackets("")) # True
print(9, has_balanced_brackets("<{([")) # False (only opening brackets)
print(10, has_balanced_brackets("])}>")) # False (only closing brackets)