{
  function lastStoneWeight(stones: number[]): number {
    while (stones.length > 1) {
      let max1 = Math.max(...stones),
        maxIndex = stones.indexOf(max1);
      stones.splice(maxIndex, 1);

      let max2 = Math.max(...stones);
      maxIndex = stones.indexOf(max2);
      stones.splice(maxIndex, 1);

      if (max1 === max2) {
        continue;
      } else {
        stones.push(max1 - max2);
      }
    }

    if (stones.length === 1) {
      return stones[0];
    }

    return 0;
  }

  let a: any[] = [[2, 7, 4, 1, 8, 1], [1], [1, 2, 3], [1, 3]],
    b: any[] = [];
  a.forEach((aElement, _index) => {
    console.log(lastStoneWeight(aElement));
  });
}
