{
  function kidsWithCandies(candies: number[], extraCandies: number): boolean[] {
    const max: number = Math.max(...candies);
    return candies.map((candy) => candy + extraCandies >= max);
  }

  let a: any[] = [
      [2, 3, 5, 1, 3],
      [4, 2, 1, 1, 2],
    ],
    b: any[] = [3, 1];
  const startTime = Date.now();
  a.forEach((aElement, _i) => {
    console.log(JSON.stringify(kidsWithCandies(aElement, b[_i])));
  });
  const endTime = Date.now();
  console.log(`\nExecution time: ${endTime - startTime} milliseconds`);
}
