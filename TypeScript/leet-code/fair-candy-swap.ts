{
  function fairCandySwap(aliceSizes: number[], bobSizes: number[]): number[] {
    const sumA = aliceSizes.reduce(
        (accumulate, value) => accumulate + value,
        0
      ),
      sumB = bobSizes.reduce((accumulate, value) => accumulate + value, 0),
      diff = (sumB - sumA) / 2,
      bobSet = new Set(bobSizes);
    for (let size of aliceSizes) {
      const target = size + diff;
      if (bobSet.has(target)) {
        return [size, target];
      }
    }
    return [];
  }

  let a: any[] = [[1, 1], [1, 2], [2]];
  let b: any[] = [
    [2, 2],
    [2, 3],
    [1, 3],
  ];
  a.forEach((_a, _index) => {
    console.log(fairCandySwap(_a, b[_index]));
  });
}
