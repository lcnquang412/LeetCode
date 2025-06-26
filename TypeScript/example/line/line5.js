// {
//   function solution(...arrays) {
//     // Provide your solution here
// }

//   let a = [];
//   a.forEach((aElement, _index) => {
//     console.log(solution(aElement));
//   });
// }


function solution(...arrays) {
  // Provide your solution here
  const set = new Set();
  let result = true
  function check(_arrays) {
    console.log('[Here]', set)
    if (!result) {
      return
    }
    for (let element of _arrays) {
      if (Array.isArray(element)) {
        check(element)
      } else {
        if (set.has(element)) {
          result = false
          return
        } else {
          set.add(element)
        }
      }
    }
  }
  check(arrays)

  return result
}

console.log('[Here] ', solution(1, 2, [3], 1))