{
  function validMountainArray(arr: number[]): boolean {
    const length = arr.length;
    if (length < 3) {
      return false;
    }
    let left = 1,
      right = length - 2,
      leftTop = -1,
      rightTop = 1001;

    while (
      left < length &&
      right > -1 &&
      (leftTop === -1 || rightTop === 1001) &&
      leftTop !== rightTop
    ) {
      if (leftTop === -1) {
        if (arr[left] > arr[left - 1]) {
          left++;
        } else if (arr[left] === arr[left - 1]) {
          return false;
        } else {
          leftTop = left - 1;
        }
      }

      if (rightTop === 1001) {
        if (arr[right] > arr[right + 1]) {
          right--;
        } else if (arr[right] === arr[right + 1]) {
          return false;
        } else {
          rightTop = right + 1;
        }
      }
    }
    return leftTop === rightTop;
  }

  // if (arr[0] > arr[1]) {
  // 	return false;
  // }
  // for (let i = 1; i < arr.length; i++) {
  // 	const num = arr[i],
  // 		numPrevious = arr[i - 1]
  // 	if (num === numPrevious) {
  // 		return false;
  // 	}

  // 	if (isGoUp) {
  // 		if (numPrevious > num) {
  // 			isGoUp = false;
  // 		}
  // 	} else {
  // 		if (numPrevious < num) {
  // 			return false;
  // 		}
  // 	}
  // }
  // return !isGoUp;

  let a: any[] = [
    [2, 1],
    [3, 5, 5],
    [0, 3, 2, 1],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7],
  ];
  a.forEach((aElement, _index) => {
    console.log(validMountainArray(aElement));
  });
}
