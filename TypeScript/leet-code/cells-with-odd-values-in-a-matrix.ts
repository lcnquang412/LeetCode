{
  function oddCells(m: number, n: number, indices: number[][]): number {
    const row: number[] = Array.from({ length: m }, () => 0),
      col: number[] = Array.from({ length: n }, () => 0);

    for (let index of indices) {
      row[index[0]]++;
      col[index[1]]++;
    }

    let count: number = 0;
    for (let r of row) {
      for (let c of col) {
        if ((r + c) % 2 === 1) {
          count++;
        }
      }
    }
    return count;
  }

  let a: any[] = [2, 2],
    b: any[] = [3, 2],
    c: any[] = [
      [
        [0, 1],
        [1, 1],
      ],
      [
        [1, 1],
        [0, 0],
      ],
    ];
  const startTime = Date.now();
  a.forEach((aElement, _i) => {
    console.log(JSON.stringify(oddCells(aElement, b[_i], c[_i])));
  });
  const endTime = Date.now();
  console.log(`\nExecution time: ${endTime - startTime} milliseconds`);
}
