/***
 * This program takes a flag -d or -e and a cipher key on the command line
 * and a text as input.
 * It then precedes to decrypt (or encrypt) the text using the cipher key.
 * It assumes all characters are upper-case alphabetic values
 *
 * Example:
 *    java WordCipher -d ARTICHOKE
 *        HGIMOCRVMVFNNUA
 *    Outputs:
 *        GOODLUCKHUNTERS
 *
 * Actually, switched to use A as shift 0... 
 ***/
import java.util.Scanner;

public class WordCipher {
    public static void printUsage() {
	System.err.println("Usage: java WordCipher -[d|e] KEY");
	System.exit(1);
    }

    public static void main(String[] args) {
	boolean encryptFlag = true;
	if (args.length < 2) {
	    printUsage();
	}

	if ("-e".equals(args[0])) {
	    encryptFlag = true;
	} else if ("-d".equals(args[0])) {
	    encryptFlag = false;
	} else {
	    printUsage();
	}

	String key = args[1];
	key = key.toUpperCase();  // No check for pure A-Z

	Scanner in = new Scanner(System.in);
	while (in.hasNext()) {
	    String line = in.nextLine();
	    String crypt = cipher(encryptFlag, key, line);
	    System.out.println(crypt);
	}
    }

    public static String cipher(boolean flag, String key, String message) {
	message = message.toUpperCase();
	String crypt = "";

	int ml = message.length();
	int kl = key.length();
	int i, j;
	for (i = j = 0; i < ml; i++) {
	    // Message character (A=0, Z=25)
	    char mc = (char) (message.charAt(i) - 'A');
	    char c;

	    if (mc < 0 || mc > 25) {
		// It was not a letter in range A-Z
		// We only encrypt/decrypt those letters...
		// Ignore others (well leave them alone)
		c = message.charAt(i);
	    } else {
		// And the key character
		char kc = (char) (key.charAt(j)- 'A');
		// We start counting from 0... I believe...
		j++; if (j >= kl) j = 0;  // Move to the next key
		
		// Add or subtract the two values depending on the
		// flag...
		c = (char) ('A' + (flag ? ((mc + kc) % 26) :
				    (26 + mc - kc) % 26));
	    }
	    crypt += c;
	}
	return crypt;
    }
}
