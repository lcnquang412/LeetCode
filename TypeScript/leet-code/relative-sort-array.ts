{
  function relativeSortArray(arr1: number[], arr2: number[]): number[] {
    const remain: number[] = [],
      map: { [key: number]: number } = {};
    let result: number[] = [];

    for (let num of arr2) {
      map[num] = 0;
    }

    for (let num of arr1) {
      if (map[num] !== undefined) {
        map[num]++;
      } else {
        remain.push(num);
      }
    }

    remain.sort((a, b) => a - b);

    for (let num of arr2) {
      for (let i = 0; i < map[num]; i++) {
        result.push(num);
      }
    }

    return result.concat(remain);
  }

  let a: any[] = [
      [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19],
      [28, 6, 22, 8, 44, 17],
      [5],
    ],
    b: any[] = [[2, 1, 4, 3, 9, 6], [22, 28, 8, 6], [5]];
  a.forEach((aElement, _index) => {
    console.log(relativeSortArray(aElement, b[_index]));
  });
}
