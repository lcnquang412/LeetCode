{
  function canThreePartsEqualSum(arr: number[]): boolean {
    const sum: number = arr.reduce(
      (accumulate, currentValue) => accumulate + currentValue,
      0
    );

    if (sum % 3 === 0) {
      const sumSub: number = sum / 3;
      let total: number = 0,
        count: number = 0,
        i: number = 0;
      for (i = 0; i < arr.length; i++) {
        total += arr[i];
        if (count === 2 && i < arr.length - 1) {
          continue;
        }
        if (total === sumSub) {
          count++;
          total = 0;
        }
      }

      if (count === 3 && i === arr.length) {
        return true;
      }
    }
    return false;
  }

  let a: any[] = [
      [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1],
      [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1],
      [3, 3, 6, 5, -2, 2, 5, 1, -9, 4],
      [0, 0, 0],
      [10, -10, 10, -10, 10, -10, 10, -10],
    ],
    b: any[] = [];
  a.forEach((aElement, _index) => {
    console.log(canThreePartsEqualSum(aElement));
  });
}
