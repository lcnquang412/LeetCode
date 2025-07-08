{
  function duplicateZeros(arr: number[]): void {
    const stack: number[] = [];
    let index = 0;
    for (let i = 0; i < arr.length; i++) {
      const num: number = arr[i];
      if (index < stack.length) {
        stack.push(num);
        arr[i] = stack[index];
        index++;
      }
      if (num === 0) {
        stack.push(0);
      }
    }
  }

  let a: any[] = [
      [1, 0, 2, 3, 0, 4, 5, 0],
      // [1, 2, 3],
    ],
    b: any[] = [];
  a.forEach((aElement, _index) => {
    console.log(duplicateZeros(aElement));
  });
}
