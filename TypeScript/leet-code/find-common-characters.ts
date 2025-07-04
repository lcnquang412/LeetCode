{
  function commonChars(words: string[]): string[] {
    let freqMin = new Array(26).fill(Infinity),
      distance: number = "a".charCodeAt(0);

    for (let word of words) {
      let freqTmp = new Array(26).fill(0);
      for (let char of word) {
        freqTmp[char.charCodeAt(0) - distance]++;
      }
      for (let i = 0; i < 26; i++) {
        freqMin[i] = Math.min(freqMin[i], freqTmp[i]);
      }
    }

    let result: string[] = [];
    for (let i = 0; i < 26; i++) {
      if (freqMin[i] != 0) {
        while (freqMin[i]-- > 0) {
          result.push(String.fromCharCode(i + distance));
        }
      }
    }

    return result;
  }

  let a: any[] = [
    ["bella", "label", "roller"],
    ["cool", "lock", "cook"],
  ];
  a.forEach((aElement, _index) => {
    console.log(commonChars(aElement));
  });
}
