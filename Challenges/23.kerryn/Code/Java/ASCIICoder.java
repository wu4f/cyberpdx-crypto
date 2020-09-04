public class ASCIICoder {
    public static String secondMessage = 
	"Nice.  You can connect with this... ";

    public static void main(String[] args) {
	if (args.length < 2) {
	    System.err.println("Usage: java ASCIICoder BASE Message1 Message2 ...");
	    System.err.println("       BASE=10 (Decimal) or 16 (Hexadecimal)");
	    System.exit(1);
	}

	int base = 10;
	try {
	    base = Integer.parseInt(args[0]);
	} catch (NumberFormatException e) {
	    System.err.println("Error: Base value was not recognized.  Use 10 or 16.");
	    System.exit(1);
	}

	// This wraps multiple codes over and over again (if interested)
	int m;
	String encryptedMessage = "";
	for (m = args.length-1; m > 0; m--) {
	    String message = args[m] + encryptedMessage;
	    encryptedMessage = encryptIt(base, message);
	    System.err.println(message + " ==> " + encryptedMessage);
	}
	
	System.out.println(encryptedMessage);
    }

    public static String encryptIt(int base, String message) {
	String encrypted = "";
	for (int i = 0; i < message.length(); i++) {
	    char letter = message.charAt(i);
	    int value = (int) (letter);

	    encrypted = encrypted + Integer.toString(value, base).toUpperCase();
	    if (i < message.length()-1) encrypted = encrypted + " ";
	}
	return encrypted;
    }
}
