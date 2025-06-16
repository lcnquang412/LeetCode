{
  function numberOfLines(widths: number[], s: string): number[] {
    let total: number = 0,
      lineCount: number = 0;

    for (let char of s) {
      const width: number = widths[char.charCodeAt(0) - 97];

      if (total + width > 100) {
        total = width;
        lineCount += 1;
      } else {
        total = total + width;
      }
    }
    return [lineCount + 1, total];
  }

  // let a: any = [
  //   10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
  //   10, 10, 10, 10, 10, 10, 10,
  // ];
  // let b: any = "abcdefghijklmnopqrstuvwxyz";
  let a: any = [
    4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
    10, 10, 10, 10, 10, 10, 10,
  ];
  let b: any = "bbbcccdddaac";
  console.log(numberOfLines(a, b));
}
