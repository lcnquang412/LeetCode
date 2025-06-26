// {
//   function solution(v) {
//     var answer = [
//       []
//     ];

//     return answer;
//   }

//   let a = [];
//   a.forEach((aElement, _index) => {
//     console.log(solution(aElement));
//   });
// }

// eval(function (p, a, c, k, e, d) { e = function (c) { return c }; if (!''.replace(/^/, String)) { while (c--) { d[c] = k[c] || c } k = [function (e) { return d[e] }]; e = function () { return '\\w+' }; c = 1 }; while (c--) { if (k[c]) { p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c]) } } return p }('4.5.7("9"),4.5.10("8",3=>{6 0=1.11(3);12.17(1.18(16(0.15)(0.13),14,2))});', 10, 19, 't|JSON||s|process|stdin|var|setEncoding|data|utf8|on|parse|console|text|null|tag|solution|log|stringify'.split('|'), 0, {}))


function solution(tag) {
  // Provide your solution here
  function escapedHtml(str) {
    if (!str) {
      return ""
    }
    var map = {
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      '"': '&quot;',
      "'": '&#039;'
    };
    return str.replace(/[&<>"']/g, function (m) { return map[m] })
  }
  function combine(content) {
    return `<${tag}>${escapedHtml(content)}</${tag}>`
  }
  return combine;
}

console.log(solution('h1')('<quang>'))