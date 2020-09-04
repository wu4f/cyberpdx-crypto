/***
 * Author: Christian Duncan
 * Class: RodMessage
 *    This creates a simple rod message style message
 *    It works by taking a message (or multiple ones)
 *    and with a given size k places each message after
 *    the kth slot (skip counting in essence).
 *    So, the message GOOD_LUCKYOU_CAN_DOIT! with a value of k=3
 *    becomes 
 *    G..O..O..D.._..L..U..C..K..
 *    .Y..O..U.._..C..A..N.._..D.
 *    ..O..I..T..!..Y..Z..Q..W..E
 *    Or
 *    GYOOOIOUTD_!_CYLAZUNQC_WKDE
 *    Note the addition of some extra (random) characters at the end.
 ***/

import java.util.Random;

public class RodMessage {
    public static void main(String[] args) {
	if (args.length != 2) {
	    System.err.println("Usage: java RodMessage k1 MSG1");
	    System.exit(1);
	}

	int k = Integer.parseInt(args[0]);
	String msg = args[1];
	int max = msg.length();
	int rem = max % k;
	Random ran = new Random();
	if (rem > 0) {
	    // Adjust for space by padding with extra characters
	    max += (k - rem);
	    while (rem < k) {
		msg += (char) (ran.nextInt(26) + 'A');
		rem++;
	    }
	}

	char comb[] = new char[max];
	int cols = max / k;
	for (int c = 0, i = 0; c < cols; c++) {
	    for (int r = 0; r < k; r++, i++) {
		comb[i] = msg.charAt(c+r*cols);
	    }
	}

	System.out.println(comb);
    }
}
