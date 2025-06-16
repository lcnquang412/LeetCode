{
  function largestTriangleArea(points: number[][]): number {
    let maxResult = -1.0;

    function getTriangleArea(
      point1: number[],
      point2: number[],
      point3: number[]
    ): number {
      return (
        0.5 *
        Math.abs(
          point1[0] * (point2[1] - point3[1]) +
            point2[0] * (point3[1] - point1[1]) +
            point3[0] * (point1[1] - point2[1])
        )
      );
    }

    const length = points.length;
    for (let i = 0; i < length - 2; i++) {
      const point1: number[] = points[i];
      for (let j = i + 1; j < length - 1; j++) {
        const point2: number[] = points[j];
        for (let k = j + 1; k < length; k++) {
          const point3: number[] = points[k];
          maxResult = Math.max(
            maxResult,
            getTriangleArea(point1, point2, point3)
          );
        }
      }
    }
    return maxResult;
  }

  //   let a: any = [
  //     [0, 0],
  //     [0, 1],
  //     [1, 0],
  //     [0, 2],
  //     [2, 0],
  //   ];
  let a: any = [
    [1, 0],
    [0, 0],
    [0, 1],
  ];
  console.log(largestTriangleArea(a));
}
