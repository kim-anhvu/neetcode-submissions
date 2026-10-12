class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not(self.isRowColValid(board[i])):
                return False
            elif not(self.isRowColValid(self.getCol(i, board))):
                return False
            elif not(self.isRowColValid(self.getSquare(i, board))):
                return False
        return True
    
    def isRowColValid(self, rowCol: List[str]):
        filteredList = [x for x in rowCol if x != "."]
        if (len(set(filteredList)) != len(filteredList)):
            return False
        return True

    def getCol(self, colId: int, board: List[List[str]]):
        col = []
        for rowIndex in range(0, 9):
            col.append(board[rowIndex][colId])
        return col
    
    def getSquare(self, squareId: int, board: List[List[str]]):
        squareNums = []
        squareCoords = {0: [0,0], 1: [0,3], 2: [0,6], 3: [3,0], 4: [3,3], 5: [3,6], 6: [6,0], 7: [6,3], 8: [6,6] }
        beginningCoords = squareCoords.get(squareId)  

        for i in range(beginningCoords[0], beginningCoords[0]+3):
            for j in range(beginningCoords[1], beginningCoords[1]+3):
                squareNums.append(board[i][j])
        return squareNums
