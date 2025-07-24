{
  function replaceElements(arr: number[]): number[] {
    const length = arr.length;
    let max = -1;
    for (let i = length - 1; i >= 0; i--) {
      const current = arr[i];
      arr[i] = max;
      if (current > max) {
        max = current;
      }
    }
    return arr;
  }

  let a: any[] = [[17, 18, 5, 4, 6, 1], [400]],
    b: any[] = [];
  const startTime = Date.now();
  a.forEach((aElement, _i) => {
    console.log(JSON.stringify(replaceElements(aElement)));
  });
  const endTime = Date.now();
  console.log(`\nExecution time: ${endTime - startTime} milliseconds`);
}
