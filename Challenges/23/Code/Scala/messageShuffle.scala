/**********
 * MessageShuffle
 * Author: Christian Duncan
 *    This short snippet of code takes a sentence and 
 *    randomly shuffles the letters between each word, 
 *    excluding the first and last ones.
 *    Suohld prdocue smoetihng lkie this.
 *    For now, keep it simple.  No punctuation - and all on one line.
 * *******/

import scala.util.Random
val ran = new Random

def mix(w: String): String = {
  if (w.length <= 3) w
  else w(0)+ran.shuffle(w.drop(1).dropRight(1).toList).mkString+w.takeRight(1)
}

// Read in the message and split into words
val words = scala.io.StdIn.readLine.filter(x=>(x.isLetter || x == ' ')).split(' ')
println("Scrambling: " + words.mkString(" "))
for (w <- words) {
  print(mix(w) + " ")
}
println
