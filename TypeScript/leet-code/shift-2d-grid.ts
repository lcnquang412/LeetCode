{
  function shiftGrid(grid: number[][], k: number): number[][] {
    const gridTmp: number[] = grid.flat(),
      row = grid.length,
      col = grid[0].length,
      result: number[][] = [];
    let kLoop: number = k % (row * col);
    while (kLoop--) {
      gridTmp.unshift(gridTmp.pop() ?? -2000);
    }
    while (gridTmp.length) {
      result.push(gridTmp.splice(0, col));
    }
    return result;
  }

  // function shiftGrid(grid: number[][], k: number): number[][] {
  //   const row: number = grid.length,
  //     col: number = grid[0].length;
  //   let gridTmp: number[] = Array.from({ length: col }, () => 0);

  //   for (let i = 0; i < k % (row * col); i++) {
  //     for (let r = 0; r < row; r++) {
  //       gridTmp[r] = grid[r][0];
  //       grid[r][0] = grid[r][col - 1];
  //     }

  //     for (let c = 1; c < col; c++) {
  //       for (let r = 0; r < row; r++) {
  //         [grid[r][c], gridTmp[r]] = [gridTmp[r], grid[r][c]];
  //       }
  //     }

  //     let tmp = grid[0][0];
  //     grid[0][0] = grid[row - 1][0];
  //     for (let r = 1; r < row; r++) {
  //       [grid[r][0], tmp] = [tmp, grid[r][0]];
  //     }
  //   }

  //   return grid;
  // }

  let a: any[] = [
      [[1], [2], [3], [4], [7], [6], [5]],
      // [
      //   [1, 2, 3],
      //   [4, 5, 6],
      //   [7, 8, 9],
      // ],
      // [
      //   [3, 8, 1, 9],
      //   [19, 7, 2, 5],
      //   [4, 6, 11, 10],
      //   [12, 0, 21, 13],
      // ],
      // [[1, 2, 3, 4]],
      // [[1], [2], [3], [4]],
      // [1],
    ],
    b: any[] = [23, 1, 4, 2, 2, 100];
  const startTime = Date.now();
  a.forEach((aElement, _i) => {
    console.log(JSON.stringify(shiftGrid(aElement, b[_i])));
  });
  const endTime = Date.now();
  console.log(`\nExecution time: ${endTime - startTime} milliseconds`);
}
