{
  function findJudge(n: number, trust: number[][]): number {
    if (trust.length === 0) {
      return n === 1 ? 1 : -1;
    }
    const map: { [key: number]: number } = {};
    for (let i = 1; i <= n; i++) {
      map[i] = 0;
    }

    for (let t of trust) {
      map[t[0]] -= 1;
      map[t[1]] += 1;
    }

    for (let key in map) {
      if (map[key] === n - 1) {
        return parseInt(key);
      }
    }

    return -1;
  }

  let a: any[] = [2, 3, 3],
    b: any[] = [
      [[1, 2]],
      [
        [1, 3],
        [2, 3],
      ],
      [
        [1, 3],
        [2, 3],
        [3, 1],
      ],
    ];
  a.forEach((aElement, _index) => {
    console.log(findJudge(aElement, b[_index]));
  });
}
