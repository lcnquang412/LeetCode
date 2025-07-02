{
  function findJudge(n: number, trust: number[][]): number {
    if (trust.length === 0) {
      return n === 1 ? 1 : -1;
    }
    const map: Map<number, number> = new Map<number, number>();
    for (let t of trust) {
      map.set(t[0], (map.get(t[0]) || 0) - 1);
      map.set(t[1], (map.get(t[1]) || 0) + 1);
    }

    for (const [key, value] of map) {
      if (value === n - 1) {
        return key;
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
