{
  function isMonotonic(nums: number[]): boolean {
    const NONE = "none",
      INC = "increase",
      DEC = "decrease";
    let monotone = NONE;
    for (let i = 1; i < nums.length; i++) {
      const num = nums[i],
        numPrev = nums[i - 1];
      if (num === numPrev) {
        continue;
      } else {
        switch (monotone) {
          case NONE:
            monotone = numPrev < num ? INC : DEC;
            break;
          case INC:
            if (numPrev > num) {
              return false;
            }
            break;
          case DEC:
            if (numPrev < num) {
              return false;
            }
            break;
          default:
            break;
        }
      }
    }
    return true;
  }

  let a: any[] = [
    [1, 2, 2, 3],
    [6, 5, 4, 4],
    [1, 3, 2],
  ];
  a.forEach((aElement, _index) => {
    console.log(isMonotonic(aElement));
  });
}
