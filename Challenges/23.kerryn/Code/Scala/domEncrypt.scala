/****
 * domEncrypt
 *    This simple program takes a graph as input and a number and
 *    returns an encryption of the number on each node of the graph.
 *    --- See CS Unplugged's Public/Private Key Encryption Scheme.
 *    The input graph is as a list of edges.
 ****/
import scala.util.Random

val rand = new Random()

def readGraph: Array[List[Int]] = {
  val n: Int = readInt   // How many nodes
  val e: Int = readInt   // How many edges
  val graph = Array.fill(n)(List[Int]())

  for (i <- 0 until e) {
    // Read in the end points of the edge
    val line = readLine.split(" ").map(_.toInt)
    val (a,b) = (line(0), line(1))

    // And add it to the graph (for ease making it symmetric)
    graph(a) ::= b
    graph(b) ::= a
  }

  // Sort the edge list for each node
  for (i <- 0 until n) {
    graph(i) = graph(i).sortWith(_<_)
  }

  return graph
}

def encrypt(graph: Array[List[Int]], n: Int): Array[Int] = {
  val sum = Array.fill(graph.length)(0)
  for (i <- 0 until n) 
    sum(rand.nextInt(graph.length)) += 1

  println("Sum = " + sum.mkString(" "))
  val enc = new Array[Int](graph.length)
  for (i <- sum.indices) {
    var total = sum(i)
    for (b <- graph(i))
      total += sum(b)
    enc(i) = total
  }
  return enc
}

if (args.length < 1) {
  println("Error: Too few arguments.")
  sys.exit(1)
}

val msg = args(0)
val g = readGraph
for (i <- msg.indices) {
  val num = msg(i).toInt
  println("Encrypting " + num)

  val enc = encrypt(g, num)
  println("arr"+i+"=( "+enc.mkString(" ")+" )")

  for (i <- enc.indices) {
    print("(" + i + " " + enc(i) + ") ")
  }
  println
}
