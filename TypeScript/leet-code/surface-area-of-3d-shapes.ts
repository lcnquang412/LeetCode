{
  function surfaceArea(grid: number[][]): number {
    const row: number = grid.length,
      col: number = grid.length;
    let tsa: number = 0;
    for (let i = 0; i < row; i++) {
      for (let j = 0; j < col; j++) {
        if (grid[i][j] !== 0) {
          tsa += 2;
        }
        if (i === 0) {
          tsa += grid[i][j];
        }
        if (i === row - 1) {
          tsa += grid[i][j];
        }
        if (j === 0) {
          tsa += grid[i][j];
        }
        if (j === col - 1) {
          tsa += grid[i][j];
        }

        if (i > 0) {
          tsa += Math.abs(grid[i][j] - grid[i - 1][j]);
        }
        if (j > 0) {
          tsa += Math.abs(grid[i][j] - grid[i][j - 1]);
        }
      }
    }
    return tsa;
  }

  let a: any[] = [
    [
      [1, 2],
      [3, 4],
    ],
    [[2]],
    [
      [1, 0],
      [0, 2],
    ],
    [
      [1, 1, 1],
      [1, 0, 1],
      [1, 1, 1],
    ],
    [
      [2, 2, 2],
      [2, 1, 2],
      [2, 2, 2],
    ],
  ];
  for (let aElement of a) {
    console.log(surfaceArea(aElement));
  }
}
