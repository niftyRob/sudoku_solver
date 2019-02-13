from sudoku import SudokuGrid, SudokuSolver


def main():
    # # Easy
    # row1 = '5,-,-,-,-,-,-,-,1,'
    # row2 = '-,7,-,-,8,-,9,-,-,'
    # row3 = '8,-,9,-,-,-,-,-,6,'
    # row4 = '6,8,-,2,-,5,7,4,-,'
    # row5 = '7,-,-,6,-,8,-,-,3,'
    # row6 = '-,1,5,3,-,9,-,6,8,'
    # row7 = '3,-,-,-,-,-,6,-,7,'
    # row8 = '-,-,6,-,3,-,-,1,-,'
    # row9 = '1,-,-,-,-,-,-,-,4'
    # Blank
    # row1 = '-,-,-,-,-,-,-,-,-,'
    # row2 = '-,-,-,-,-,-,-,-,-,'
    # row3 = '-,-,-,-,-,-,-,-,-,'
    # row4 = '-,-,-,-,-,-,-,-,-,'
    # row5 = '-,-,-,-,-,-,-,-,-,'
    # row6 = '-,-,-,-,-,-,-,-,-,'
    # row7 = '-,-,-,-,-,-,-,-,-,'
    # row8 = '-,-,-,-,-,-,-,-,-,'
    # row9 = '-,-,-,-,-,-,-,-,-'
    row1 = '8,-,-,-,-,-,-,-,-,'
    row2 = '-,-,3,6,-,-,-,-,-,'
    row3 = '-,7,-,-,9,-,2,-,-,'
    row4 = '-,5,-,-,-,7,-,-,-,'
    row5 = '-,-,-,-,4,5,7,-,-,'
    row6 = '-,-,-,1,-,-,-,3,-,'
    row7 = '-,-,1,-,-,-,-,6,8,'
    row8 = '-,-,8,5,-,-,-,1,-,'
    row9 = '-,9,-,-,-,-,4,-,-'
    puzzle = row1 + row2 + row3 + row4 + row5 + row6 + row7 + row8 + row9
    sg = SudokuGrid(puzzle.split(','))
    solver = SudokuSolver(sg)
    solver.solve_puzzle()
    print(solver.grid)
    print(solver.puzzle_solved())
    print(solver.count, "Iterations")


if __name__ == '__main__':
    main()
