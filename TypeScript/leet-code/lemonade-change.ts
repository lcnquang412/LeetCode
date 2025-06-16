{
	function lemonadeChange(bills: number[]): boolean {
		let balance: { [key: number]: number } = {
			5: 0,
			10: 0,
			20: 0,
		};

		for (let bill of bills) {
			balance[bill]++;
			if (bill === 10) {
				balance[5]--;
			} else if (bill === 20) {
				if (balance[10] > 0) {
					balance[10]--;
					balance[5]--;
				} else {
					balance[5] -= 3;
				}
			}
			if (balance[10] < 0 || balance[5] < 0) {
				return false;
			}
		}
		return true;
	}

	let a: any = [5, 5, 5, 10, 20];
	//   let a: any = [5, 5, 10, 10, 20];
	console.log(lemonadeChange(a));
}
