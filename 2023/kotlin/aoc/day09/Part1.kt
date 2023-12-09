fun List<Int>.diff(): List<Int> = this.zipWithNext().map { (a, b) -> b - a }

fun List<Int>.extrapolate(): Int =
    when {
        this.all { it == 0 } -> 0
        else -> this.last() + this.diff().extrapolate()
    }

fun main() {
    System.`in`.bufferedReader().lineSequence().map { line ->
        line.trim().split(" ").map { it.toInt() }.extrapolate()
    }.sum().let { result -> println(result) }
}
