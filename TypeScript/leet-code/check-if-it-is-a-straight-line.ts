{
  function checkStraightLine(coordinates: number[][]): boolean {
    if (coordinates.length <= 0) {
      return true;
    }
    const point1 = coordinates[0],
      point2 = coordinates[1];

    if (point1[0] === point2[0]) {
      for (let i = 2; i < coordinates.length; i++) {
        if (point1[0] !== coordinates[i][0]) {
          return false;
        }
      }
    } else {
      const m = (point2[1] - point1[1]) / (point2[0] - point1[0]),
        b = point1[1] - m * point1[0];
      for (let i = 2; i < coordinates.length; i++) {
        if (coordinates[i][1] !== coordinates[i][0] * m + b) {
          return false;
        }
      }
    }

    return true;
  }

  let a: any[] = [
      [
        [1, 2],
        [2, 3],
        [3, 4],
        [4, 5],
        [5, 6],
        [6, 7],
      ],
      [
        [1, 1],
        [2, 2],
        [3, 4],
        [4, 5],
        [5, 6],
        [7, 7],
      ],
      [
        [0, 0],
        [0, 1],
        [0, -1],
      ],
    ],
    b: any[] = [];
  const startTime = Date.now();
  a.forEach((aElement, _i) => {
    console.log(JSON.stringify(checkStraightLine(aElement)));
  });
  const endTime = Date.now();
  console.log(`\nExecution time: ${endTime - startTime} milliseconds`);
}
