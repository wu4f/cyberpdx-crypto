import java.io.InputStream;

public class ProcessMessage {
    public static void main(String[] args) {
	if (args.length < 1) {
	    System.err.println("Usage: java ProcessMessage WIDTH [TITLE]");
	    System.exit(1);
	}

	String title = args.length < 2 ? "Message" : args[1];

	try {
	    // First print the preamble
	    System.out.println("\\begin{minipage}{\\textwidth}\\begin{center} " + title + " \\end{center}\\hrule\\begin{center}");
	    System.out.println("\\Large\n");
	    System.out.println("\\begin{verbatim}\n");

	    int width = Integer.parseInt(args[0]);
	    int col = 0;
	    int val = System.in.read();
	    while (val != -1) {
		System.out.print((char) val);
		col++;
		if (col == width) {
		    // Reached the end of the line
		    col = 0;
		    System.out.println();
		    System.out.println();
		}
		val = System.in.read();
	    }
	    System.out.println("\n\\end{verbatim}\\end{center}\\end{minipage}");
	} catch (Exception e) { }
    }
}
