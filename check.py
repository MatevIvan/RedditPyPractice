def check(king, queen):
    """
    Given a chessboard with one K and one Q, see if the Q can attack the K.
    This function is given coordinates for the king and queen on a chessboard.
    These coordinates are given as a letter A-H for the columns and 1-8 for the
    row, like "D6" and "B7":
    """
    # ascii values for A-H are 65-72

    xDirection = 1
    yDirection = 1
    # if king and queen are in the same row or column, return true
    if (king[0] == queen[0]) or (king[1] == queen[1]):
        return True
    # find the general direction to check
    if king[0] < queen [0]:
        xDirection = -1
    if king[1] < queen[1]:
        yDirection = -1

    # set temp variable for the queen's coordinates so they can be changed
    queenLetter = ord(queen[0])
    queenNumber = (int)(queen[1])
    while True:
        if queenLetter == ord(king[0]) and queenNumber == (int)(king[1]):
            return True
        # change the queen's direction by 1 in the king's direction
        queenLetter += xDirection
        queenNumber += yDirection
        # check if in bounds
        if queenLetter < 65 or queenLetter > 72 or queenNumber < 1 or queenNumber > 8:
            return False

# Test the Code
print(check("D6","H6")) # True
print(check("E3","E7")) # True
print(check("B7","D5")) # True

print(check("D6","H7")) # False
print(check("E6","F4")) # False
print(check("B3","G4")) # False
