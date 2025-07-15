{
  function minCostToMoveChips(position: number[]): number {
    let odd: number = 0,
      even: number = 0;
    for (let pos of position) {
      if (pos % 2 === 0) {
        even++;
      } else {
        odd++;
      }
    }
    return Math.min(even, odd);
  }

  let a: any[] = [
      [1, 2, 3],
      [2, 2, 2, 3, 3],
      [1, 1000000000],
    ],
    b: any[] = [];
  const startTime = Date.now();
  a.forEach((aElement, _i) => {
    console.log(JSON.stringify(minCostToMoveChips(aElement)));
  });
  const endTime = Date.now();
  console.log(`\nExecution time: ${endTime - startTime} milliseconds`);
}
