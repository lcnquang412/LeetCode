{
  function projectionArea(grid: number[][]): number {
    const row: number = grid.length,
      col: number = grid.length;
    let areaRight: number = 0,
      areaBelow: number = 0,
      areaBehind: number[] = Array.from({ length: col }, () => -1);
    for (let i = 0; i < row; i++) {
      let maxRow = grid[i][0];
      for (let j = 0; j < col; j++) {
        if (grid[i][j] !== 0) {
          areaBelow++;
        }
        if (grid[i][j] > maxRow) {
          maxRow = grid[i][j];
        }
        if (grid[i][j] > areaBehind[j]) {
          areaBehind[j] = grid[i][j];
        }
      }
      areaRight += maxRow;
    }

    return (
      areaRight +
      areaBelow +
      areaBehind.reduce(
        (accumulator, currentValue) => accumulator + currentValue,
        0
      )
    );
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
  ];
  for (let aElement of a) {
    console.log(projectionArea(aElement));
  }
}
