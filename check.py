def check(king: str, queen: str) -> bool:
    """
    Given a chessboard with one K and one Q, see if the Q can attack the K.
    This function is given coordinates for the king and queen on a chessboard.
    These coordinates are given as a letter A-H for the columns and 1-8 for the
    row, like "D6" and "B7"

    Args:
        king (str): length of 2
        queen (str): length of 2
    Returns:
        bool: True if king is in line of sight of queen, False otherwise
    """
    # ascii values for A-H are 65-72

    queen = queen[0].upper() + queen[1]
    king = king[0].upper() + king[1]

    # handle input errors
    if not(len(queen) == 2  and len(king) == 2 and 65 <= ord(queen[0]) <= 72 and 1 <= int(queen[1]) <= 8 and 65 <= ord(king[0]) <= 72 and 1 <= int(king[1]) <= 8):
        print(f"\nInput error. Given input: \nKing: {king}\nQueen: {queen}\n")
        return False

    row_direction = 1
    column_direction = 1
    # if king and queen are in the same row or column, return true
    if (king[0] == queen[0]) or (king[1] == queen[1]):
        return True
    # find the general direction to check
    if king[0] < queen [0]:
        row_direction = -1
    if king[1] < queen[1]:
        column_direction = -1

    # set temp variable for the queen's coordinates so they can be changed
    queen_letter = ord(queen[0])
    queen_number = (int)(queen[1])
    while True:
        if queen_letter == ord(king[0]) and queen_number == (int)(king[1]):
            return True
        # change the queen's direction by 1 in the king's direction
        queen_letter += row_direction
        queen_number += column_direction
        # check if in bounds
        if queen_letter < 65 or queen_letter > 72 or queen_number < 1 or queen_number > 8:
            return False

# Test the Code
print(check("D6","h6")) # True
print(check("e3","E7")) # True
print(check("B7","d5")) # True

print(check("D0","g1")) # False
print(check("E6","F4")) # False
print(check("B3","G4")) # False
