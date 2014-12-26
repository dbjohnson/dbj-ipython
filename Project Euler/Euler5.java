

class Euler5 {
	public static void main(String [] args) {
		
		int maxDivisor = 20;
		int winner = 0;
	
		long t = System.currentTimeMillis();
	
		int n = maxDivisor;
		while (true) {
			boolean foundIt = true;
			for (int divisor = maxDivisor - 1; divisor > 1; --divisor) {
				if ((n % divisor) != 0) {
					foundIt = false;
					break;
				}
			}

			if (foundIt) {
				winner = n;
				break;
			}
			n += maxDivisor;
		}
	 	t = System.currentTimeMillis() - t;
	
		System.out.printf("Smallest value: %d\n", winner);
	  	System.out.printf ("Elapsed time: %1.2es\n",t / 1000.0);
	
	}
}