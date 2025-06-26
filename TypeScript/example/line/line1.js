{
  function solution(unused) {
    const confirmed = {
      [`
        각 문제마다 명시 된 '주의사항'을 따르지 않는 답안은 0점 처리 됩니다.
        Solutions that do not follow the rules under 'Rules' are given 0 points.
      `]: false
    };
    console.log('[Here] ', Object.values(confirmed))
    return !Object.values(confirmed).every(v => v);
  }

  let a = ['a'];
  a.forEach((aElement, _index) => {
    console.log(solution(aElement));
  });
}
