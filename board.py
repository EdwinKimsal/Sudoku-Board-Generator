# Import(s)
import random
import copy
import time

# check_board function
def check_board(board):
    # Iterate through each block in board (left -> right, top -> down)
    for y in range(len(board)):
        for x in range(len(board)):
            # Check horizontal row
            if len(board[y]) > x + 1:
                if board[y][x] in board[y][x + 1:]:
                    if board[y][x] != "-":
                        return False

            # Check vertical row using temp list
            temp = []
            for i in range(len(board) - y - 1):
                if len(board[i + y + 1]) > x:
                    temp.append(board[i + y + 1][x])

            if len(board[y]) > x:
                if board[y][x] in temp:
                    if board[y][x] != "-":
                        return False

            # Check block of nine using temp list
            temp = []
            for i in range(3):
                for j in  range(3):
                    if 3*(y//3) + i != y and 3*(x//3) + j != x:
                        if board[3*(y//3) + i][3*(x//3) + j] != "-":
                            temp.append(board[3*(y//3) + i][3*(x//3) + j])

            if board[y][x] in temp:
                    return False

    # If no return, board is valid
    return True


# Merge solution and board function
def merge(board, solution):
    """
    Merges two parameters, board and solution,
    and returns the merged result
    """

    # Perform a deep copy of the board
    m_board = copy.deepcopy(board)

    # Set count to 0
    count = 0

    # Iterate through each block in the board
    for i in range(9):
        for j in range(9):
            # If the block is empty and a valid block, add the solution
            if m_board[i][j] == "-":
                if count < len(solution):
                    m_board[i][j] = solution[count]
                    count += 1

    # Return the merged board
    return m_board


# Solve board function
def solve_board(board):
    """
    Solves the parameter board using brute force
    and returns the solved board
    """

    # Set vars
    solution = [1] # Start with 1
    is_complete = False # Initially false

    # Iterate until is_complete is True
    while is_complete is False:
        # Merge board and check if it is valid
        merged_board = merge(board, solution)
        is_valid = check_board(merged_board)

        # If valid, check if the solution is complete
        if is_valid is True:
            if len(solution) == 54:
                is_complete = True

            else:
                solution.append(1)

        # If not valid, increment as needed
        else:
            solution[-1] += 1

            while solution[-1] > 9:
                solution.pop()
                solution[-1] += 1

    # Return the solved board
    return merge(board, solution)


# Rand block gen function
def block_gen():
    """
    Generates three individual blocks,
    one block is one nested list and
    returns a list of lists
    """

    # Set list to a blank list of lists
    list = [[], [], []]

    # Iterate through each block and ele in each block
    for i in range(3):  # 3 blocks
        for j in range(9):  # 9 ele
            # Set is_valid to False
            is_valid = False

            # Iterate until is_valid is True
            while is_valid != True:
                num = random.randrange(1, 10)

                if num not in list[i]:
                    list[i].append(num)
                    is_valid = True

    # Return final list
    return list


# Random list (board) function
def rand_board():
    """
    Generates and returns a new random
    sudoku board
    """

    # Generate blocks
    blocks = block_gen()

    # Set list to a blank board
    list = [["-" for i in range(9)] for j in range(9)]

    # Add three separate blocks to list
    for i in range(3):
        for j in range(9):
            list[i * 3 + j // 3][i * 3 + j % 3] = blocks[i][j]

    # Solve the rest of the board by calling solve_board function
    list = solve_board(list)

    # Return the final list
    return list


# Print the board function
def print_board(board):
    """
    Prints the parameter board as a sudoku board,
    but return nothing
    """

    # Iterate through each row in the board
    for row in board:
        # Make block vertical boarders
        if board.index(row) % 3 == 0 and board.index(row) != 0:
            print("-------------------------------------------------------------")

        # Print each row
        print("-------------------------------------------------------------")
        temp_row = []
        for ele in row:
            if row.index(ele) % 3 == 0 and row.index(ele) != 0:
                temp_row.append(f"|  {ele}")

            else:
                temp_row.append(ele)

        row = f"|  {"  |  ".join(temp_row)}  |"
        print(row)

    # Print last vertical boarder
    print("-------------------------------------------------------------")

    # Print extra space
    print()


# Main function
def main():
    # Set start time
    start_time = time.time()

    # Generate a random list
    list = rand_board()

    # Set str_board
    str_board = [[str(int) for int in row] for row in list]

    # Check the board
    is_solved = check_board(list)

    print(is_solved)

    # Print the board
    print_board(str_board)

    # Set end time
    end_time = time.time()

    # Calculate and print elapsed time
    elapsed_time = end_time - start_time
    print(f'Elapsed time: {elapsed_time:.2f} seconds')


# Call main function
main()