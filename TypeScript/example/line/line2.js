{
  function solution(array) {
    var answer = [];
    if (array) {
      answer = array.sort((a, b) => b - a)
    }
    return answer;
  }

  let a = [null];
  a.forEach((aElement, _index) => {
    console.log(solution(aElement));
  });
}
