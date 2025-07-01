{
	function sortedSquares(nums: number[]): number[] {
		if (nums[0] >= 0) {
			return nums.map(e => e * e)
		} else {
			const length = nums.length
			if (nums[length - 1] <= 0) {
				return nums.map(e => e * e).reverse()
			}

			let right: number = nums.findIndex(e => e >= 0),
				left: number = right - 1,
				numsResorted: number[] = []

			while (left > -1 || right < length) {
				if (left === -1 && right < length) {
					numsResorted.push(nums[right++])
					continue;
				} else if (left > -1 && right === length) {
					numsResorted.push(nums[left--])
					continue;
				} else {
					if (Math.abs(nums[left]) < nums[right]) {
						numsResorted.push(nums[left--])
					} else {
						numsResorted.push(nums[right++])
					}
				}
			}

			return numsResorted.map(e => e * e)
		}
	};

	let a: any[] = [
		[-4, -1, 0, 3, 10],
		// [-7, -3, 2, 3, 11]
	]
	a.forEach((aElement, _index) => {
		console.log(sortedSquares(aElement));
	})
}