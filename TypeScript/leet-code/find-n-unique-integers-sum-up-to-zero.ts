{
  function sumZero(n: number): number[] {
    const result: number[] = [];
    for (let i = 1; i <= n / 2; i++) {
      result.push(i, -i);
    }
    if (n % 2 !== 0) {
      result.push(0);
    }
    return result;
  }

  let a: any[] = [5, 3, 1],
    b: any[] = [];
  const startTime = Date.now();
  a.forEach((aElement, _i) => {
    console.log(JSON.stringify(sumZero(aElement)));
  });
  const endTime = Date.now();
  console.log(`\nExecution time: ${endTime - startTime} milliseconds`);
}
