{
  function numRookCaptures(board: string[][]): number {
    let rowRook: number = -1,
      colRook: number = -1;
    const BOARD_LENGTH: number = 8;
    for (let i = 0; i < BOARD_LENGTH; i++) {
      for (let j = 0; j < BOARD_LENGTH; j++) {
        if (board[i][j] === "R") {
          rowRook = i;
          colRook = j;
          break;
        }
      }
    }

    let count = 0;
    for (let i = rowRook + 1; i < BOARD_LENGTH; i++) {
      if (board[i][colRook] === "B") {
        break;
      } else if (board[i][colRook] === "p") {
        count++;
        break;
      }
    }

    for (let i = rowRook - 1; i >= 0; i--) {
      if (board[i][colRook] === "B") {
        break;
      } else if (board[i][colRook] === "p") {
        count++;
        break;
      }
    }

    for (let j = colRook + 1; j < BOARD_LENGTH; j++) {
      if (board[rowRook][j] === "B") {
        break;
      } else if (board[rowRook][j] === "p") {
        count++;
        break;
      }
    }

    for (let j = colRook - 1; j >= 0; j--) {
      if (board[rowRook][j] === "B") {
        break;
      } else if (board[rowRook][j] === "p") {
        count++;
        break;
      }
    }

    return count;
  }

  let a: any[] = [
    [
      [".", ".", ".", ".", ".", ".", ".", "."],
      [".", ".", ".", "p", ".", ".", ".", "."],
      [".", ".", ".", "R", ".", ".", ".", "p"],
      [".", ".", ".", ".", ".", ".", ".", "."],
      [".", ".", ".", ".", ".", ".", ".", "."],
      [".", ".", ".", "p", ".", ".", ".", "."],
      [".", ".", ".", ".", ".", ".", ".", "."],
      [".", ".", ".", ".", ".", ".", ".", "."],
    ],
    [
      [".", ".", ".", ".", ".", ".", "."],
      [".", "p", "p", "p", "p", "p", ".", "."],
      [".", "p", "p", "B", "p", "p", ".", "."],
      [".", "p", "B", "R", "B", "p", ".", "."],
      [".", "p", "p", "B", "p", "p", ".", "."],
      [".", "p", "p", "p", "p", "p", ".", "."],
      [".", ".", ".", ".", ".", ".", ".", "."],
      [".", ".", ".", ".", ".", ".", ".", "."],
    ],
    [
      [".", ".", ".", ".", ".", ".", ".", "."],
      [".", ".", ".", "p", ".", ".", ".", "."],
      [".", ".", ".", "p", ".", ".", ".", "."],
      ["p", "p", ".", "R", ".", "p", "B", "."],
      [".", ".", ".", ".", ".", ".", ".", "."],
      [".", ".", ".", "B", ".", ".", ".", "."],
      [".", ".", ".", "p", ".", ".", ".", "."],
      [".", ".", ".", ".", ".", ".", ".", "."],
    ],
  ];
  a.forEach((aElement, _index) => {
    console.log(numRookCaptures(aElement));
  });
}
