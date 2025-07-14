{
  function minimumAbsDifference(arr: number[]): number[][] {
    arr.sort((a, b) => a - b);
    const map: { [key: string]: number[][] } = {};
    let min: number = Infinity;
    for (let i = 1; i < arr.length; i++) {
      const diff: number = Math.abs(arr[i] - arr[i - 1]);
      if (diff <= min) {
        min = diff;
        const result: number[] = [arr[i - 1], arr[i]];
        if (map[min]) {
          map[min].push(result);
        } else {
          map[min] = [result];
        }
      }
    }
    return map[min];
  }

  let a: any[] = [
      [4, 2, 1, 3],
      [1, 3, 6, 10, 15],
      [3, 8, -10, 23, 19, -4, -14, 27],
    ],
    b: any[] = [];
  const startTime = Date.now();
  a.forEach((aElement, _i) => {
    console.log(JSON.stringify(minimumAbsDifference(aElement)));
  });
  const endTime = Date.now();
  console.log(`\nExecution time: ${endTime - startTime} milliseconds`);
}
