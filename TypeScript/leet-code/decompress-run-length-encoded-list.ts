{
  function decompressRLElist(nums: number[]): number[] {
    const result: number[] = [];
    for (let i = 0; i < nums.length; i += 2) {
      const length: number = nums[i],
        value: number = nums[i + 1];
      for (let j = 0; j < length; j++) {
        result.push(value);
      }
    }
    return result;
  }

  let a: any[] = [
      [1, 2, 3, 4],
      [1, 1, 2, 3],
    ],
    b: any[] = [];
  const startTime = Date.now();
  a.forEach((aElement, _i) => {
    console.log(JSON.stringify(decompressRLElist(aElement)));
  });
  const endTime = Date.now();
  console.log(`\nExecution time: ${endTime - startTime} milliseconds`);
}
