{
  function transpose(matrix: number[][]): number[][] {
    // const row = matrix.length,
    //   col = matrix[0].length,
    //   result: number[][] = Array.from({ length: col }, () =>
    //     Array.from({ length: row }, () => 0)
    //   );

    // for (let i = 0; i < col; i++) {
    //   for (let j = 0; j < row; j++) {
    //     result[i][j] = matrix[j][i];
    //   }
    // }

    const row = matrix.length,
      col = matrix[0].length;

    for (let i = 0; i < row; i++) {
      for (let j = 0; j < col; j++) {
        const tmp: number = matrix[i][j];
        matrix[i][j] = matrix[i][j];
        matrix[i][j] = tmp;
      }
    }

    return matrix;
  }

  let a: any[] = [
    [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
    ],
    [
      [1, 2, 3],
      [4, 5, 6],
    ],
  ];
  for (let aElement of a) {
    console.log(transpose(aElement));
  }
}
