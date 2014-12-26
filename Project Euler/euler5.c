#include <stdio.h>
#include <time.h>    


int main() {
	
	clock_t t = clock();
	
	int maxDivisor = 20;
	int winner = 0;
	int n = maxDivisor;

	while (1) {
		int foundIt = 1;
		int divisor = 0;
		for (divisor = maxDivisor - 1; divisor > 1; --divisor) {
			if ((n % divisor) != 0) {
				foundIt = 0;
				break;
			}
		}

		if (foundIt == 1) {
			winner = n;
			break;
		}
		n += maxDivisor;
	}
 	t = clock() - t;
	
	printf("Smallest value: %d\n", winner);
  	printf ("Elapsed time: %1.2es\n",((float)t)/CLOCKS_PER_SEC);
	
	return 0;
}