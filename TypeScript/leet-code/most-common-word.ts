{
  function mostCommonWord(paragraph: string, banned: string[]): string {
    paragraph = paragraph.toLowerCase();
    let word: string = "",
      map: { [key: string]: number } = {};
    function buildMap(_word: string) {
      if (!word) {
        return;
      }
      if (banned.indexOf(_word) === -1) {
        if (map?.[_word]) {
          map[_word] += 1;
        } else {
          map[_word] = 1;
        }
      } else {
        map[_word] = -1;
      }
    }
    for (let char of paragraph) {
      if ("a" <= char && char <= "z") {
        word += char;
      } else {
        buildMap(word);
        word = "";
      }
    }
    buildMap(word);

    let maxCount: number = -1,
      result: string = "";
    for (let word in map) {
      if (map[word] > maxCount) {
        maxCount = map[word];
        result = word;
      }
    }
    return result;
  }

  //   let a: any = "Bob hit a ball, the hit BALL flew far after it was hit.",
  //     b: string[] = ["hit"];
  let a: any = "Bob. hIt, baLl",
    b: string[] = ["bob", "hit"];
  console.log(mostCommonWord(a, b));
}
