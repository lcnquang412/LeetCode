{
	function diStringMatch(s: string): number[] {
		const n = s.length,
			result: number[] = [];
		let left = 0,
			right = n
		for (let i = 0; i < n; i++) {
			if (s[i] === 'I') {
				result.push(left++)
			} else {
				result.push(right--)
			}
		}
		result.push(left)
		return result;
	};

	let a: any[] = [
		'IDID',
		"III",
		"DDI"
	]
	a.forEach((aElement, _index) => {
		console.log(diStringMatch(aElement));
	})
}