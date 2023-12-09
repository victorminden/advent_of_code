fun List<Int>.diff(): List<Int> = this.zipWithNext().map { (a, b) -> b - a }

fun List<Int>.extrapolateBackwards(): Int =
    when {
        this.all { it == 0 } -> 0
        else -> this.first() - this.diff().extrapolateBackwards()
    }

fun main() {
    System.`in`.bufferedReader().lineSequence().map { line ->
        line.trim().split(" ").map { it.toInt() }.extrapolateBackwards()
    }.sum().let { result -> println(result) }
}
