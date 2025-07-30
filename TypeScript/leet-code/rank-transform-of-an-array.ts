{
  function arrayRankTransform(arr: number[]): number[] {
    const result: number[] = [],
      // map: { [key: number]: number } = {},
      map: Map<number, number> = new Map<number, number>(),
      uniqueArr = [...new Set(arr)];
    uniqueArr.sort((a, b) => a - b);

    for (let i = 0; i < uniqueArr.length; i++) {
      // map[uniqueArr[i]] = i + 1;
      map.set(uniqueArr[i], i + 1);
    }

    for (let number of arr) {
      result.push(map.get(number) || 0);
      // result.push(map[number]);
    }
    return result;
  }

  let a: any[] = [
      [40, 10, 20, 30],
      [100, 100, 100],
      [37, 12, 28, 9, 100, 56, 80, 5, 12],
    ],
    b: any[] = [];
  const startTime = Date.now();
  a.forEach((aElement, _i) => {
    console.log(JSON.stringify(arrayRankTransform(aElement)));
  });
  const endTime = Date.now();
  console.log(`\nExecution time: ${endTime - startTime} milliseconds`);
}
