{
  function minTimeToVisitAllPoints(points: number[][]): number {
    let res: number = 0;
    for (let i = 1; i < points.length; i++) {
      const prevPoint: number[] = points[i - 1],
        currPoint: number[] = points[i],
        gapX: number = Math.abs(prevPoint[0] - currPoint[0]),
        gapY: number = Math.abs(prevPoint[1] - currPoint[1]);

      res += Math.min(gapX, gapY) + Math.abs(gapX - gapY);
    }

    return res;
  }

  let a: any[] = [
      [
        [1, 1],
        [3, 4],
        [-1, 0],
      ],
      [
        [3, 2],
        [-2, 2],
      ],
    ],
    b: any[] = [];
  const startTime = Date.now();
  a.forEach((aElement, _i) => {
    console.log(JSON.stringify(minTimeToVisitAllPoints(aElement)));
  });
  const endTime = Date.now();
  console.log(`\nExecution time: ${endTime - startTime} milliseconds`);
}
