import java.util.Scanner;

public class ASCIIDecoder {
    public static void main(String[] args) {
	Scanner in = new Scanner(System.in);

	while (in.hasNextInt()) {
	    int i = in.nextInt();
	    char c = (char) i;
	    System.out.print(c);
	}
	System.out.println();
    }
}
