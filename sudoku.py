'''
         As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:

         each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
         each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
         each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.
         If you need more details, you can find them here.

    Your task is to write a program which:

    reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
    outputs Yes if the Sudoku is valid, and No otherwise.
    Test your code using the data we've provided.

    Test data
    Sample input:
    
    2 9 5 7 4 3 8 6 1
    4 3 1 8 6 5 9 2 7
    8 7 6 1 9 2 5 4 3
    3 8 7 4 5 9 2 1 6
    6 1 2 3 8 7 4 9 5
    5 4 9 2 1 6 7 3 8
    7 6 3 5 2 4 1 8 9
    9 2 8 6 7 1 3 5 4
    1 5 4 9 3 8 6 7 2
    
    Sample output:

    True


    Sample input:

    1 9 5 7 4 3 8 6 2
    4 3 1 8 6 5 9 2 7
    8 7 6 1 9 2 5 4 3
    3 8 7 4 5 9 2 1 6
    6 1 2 3 8 7 4 9 5
    5 4 9 2 1 6 7 3 8
    7 6 3 5 2 4 1 8 9
    9 2 8 6 7 1 3 5 4
    2 5 4 9 3 8 6 7 1
    
    Sample output:

    False

'''
# A function that checks whether a list passed as an argument contains
# nine digits from '1' to '9'.
def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]


# A list of rows representing the sudoku.
rows = []
for r in range(9):
    ok = False
    while not ok:
        row = input().replace(' ','')
        ok = len(row) == 9 or row.isdigit()
        if not ok:
            print("Incorrect row data - 9 digits required")
    rows.append(row)

ok = True

# Check if all rows are good.
for r in rows:
    if not checkset(r):
        ok = False
        break

# Check if all columns are good.	
if ok:
    for c in range(9):
        col = []
        for r in range(9):
            col.append(rows[r][c])
        if not checkset(col):
            ok = False
            break

# Check if all sub-squares (3x3) are good.
if ok:
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            sqr = ''
            # Make a string containing all digits from a sub-square.
            for i in range(3):
                sqr += rows[r+i][c:c+3]
            if not checkset(list(sqr)):
                ok = False
                break

# Print the final verdict.
if ok:
    print("True")
else:
    print("False")
