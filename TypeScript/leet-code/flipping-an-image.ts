{
	function flipAndInvertImage(image: number[][]): number[][] {
		for (let row of image) {
			let len: number = row.length;
			for (let i: number = 0; i < Math.ceil(len / 2); i++) {
				let tmp: number = row[i];
				row[i] = row[len - i - 1] ^ 1;
				row[len - i - 1] = tmp ^ 1;
			}
		}
		return image;
	}

	let a: any = [
		[1, 1, 0],
		[1, 0, 1],
		[0, 0, 0],
	];
	console.log(flipAndInvertImage(a));
}
