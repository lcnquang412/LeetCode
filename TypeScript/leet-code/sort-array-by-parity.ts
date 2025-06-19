{
  function sortArrayByParity(nums: number[]): number[] {
    const length: number = nums.length;
    let oddIndex: number = length - 1,
      evenIndex: number = 0;
    while (evenIndex <= oddIndex) {
      if (nums[evenIndex] % 2 === 0) {
        evenIndex++;
      } else {
        [nums[evenIndex], nums[oddIndex]] = [nums[oddIndex], nums[evenIndex]];
        oddIndex--;
      }
    }
    return nums;
  }

  let a: any[] = [[3, 1, 2, 4], [0]];
  a.forEach((aElement, _index) => {
    console.log(sortArrayByParity(aElement));
  });
}
