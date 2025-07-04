{
  function allCellsDistOrder(
    rows: number,
    cols: number,
    rCenter: number,
    cCenter: number
  ): number[][] {
    const queue: number[][] = [[rCenter, cCenter]],
      result: number[][] = [],
      flag: boolean[][] = Array.from({ length: rows }, () =>
        Array.from({ length: cols }, () => true)
      );
    let index = 0;
    const STEPS: number[][] = [
      [0, 1],
      [0, -1],
      [1, 0],
      [-1, 0],
    ];
    flag[rCenter][cCenter] = false;

    while (index < queue.length) {
      const item: number[] = queue[index++] || [];
      result.push(item);
      STEPS.forEach((step) => {
        const row = item[0] + step[0],
          col = item[1] + step[1];
        if (flag[row]?.[col]) {
          queue.push([row, col]);
          flag[row][col] = false;
        }
      });
    }
    return result;
  }

  let a: any[] = [
      // [1, 2, 0, 0],
      // [2, 2, 0, 1],
      // [2, 3, 1, 2],
      [3, 3, 0, 2],
    ],
    b: any[] = [];
  a.forEach((aElement, _index) => {
    console.log(
      JSON.stringify(
        allCellsDistOrder(aElement[0], aElement[1], aElement[2], aElement[3])
      )
    );
  });
}
