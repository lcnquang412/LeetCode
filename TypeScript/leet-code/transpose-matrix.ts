{
  function transpose(matrix: number[][]): number[][] {
    const row = matrix.length,
      col = matrix[0].length;
    if (row !== col) {
      let result: number[][] = Array.from(
        { length: col },
        () => new Array(row)
      );

      for (let i = 0; i < col; i++) {
        for (let j = 0; j < row; j++) {
          result[i][j] = matrix[j][i];
        }
      }
      return result;
    } else {
      for (let i = 0; i < row; i++) {
        for (let j = i + 1; j < row; j++) {
          [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
        }
      }
      return matrix;
    }
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
