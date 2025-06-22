{
  function hasGroupsSizeX(deck: number[]): boolean {
    function gcd(a: number, b: number): number {
      return b > 0 ? gcd(b, a % b) : a;
    }

    // Count
    const hash = new Map<number, number>();
    for (let d of deck) {
      hash.set(d, (hash.get(d) || 0) + 1);
    }

    let result = 0;
    for (let [_, value] of hash) {
      result = gcd(result, value);
    }
    return result > 1;
  }

  let a: any[] = [
    // [1, 2, 3, 4, 4, 3, 2, 1],
    // [1, 1, 1, 2, 2, 2, 3, 3],
    // [1],
    // [1, 1, 2, 2, 2, 2],
    // [1, 1, 1, 1, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3],
  ];
  a.forEach((aElement, _index) => {
    console.log(hasGroupsSizeX(aElement));
  });
}
