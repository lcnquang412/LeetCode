{
  function commonChars(words: string[]): string[] {
    let result: { [key: string]: number } = {},
      resultTmp: { [key: string]: number } = {},
      count = 0,
      countTmp = 0;
    for (let char of words[0]) {
      if (result[char]) {
        result[char] += 1;
        // count++;
      } else {
        result[char] = 1;
        // count++;
      }
    }

    for (let i = 1; i < words.length; i++) {
      const word: string = words[i];
      resultTmp = {};
      countTmp = 0;
      for (let char of word) {
        if (result[char]) {
          if (resultTmp[char]) {
            if (resultTmp[char] < result[char]) {
              resultTmp[char] += 1;
              // countTmp++;
            }
          } else {
            resultTmp[char] = 1;
            // countTmp++;
          }
        }
        // if (countTmp === count) {
        //   break;
        // }
      }
      result = resultTmp;
      // count = countTmp;
    }

    const resultFinal: string[] = [];
    for (let key in result) {
      const value: number = result[key];
      for (let i = 0; i < value; i++) {
        resultFinal.push(key);
      }
    }
    return resultFinal;
  }

  let a: any[] = [
    ["bella", "label", "roller"],
    ["cool", "lock", "cook"],
  ];
  a.forEach((aElement, _index) => {
    console.log(commonChars(aElement));
  });
}
