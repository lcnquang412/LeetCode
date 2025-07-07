{
  function isBoomerang(points: number[][]): boolean {
    return (
      points[0][0] * (points[1][1] - points[2][1]) +
        points[1][0] * (points[2][1] - points[0][1]) +
        points[2][0] * (points[0][1] - points[1][1]) !==
      0
    );
  }

  let a: any[] = [
      [
        [1, 1],
        [2, 3],
        [3, 2],
      ],
      [
        [1, 1],
        [2, 2],
        [3, 3],
      ],
      [
        [0, 0],
        [0, 2],
        [2, 1],
      ],
    ],
    b: any[] = [];
  a.forEach((aElement, _index) => {
    console.log(isBoomerang(aElement));
  });
}
