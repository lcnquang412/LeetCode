{
  function heightChecker(heights: number[]): number {
    const expected = [...heights];
    let count = 0;
    expected.sort((a, b) => a - b);
    for (let i = 0; i < heights.length; i++) {
      if (heights[i] !== expected[i]) {
        count++;
      }
    }

    return count;
  }

  let a: any[] = [
      [1, 1, 4, 2, 1, 3],
      [5, 1, 2, 3, 4],
      [1, 2, 3, 4, 5],
    ],
    b: any[] = [];
  a.forEach((aElement, _index) => {
    console.log(heightChecker(aElement));
  });
}
