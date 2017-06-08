public class Factorer {
    // A very simple (unintelligent) factorer
    public static void main(String[] args) {
	long num = Long.parseLong(args[0]);
	System.out.println("Factoring " + num);
	long max = (long) (Math.sqrt(num)+1);
	int i;
	for (i = 2; i <= max; i++) {
	    while (num % i == 0) {
		// Found a factor
		System.out.print(i + " ");
		num /= i;
		max = (long) (Math.sqrt(num)+1);
	    }
	}
	System.out.println(num);
    }
}
