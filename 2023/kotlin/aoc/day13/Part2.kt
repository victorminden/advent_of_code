import java.io.File

typealias Pattern = Map<Pair<Int, Int>, Char>

fun Pattern.rotate(): Pattern =
    this.mapKeys {
        val (row, col) = it.key
        Pair(col, row)
    }

fun Pattern.print() {
    val maxRow = this.maxOf { it.key.first }
    val maxCol = this.maxOf { it.key.second }
    (0..maxRow).forEach { row ->
        println((0..maxCol).map { col -> this[Pair(row, col)] }.joinToString(""))
    }
    println("")
}

fun colSummary(pattern: Pattern): Int {
    val maxRow = pattern.maxOf { it.key.first }
    val maxCol = pattern.maxOf { it.key.second }
    return (1..maxCol).firstOrNull { cols ->
        (0..maxRow).asIterable().sumOf { rowId: Int ->
            val row = (0..maxCol).map { pattern[Pair(rowId, it)] }.toList()
            row.take(cols).reversed().zip(row.drop(cols)).asIterable().sumOf {
                    (a, b) ->
                (if (a == b) 0 else 1).toInt()
            }
        }.let { sum -> sum == 1 }
    } ?: 0
}

fun rowSummary(pattern: Pattern): Int = 100 * colSummary(pattern.rotate())

fun summarize(pattern: Pattern): Int = rowSummary(pattern) + colSummary(pattern)

fun main() {
    File("input.txt").readText().split("\n\n").map { pattern ->
        pattern.trim().split("\n").flatMapIndexed { row, line ->
            line.mapIndexed { col, char ->
                Pair(row, col) to char
            }
        }.toMap()
    }.sumOf { pattern ->
        summarize(pattern).also { if (it == 0) pattern.print() }
    }.let { result -> println(result) }
}
