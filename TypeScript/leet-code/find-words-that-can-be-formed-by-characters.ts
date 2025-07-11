{
  function countCharacters(words: string[], chars: string): number {
    const hash: number[] = Array.from({ length: 26 }, () => 0),
      distance: number = "a".charCodeAt(0);
    for (let char of chars) {
      hash[char.charCodeAt(0) - distance]++;
    }

    function isGoodWord(word: string): number {
      const hashTmp: number[] = Array.from({ length: 26 }, () => 0);
      for (let char of word) {
        const index = char.charCodeAt(0) - distance;
        if (hash[index] === 0) {
          return 0;
        } else {
          hashTmp[index]++;
          if (hashTmp[index] > hash[index]) {
            return 0;
          }
        }
      }

      return word.length;
    }

    let result: number = 0;
    for (let word of words) {
      result += isGoodWord(word);
    }
    return result;
  }

  let a: any[] = [
      ["cat", "bt", "hat", "tree"],
      ["hello", "world", "leetcode"],
    ],
    b: any[] = ["atach", "welldonehoneyr"];
  const startTime = Date.now();
  a.forEach((aElement, _index) => {
    console.log(countCharacters(aElement, b[_index]));
  });
  const endTime = Date.now();
  console.log(`\nExecution time: ${endTime - startTime} milliseconds`);
}
