import kotlin.math.pow

fun Int.pow(x: Int): Int = this.toDouble().pow(x).toInt()

fun main() {
    System.`in`.bufferedReader().lineSequence().sumOf { line ->
        val (winning, seen) =
            line.trim().split(": ")[1].split(" | ").map { numberString ->
                numberString.trim().split("\\s+".toRegex()).map {
                    it.toInt()
                }.toSet()
            }
        2.pow(winning.intersect(seen).size - 1)
    }.let { result ->
        println(result)
    }
}
