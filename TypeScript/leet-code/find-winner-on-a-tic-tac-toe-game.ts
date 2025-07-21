{
  function tictactoe(moves: number[][]): string {
    const INDEX_H_V = 3,
      INDEX_DIAGONAL = 2,
      horizontal: number[] = Array.from({ length: INDEX_H_V * 2 }, () => 0),
      vertical: number[] = Array.from({ length: INDEX_H_V * 2 }, () => 0),
      diagonal: number[] = Array.from({ length: INDEX_DIAGONAL * 2 }, () => 0);

    for (let i = 0; i < moves.length; i++) {
      const move: number[] = moves[i],
        player: number = i % 2;
      // Horizontal
      horizontal[player * INDEX_H_V + move[0]]++;
      // Vertical
      vertical[player * INDEX_H_V + move[1]]++;

      // Diagonal
      if (move[0] === move[1]) {
        diagonal[player * INDEX_DIAGONAL]++;
        if (move[0] === 1) {
          diagonal[player * INDEX_DIAGONAL + 1]++;
        }
      }

      if (
        (move[0] === 0 && move[1] === 2) ||
        (move[0] === 2 && move[1] === 0)
      ) {
        diagonal[player * INDEX_DIAGONAL + 1]++;
      }
    }

    // Check: Horizontal, Vertical
    for (let i = 0; i < INDEX_H_V * 2; i++) {
      if (horizontal[i] === 3 || vertical[i] === 3) {
        return i < INDEX_H_V ? "A" : "B";
      }
    }

    // Check: Diagonal
    for (let i = 0; i < INDEX_DIAGONAL * 2; i++) {
      if (diagonal[i] === 3) {
        return i < INDEX_DIAGONAL ? "A" : "B";
      }
    }

    if (moves.length < 9) {
      return "Pending";
    }

    return "Draw";
  }

  let a: any[] = [
      [
        [0, 0],
        [2, 0],
        [1, 1],
        [2, 1],
        [2, 2],
      ],
      [
        [0, 0],
        [1, 1],
        [0, 1],
        [0, 2],
        [1, 0],
        [2, 0],
      ],
      [
        [0, 0],
        [1, 1],
        [2, 0],
        [1, 0],
        [1, 2],
        [2, 1],
        [0, 1],
        [0, 2],
        [2, 2],
      ],
      [
        [0, 0],
        [1, 1],
      ],
    ],
    b: any[] = [];
  const startTime = Date.now();
  a.forEach((aElement, _i) => {
    console.log(JSON.stringify(tictactoe(aElement)));
  });
  const endTime = Date.now();
  console.log(`\nExecution time: ${endTime - startTime} milliseconds`);
}
