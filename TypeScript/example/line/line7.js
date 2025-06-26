{
  function solution(list) {
    // Provide your solution here
    var result = {}
    function assign(_splittedElements, length, index, _result) {
      let value = true
      if (index !== length - 1) {
        value = _result[_splittedElements[index]] || {}
      }
      _result[_splittedElements[index]] = value
      if (index === length) {
        return
      } else {
        assign(_splittedElements, length, index + 1, _result[_splittedElements[index]])
      }
    }
    for (let element of list) {
      let splittedElements = element.split("/")
      assign(splittedElements, splittedElements.length, 0, result)

    }
    return result;
  }

  let a = [[
    'a/b/c',
    'a/b/d/e',
    'a/b/d/f'
  ]];
  a.forEach((aElement, _index) => {
    console.log(JSON.stringify(solution(aElement)));
  });
}
