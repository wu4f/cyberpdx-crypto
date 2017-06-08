/***
 * A very smiple RSA implementation.
 *  Used more to illustrate the process
 *  and not for security at all
 ***/
import java.util.Scanner;

public class SimpleRSA {
    public static void main(String[] args) {
	if (args.length < 2) {
	    // Need the keys
	    System.err.println("Usage: java SimpleRSA E N\n");
	    System.exit(1);
	}

	int e = Integer.parseInt(args[0]);
	int n = Integer.parseInt(args[1]);
	// n = p*q and e is relatively prime to phi(n)=(p-1)*(q-1)
	// d: inverse of e (the two are essentially interchangeable)

	// Now read in the message (a sequence of numbers)
	String message;
	Scanner in = new Scanner(System.in);

	while (in.hasNextInt()) {
	    int p = in.nextInt();

	    // Now we have the number, convert it
	    int c = modPower(p,e,n);
	    
	    // And output it
	    System.out.print(c + " ");
	}
	System.out.println();
    }

    /***
     * Computes P^e (mod n)
     *   This is an inefficient means but works 
     *   for small enough e and n
     ***/
    public static int modPower(int p, int e, int n) {
	int ans = 1;
	while (e > 0) {
	    ans *= p;
	    ans = ans % n;  // Take remainder each step
	    e--;
	}
	return ans;
    }
}
