{
  function uniqueOccurrences(arr: number[]): boolean {
    const map: { [key: number]: number } = {},
      hashMap: Map<number, boolean> = new Map<number, boolean>();
    for (let num of arr) {
      map[num] = (map[num] ?? 0) + 1;
    }

    for (let key of Object.keys(map)) {
      const value: number = map[parseInt(key)];
      if (hashMap.has(value)) {
        return false;
      } else {
        hashMap.set(value, true);
      }
    }
    return true;
  }

  let a: any[] = [
      [1, 2, 2, 1, 1, 3],
      [1, 2],
      [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0],
    ],
    b: any[] = [];
  const startTime = Date.now();
  a.forEach((aElement, _i) => {
    console.log(JSON.stringify(uniqueOccurrences(aElement)));
  });
  const endTime = Date.now();
  console.log(`\nExecution time: ${endTime - startTime} milliseconds`);
}
