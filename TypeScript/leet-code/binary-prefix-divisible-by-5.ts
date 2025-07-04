{
  function prefixesDivBy5(nums: number[]): boolean[] {
    const result: boolean[] = [];

    let total = 0;
    for (let num of nums) {
      total = (total * 2 + 1 * num) % 5;
      result.push(total === 0);
    }
    return result;
  }

  let a: any[] = [
      [0, 1, 1],
      [1, 1, 1],
      [
        1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1,
        0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1,
      ],
      [
        1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1,
        0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1,
      ],
    ],
    b: any[] = [];
  a.forEach((aElement, _index) => {
    console.log(prefixesDivBy5(aElement));
  });
}
