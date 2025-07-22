{
  function findSpecialInteger(arr: number[]): number {
    let candidate: number = -1,
      count: number = 0,
      target: number = arr.length / 4;
    for (let number of arr) {
      if (number === candidate) {
        count++;
      } else {
        candidate = number;
        count = 1;
      }

      if (count > target) {
        return candidate;
      }
    }
    return -1;
  }

  let a: any[] = [
      [1, 2, 2, 6, 6, 6, 6, 7, 10],
      [1, 1],
    ],
    b: any[] = [];
  const startTime = Date.now();
  a.forEach((aElement, _i) => {
    console.log(JSON.stringify(findSpecialInteger(aElement)));
  });
  const endTime = Date.now();
  console.log(`\nExecution time: ${endTime - startTime} milliseconds`);
}
