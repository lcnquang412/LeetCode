{
  function solution(AA: number, AB: number, BB: number): string {
    let resultFinal: string = "";
    // Implement your solution here
    function traverse(
      _AA: number,
      _AB: number,
      _BB: number,
      previous: string,
      result: string
    ) {
      if (resultFinal.length < result.length) {
        resultFinal = result;
      }
      if (resultFinal.length === (AA + AB + BB) * 2) {
        return;
      }
      switch (previous) {
        case "AA":
          if (_BB > 0) {
            traverse(_AA, _AB, _BB - 1, "BB", result + "BB");
          }
          break;
        case "AB":
          if (_AA > 0) {
            traverse(_AA - 1, _AB, _BB, "AA", result + "AA");
          }
          if (_AB > 0) {
            traverse(_AA, _AB - 1, _BB, "AB", result + "AB");
          }
          break;
        case "BB":
          if (_AB > 0) {
            traverse(_AA, _AB - 1, _BB, "AB", result + "AB");
          }
          if (_AA > 0) {
            traverse(_AA - 1, _AB, _BB, "AA", result + "AA");
          }
          break;
        default:
          if (_AA > 0) {
            traverse(_AA - 1, _AB, _BB, "AA", result + "AA");
          }
          if (_AB > 0) {
            traverse(_AA, _AB - 1, _BB, "AB", result + "AB");
          }
          if (_BB > 0) {
            traverse(_AA, _AB, _BB - 1, "BB", result + "BB");
          }
          break;
      }
    }
    traverse(AA, AB, BB, "", "");
    return resultFinal;
  }
  let a: any[] = [5, 1, 0, 0, 10];
  let b: any[] = [0, 2, 2, 0, 10];
  let c: any[] = [2, 1, 0, 10, 10];
  a.forEach((aElement, _index) => {
    console.log(solution(aElement, b[_index], c[_index]));
  });
}
