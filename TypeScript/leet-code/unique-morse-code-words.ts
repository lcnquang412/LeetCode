{
  function uniqueMorseRepresentations(words: string[]): number {
    const MAP: { [key: string]: string } = {
        a: ".-",
        b: "-...",
        c: "-.-.",
        d: "-..",
        e: ".",
        f: "..-.",
        g: "--.",
        h: "....",
        i: "..",
        j: ".---",
        k: "-.-",
        l: ".-..",
        m: "--",
        n: "-.",
        o: "---",
        p: ".--.",
        q: "--.-",
        r: ".-.",
        s: "...",
        t: "-",
        u: "..-",
        v: "...-",
        w: ".--",
        x: "-..-",
        y: "-.--",
        z: "--..",
      },
      HASH_MAP = new Map<string, boolean>();
    for (let word of words) {
      let morse: string = "";
      for (let char of word) {
        morse += MAP[char];
      }
      HASH_MAP.set(morse, true);
    }
    return HASH_MAP.size;
  }

  let a: any = ["a"];
  // let a: any = ["gin", "zen", "gig", "msg"];
  console.log(uniqueMorseRepresentations(a));
}
