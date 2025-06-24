{
	function numUniqueEmails(emails: string[]): number {
		function getFinalEmail(_email: string): string {
			if (!_email) {
				return "";
			}
			const splittedEmail = _email.split("@"),
				localName = splittedEmail[0],
				domainName = splittedEmail[1],
				localEmailBeforePlus = localName.split("+")[0];
			return `${localEmailBeforePlus.replace(/\./g, "")}@${domainName}`;
		}

		const set: Set<string> = new Set<string>()
		for (let email of emails) {
			let finalEmail: string = getFinalEmail(email)
			set.add(finalEmail)
		}

		return set.size;
	};

	let a: any[] = [
		// ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"],
		// ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"],
		["test.email+alex@leetcode.com", "test.email.leet+alex@code.com"]]
	a.forEach((aElement, _index) => {
		console.log(numUniqueEmails(aElement));
	})
}