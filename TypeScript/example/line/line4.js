{
  function solution(arr1, arr2) {
    // Provide your solution here
    if (!arr1 && !arr2) {
      return true
    }
    if (!arr1 || !arr2) {
      return false
    }
    if (arr1.length !== arr2.length) {
      return false
    }

    for (let i in arr1) {
      if (arr1[i] !== arr2[i]) {
        return false
      }
    }

    return true
  }

  let a = [[null, [], []]];
  a.forEach((aElement, _index) => {
    console.log(solution(aElement));
  });
}
