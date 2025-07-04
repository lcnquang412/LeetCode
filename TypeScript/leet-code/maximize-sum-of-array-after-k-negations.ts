{
  function largestSumAfterKNegations(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);
    let index: number = 0,
      length: number = nums.length;
    if (nums[0] < 0) {
      while (nums[index] < 0 && k > 0 && index < length - 1) {
        nums[index] *= -1;
        index++;
        k--;
      }
    }

    let remain = 0;
    if (k % 2 === 1) {
      remain = nums[index];
      if (length > 1 && index < length - 1) {
        remain = Math.min(remain, nums[index + 1]);
      }
      if (index > 0) {
        remain = Math.min(nums[index - 1], remain);
      }
    }

    return nums.reduce(
      (accumulator, currentValue) => accumulator + currentValue,
      -(remain * 2)
    );
  }

  let a: any[] = [
      [4, 2, 3],
      [3, -1, 0, 2],
      [2, -3, -1, 5, -4],
      [5],
      [-8, 3, -5, -3, -5, -2],
      [-4, -2, -3],
    ],
    b: any[] = [1, 3, 2, 2, 6, 4];
  a.forEach((aElement, _index) => {
    console.log(largestSumAfterKNegations(aElement, b[_index]));
  });
}
