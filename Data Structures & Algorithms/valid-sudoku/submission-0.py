class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #COLUMN CHECK

        #col_check = set() #sets cant have dups
        for col_index, column in enumerate(zip(*board)):
            col_check = set() #sets cant have dups, needs to be here so that it resets for each column 
            #print(f"Column: {column}")
            #print(type(column))
        
            for col_value in column:
                if col_value == ".":
                    continue 
                if (col_value not in col_check):
                    col_check.add(col_value)
                else:
                    print(f"False, value {col_value} is a duplicate in this column") #remove at the end
                    return False
        
        #print("All cols checked - Cols are valid")

                        
        # ROW CHECK
        for row in board:
            #print(row)
            row_check = set()

            for row_val in row:
                if row_val == ".":
                    continue

                if row_val not in row_check:
                    row_check.add(row_val)
                else:
                    print(f"False, value {row_val} is a duplicate in this row") #remove at the end
                    return False

        #print("All rows checked - Rows are valid")
            

        # 3x3 CHECK
        for row_box in range(0,9,3):
            for col_box in range(0,9,3):
                print(f"Box coords: ({row_box},{col_box})")

                grid_3_x_3_check = set() 
                for row in range(row_box, row_box+3):
                    for col in range(col_box, col_box+3):
                        #print(f"This is cell: {board[row][col]}")
                    #print()
                #print()
                        value = board[row][col]

                        if value == ".":
                            continue
                        
                        if value not in grid_3_x_3_check:
                            grid_3_x_3_check.add(value)
                        else:
                            print(f"False, value {value} is a duplicate in this 3x3 grid")
                            return False

        print("All 3x3 grids checked - 3x3 Grids are valid")

        return True  

