{
	function validMountainArray(arr: number[]): boolean {
		let isGoUp: boolean = true;
		if (arr.length < 3) {
			return false;
		}
		if (arr[0] > arr[1]) {
			return false;
		}
		for (let i = 1; i < arr.length; i++) {
			const num = arr[i],
				numPrevious = arr[i - 1]
			if (num === numPrevious) {
				return false;
			}

			if (isGoUp) {
				if (numPrevious > num) {
					isGoUp = false;
				}
			} else {
				if (numPrevious < num) {
					return false;
				}
			}
		}
		return !isGoUp;
	};

	let a: any[] = [
		[2, 1],
		[3, 5, 5],
		[0, 3, 2, 1],
		[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
		[9, 8, 7]
	]
	a.forEach((aElement, _index) => {
		console.log(validMountainArray(aElement));
	})
}