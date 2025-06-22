{
  function smallestRangeI(nums: number[], k: number): number {
    const min = Math.min(...nums),
      max = Math.max(...nums);
    return min + k >= max - k ? 0 : max - min - 2 * k;
  }

  let a: any[] = [[1], [0, 10], [1, 3, 6]],
    b: any[] = [0, 2, 3];
  a.forEach((aElement, _index) => {
    console.log(smallestRangeI(aElement, b[_index]));
  });
}
