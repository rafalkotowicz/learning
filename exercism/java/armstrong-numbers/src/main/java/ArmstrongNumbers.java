class ArmstrongNumbers {

	boolean isArmstrongNumber(int numberToCheck) {
		int sum = 0;
		int noOfDigits = String.valueOf(numberToCheck).length();
		for (int i = numberToCheck; i > 0; i/=10) {
			sum += Math.pow(i % 10, noOfDigits);
		}

		return sum == numberToCheck;
	}

}
