{
  function distanceBetweenBusStops(
    distance: number[],
    start: number,
    destination: number
  ): number {
    function traverse(s: number, d: number): number {
      let i: number = s,
        total: number = 0;
      while (i !== d) {
        total += distance[i++];
        if (i === distance.length) {
          i = 0;
        }
      }
      return total;
    }

    return Math.min(traverse(start, destination), traverse(destination, start));
  }

  let a: any[] = [
      [1, 2, 3, 4],
      [1, 2, 3, 4],
      [1, 2, 3, 4],
    ],
    b: any[] = [0, 0, 0],
    c: any[] = [1, 2, 3];
  const startTime = Date.now();
  a.forEach((aElement, _index) => {
    console.log(distanceBetweenBusStops(aElement, b[_index], c[_index]));
  });
  const endTime = Date.now();
  console.log(`\nExecution time: ${endTime - startTime} milliseconds`);
}
