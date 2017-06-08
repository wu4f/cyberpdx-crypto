/***
* Christian Duncan
* Written for Cyber Discovery Camp: Cyber-Hunt 2008-2011
*
* Group Message Puzzle
*   A message is written and split into X pieces that must be assembled to complete the message.
*   Each piece is distributed to another team with double redundany.
*   Purpose: To get students to meet other teams.
*   Combine the outputs of this program with the LaTeX file GroupMessage.tex
*
***/

public class GroupMessage {
    public static java.util.Random ran;

    // Note, each message must be the same length.  (Sigh, b/c I didn't want
    // to automate the process of adding random spaces.)
    public static String messages[] = {
	"If you are reading this, it means you have been able to get in contact with the other family members.  When the time comes, you will need to look closely at our Honorable Senator for the code word.",
        "Reading this means that you should have been in contact with the other prime Mersenne family members.  When the time is right, look closely at our Honorable Senator for the code word you seek.",
        "Deciphering this means you have been in contact with the other prime Mersenne members.  When the time comes, take a closer look at our Honorable Senator for the code word you shall need.",
	"If you deciphered this message, it means you have been in contact with the other Mersenne family members.  When the time comes, the codeword can be found by looking closer at our Honorable Senator.",
        "Decoding this message indicates you successfully contacted the other prime family members.  When the time comes, you shall find the code word you seek by looking closely at our Honorable Senator.",
	"I trust that you've been in contact with the other prime Mersenne family members, having this message.  When the time comes, find the code word you seek by looking closely at our Honorable Senator.",
        "Deciphering this means that you've been in contact with other prime Mersenne members.  Looking closely at our Honorable Senator, when the time comes, will lead you to the code word that you will need.",
        "Having deciphered this message, I hope that you have managed to contact the other Mersenne members. When the time is right, you may find the code word by looking closely at our Honorable Senator.",
        "Having deciphered this message, you must have contacted the other prime Mersenne members.  When the time comes, if you look closely at our Honorable Senator you should find the code word you seek.",
        "Decoding this message indicates you successfully contacted the other prime Mersenne family members.  When the time arrives, looking closely at the Honorable Senator will reveal the code word you seek."
    };
    public static int cols = 20;

    public static String preamble = "{\\Large\\bfseries\\itshape To crack this message, you'll need the help of the other members.}";

    public static void main(String[] args) {
	int team;

	ran = new java.util.Random();

	// Get longest message
	int max = messages[0].length();
	for (team = 1; team < messages.length; team++) {
	    if (messages[team].length() > max) { max = messages[team].length(); }
	}

	System.err.println("Max = " + max);
	// Even out the messages by adding spaces in between words
	for (team = 0; team < messages.length; team++) {
	    messages[team] = fillWithSpace(messages[team], max);
	    if (messages[team].length() != max) {
		System.err.println("Error!!!!!");
	    }
	}
	
	for (team = 0; team < messages.length; team++) {
	    createMessagePieces(team, messages[team], messages.length);
	}
    }

    public static String fillWithSpace(String message, int desiredLength) {
	// Fill strings with spaces in between words until reaches desired length
	int mLen = message.length();
	int diff = desiredLength - mLen;
	if (diff <= 0) return message;  // Nothing to do...
	char copy[] = new char[desiredLength];
	int a = 0, b = 0;
	while (a < mLen) {
	    char c = message.charAt(a);
	    copy[b++] = c;
	    if (c == ' ' && diff > 0) {
		// Add another space
		copy[b++] = c;
		diff--;
	    }
	    a++;
	}
	if (diff > 0) {
	    // At the end of string... gotta start all over
	    copy[b] = 0;
	    return fillWithSpace(new String(copy), desiredLength);
	}
	return new String(copy);
    }

    public static void createMessagePieces(int team, String message, int numPieces) {
	int assignment[][] = new int[message.length()][2];  // Double redundancy

	// Make the assignments first
	for (int i = 0; i < message.length(); i++) {
	    assignment[i][0] = ran.nextInt(numPieces);
	    do {
		assignment[i][1] = ran.nextInt(numPieces);
	    } while (assignment[i][1] == assignment[i][0]);
	}

	// Now generate the tables in TeX format
	
	// First the dimension
	// int cols = (int) (Math.sqrt(message.length()));

	for (int piece = 0; piece < numPieces; piece++) {
	    System.out.println("%------ Team (" + team + ") Piece (" + piece +") -------");
	    System.out.println("\\vfill");
	    System.out.println("\\hfill{\\Large\\bfseries " + (team+1) + "," + (((piece+team)%numPieces)+1) + "}\\\\");
	    if (piece == 0) System.out.println(preamble);
	    System.out.println("\\begin{center}");
	    System.out.println("\\begin{tabular}{|*{" + cols + "}{p{1em}|}}");
	    System.out.println("\\hline");
	    int curr;
	    int currCol;
	    for (curr = 0; curr < message.length();) {
		for (currCol = 0; currCol < cols; currCol++, curr++) {
		    if (curr < message.length() && 
			(assignment[curr][0] == piece ||
			 assignment[curr][1] == piece)) {
			// It is present in this piece (write it out)
			System.out.print("\\centering {" + message.charAt(curr) + "}" + 
					   ((currCol < cols - 1) ? " & " : "\\tabularnewline\n"));
		    } else {
			if (currCol < cols-1) {
			    System.out.print("  & ");
			} else {
			    System.out.println(" \\\\");
			}
		    }
		}
		System.out.println("\\hline");
	    }
	    System.out.println("\\end{tabular}");
	    System.out.println("\\end{center}");
	    System.out.println("\\vfill");
	    if (piece % 3 == 2) System.out.println("\\newpage");
	    else {
		System.out.println("%--------------------------");
		System.out.println("\\hrule");
		System.out.println();
		System.out.println();
	    }
	}
	System.out.println("\\newpage");
    }
}
