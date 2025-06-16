{
  function shortestToChar(s: string, c: string): number[] {
    const cIndices: number[] = [],
      len = s.length,
      result: number[] = new Array(len).fill(10001);
    for (let i = 0; i < len; i++) {
      if (s[i] === c) {
        cIndices.push(i);
      }
    }

    cIndices.forEach((i) => {
      let distance: number = 1,
        left: number = i - 1,
        right: number = i + 1;
      result[i] = 0;
      while (left >= 0 && s[left] != c && result[left] > distance) {
        result[left] = distance;
        left--;
        distance++;
      }

      distance = 1;
      while (right < len && s[right] != c && result[right] > distance) {
        result[right] = distance;
        right++;
        distance++;
      }
    });
    return result;
  }

  //   let a: any = "loveleetcode",
  //     b: string = "e";
  let a: any = "aaab",
    b: string = "b";
  console.log(shortestToChar(a, b));
}
