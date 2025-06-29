{
  function isAlienSorted(words: string[], order: string): boolean {
    const length = words.length,
      map: Map<string, number> = new Map<string, number>();

    for (let i: number = 0; i < order.length; i++) {
      map.set(order[i], i);
    }

    function valid(prev: string, current: string): boolean {
      const prevLen: number = prev.length,
        currentLen: number = current.length,
        biggerLength: number = prevLen > currentLen ? prevLen : currentLen;
      for (let j: number = 0; j < biggerLength; j++) {
        const prevCharIndex: number =
            j > prevLen - 1 ? -1 : map.get(prev[j]) ?? -1,
          currentCharIndex: number =
            j > currentLen - 1 ? -1 : map.get(current[j]) ?? -1;
        if (prevCharIndex < currentCharIndex) {
          return true;
        } else if (prevCharIndex > currentCharIndex) {
          return false;
        }
      }
      return true;
    }

    for (let i: number = 1; i < length; i++) {
      if (!valid(words[i - 1], words[i])) {
        return false;
      }
    }
    return true;
  }

  let a: any[] = [
      ["hello", "leetcode"],
      ["word", "world", "row"],
      ["apple", "app"],
      ["aa", "a"],
    ],
    b: any[] = [
      "hlabcdefgijkmnopqrstuvwxyz",
      "worldabcefghijkmnpqstuvxyz",
      "abcdefghijklmnopqrstuvwxyz",
      "abqwertyuioplkjhgfdszxcvnm",
    ];
  a.forEach((aElement, _index) => {
    console.log(isAlienSorted(aElement, b[_index]));
  });
}
