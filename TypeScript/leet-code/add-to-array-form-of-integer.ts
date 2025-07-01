{
	function addToArrayForm(num: number[], k: number): number[] {
		const numsK: number[] = [],
			result: number[] = []
		let divider: number = 10
		while (k !== 0) {
			numsK.push(k % divider);
			k = Math.floor(k / divider)
		}

		const lengthK = numsK.length
		let i = num.length - 1,
			j = 0,
			remmant = 0,
			numK = numsK[j]
		while (i >= 0 || j <= lengthK - 1) {
			const total = (num[i] || 0) + numK + remmant
			remmant = Math.floor(total / 10)
			result.push(total % 10)
			if (j <= lengthK - 1) {
				j++
				numK = numsK[j] || 0
			}
			if (i >= 0) i--
		}
		if (remmant === 1) {
			result.push(1)
		}
		return result.reverse()
	};

	let a: any[] = [[1, 2, 0, 0], [2, 7, 4], [2, 1, 5]],
		b: any[] = [34, 181, 806]
	a.forEach((aElement, _index) => {
		console.log(addToArrayForm(aElement, b[_index]));
	})
}