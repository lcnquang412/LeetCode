{
	function sortArrayByParityII(nums: number[]): number[] {
		let i: number = 0,
			iEven: number = 0,
			iOdd: number = 1
		while (i < nums.length) {
			let num = nums[i]
			if (num % 2 === 0) {
				if (i % 2 === 0) {
					i++
				} else {
					[nums[i], nums[iEven]] = [nums[iEven], nums[i]]
					iEven += 2
				}
			} else {
				if (i % 2 === 1) {
					i++
				} else {
					[nums[i], nums[iOdd]] = [nums[iOdd], nums[i]]
					iOdd += 2
				}
			}
		}
		return nums
	};

	let a: any[] = [[4, 2, 5, 7], [2, 3]]
	a.forEach((aElement, _index) => {
		console.log(sortArrayByParityII(aElement));
	})
}