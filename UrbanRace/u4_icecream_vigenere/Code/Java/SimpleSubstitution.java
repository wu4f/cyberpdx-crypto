/***
 * This program takes a flag -d or -e and a cipher key on the command line
 * and a text as input.
 * It then precedes to decrypt (or encrypt) the text using the cipher key.
 * It assumes all characters are upper-case alphabetic values
 * This uses a straightforward simple substitution.
 * The key is a 26-letter alphabet for direct substitution
 *   (character by character - only A-Z allowed.)
 ***/
import java.util.Scanner;

public class SimpleSubstitution {
    public static void printUsage() {
	System.err.println("Usage: java SimpleSubstitution -[d|e] KEY");
	System.err.println("       KEY must be 26-letter cipher-alphabet (A-Z)");
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
	if (key.length() != 26) {
	    printUsage();
	}

	key = key.toUpperCase();  // No check for pure A-Z
	
	Scanner in = new Scanner(System.in);
	while (in.hasNext()) {
	    String line = in.nextLine();
	    String crypt = cipher(encryptFlag, key, line);
	    System.out.println(crypt);
	}
    }

    public static String cipher(boolean flag, String key, String message) {
	char[] map = new char[26];
	int i, j;
	if (flag) {
	    // Encrypting... using key directly
	    for (i = 0; i < 26; i++) {
		map[i] = key.charAt(i);
	    }
	} else {
	    // Decrypting so must convert the key.
	    for (i = 0; i < 26; i++) {
		map[key.charAt(i) - 'A'] = (char) (i + 'A');
	    }
	}

	String crypt = "";

	int ml = message.length();
	for (i = 0; i < ml; i++) {
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
		c = map[mc];
	    }
	    crypt += c;
	}
	return crypt;
    }
}
