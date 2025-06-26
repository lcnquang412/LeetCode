{
  function minDeletionSize(strs: string[]): number {
    let count: number = 0;
    const length: number = strs.length,
      lengthWord: number = strs[0].length;
    if (length === 1) {
      return 0;
    }
    for (let i: number = 0; i < lengthWord; i++) {
      for (let j: number = 1; j < length; j++) {
        if (strs[j][i] < strs[j - 1][i]) {
          count++;
          break;
        }
      }
    }
    return count;
  }

  let a: any[] = [
    ["cba", "daf", "ghi"],
    ["a", "b"],
    ["zyx", "wvu", "tsr"],
  ];
  a.forEach((aElement, _index) => {
    console.log(minDeletionSize(aElement));
  });
}
