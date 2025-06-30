{
	function largestPerimeter(nums: number[]): number {
		function isTriangle(a: number, b: number, c: number): boolean {
			return a + b > c && a + c > b && b + c > a
		}
		nums.sort((a, b) => a - b);
		const length = nums.length
		for (let i = length - 1; i >= 2; i--) {
			if (isTriangle(nums[i], nums[i - 1], nums[i - 2])) {
				return nums[i] + nums[i - 1] + nums[i - 2];
			}
		}
		return 0
	};

	let a: any[] = [
		// [2, 1, 2],
		// [1, 2, 1, 10],
		[1, 2, 2, 4, 18, 8]
	]
	a.forEach((aElement, _index) => {
		console.log(largestPerimeter(aElement));
	})
}