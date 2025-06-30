{
	function repeatedNTimes(nums: number[]): number {
		const set: Set<number> = new Set<number>()
		for (let num of nums) {
			if (set.has(num)) {
				return num;
			} else {
				set.add(num);
			}
		}
		return 0;
	};

	let a: any[] = [[1, 2, 3, 3], [2, 1, 2, 5, 3, 2], [5, 1, 5, 2, 5, 3, 5, 4]]
	a.forEach((aElement, _index) => {
		console.log(repeatedNTimes(aElement));
	})
}