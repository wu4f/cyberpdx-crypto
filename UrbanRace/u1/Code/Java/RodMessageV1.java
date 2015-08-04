/***
 * Author: Christian Duncan
 * Class: RodMessage
 *    This creates a simple rod message style message
 *    It works by taking a message (or multiple ones)
 *    and with a given size k places each message after
 *    the kth slot (skip counting in essence) - starting with l
 *    It does this for a different k,l for each string
 *    The trick is knowing the value of k,l and also 
 *    making the overlaps work together (or avoiding them)
 *    The remaining space is filled in with random letters.
 ***/

import java.util.Random;

public class RodMessage {
    public static void main(String[] args) {
	if (args.length < 3) {
	    System.err.println("Usage: java RodMessage k1 l1 MSG1 [ k2 l2 MSG2 k3 l3 MSG3 ... ]");
	    System.exit(1);
	}

	int[] k = new int[args.length/3];
	int[] l = new int[args.length/3];

	// Get max size length
	k[0] = Integer.parseInt(args[0]);
	l[0] = Integer.parseInt(args[1]);

	int max = args[2].length() * k[0] + l[0];
	int i, j;
	for (i = 1; i*3 < args.length; i++) {
	    k[i] = Integer.parseInt(args[i*3]);
	    l[i] = Integer.parseInt(args[i*3+1]);
	    int val = k[i] * args[i*3+2].length() + l[i];
	    if (max < val) { max = val; }
	}

	char comb[] = new char[max];
	for (i = 0; i < max; i++) comb[i] = 0;
	
	// Now fill in the values (checking to be sure each slot is blank)
	for (i = 0; i*3 < args.length; i++) {
	    String curr = args[i*3+2];
	    for (j = 0; j < curr.length(); j++) {
		char c = curr.charAt(j);
		int ind = k[i]*j + l[i];
		if (comb[ind] != 0 && comb[ind] != c) {
		    System.err.println("Overlap error!");
		} else {
		    comb[ind] = c;
		}
	    }
	}

	Random ran = new Random();

	// Now fill in the gaps
	for (i = 0; i < max; i++) {
	    if (comb[i] == 0) {
		// Fill in with a random letter (for now)
		comb[i] = (char) (ran.nextInt(26) + 'A');
	    }
	}

	System.out.println(comb);
    }
}
