import java.io.File

typealias Pattern = Map<Pair<Int, Int>, Char>

fun Pattern.rotate(): Pattern =
    this.mapKeys {
        val (row, col) = it.key
        Pair(col, row)
    }

fun Pattern.maxRow() = this.maxOf { it.key.first }

fun Pattern.maxCol() = this.maxOf { it.key.second }

fun Pattern.print() {
    (0..this.maxRow()).forEach { row ->
        println((0..this.maxCol()).map { col -> this[Pair(row, col)] }.joinToString(""))
    }
    println("")
}

fun computeLoad(pattern: Pattern): Int =
    (0..pattern.maxCol()).sumOf { col ->
        val glyphs = (0..pattern.maxRow()).map { row -> pattern[Pair(row, col)]!! }.joinToString("")
        val tilted =
            glyphs.split("#").map { chunk ->
                chunk.toCharArray().sortedDescending().joinToString("")
            }.joinToString("#")
        tilted.reversed().foldIndexed(0) { index, acc, char ->
            acc +
                when (char) {
                    'O' -> index + 1
                    else -> 0
                }
        }.toInt()
    }

fun main() {
    File("input.txt").readText().split("\n").flatMapIndexed { row, line ->
        line.trim().mapIndexed { col, char ->
            Pair(row, col) to char
        }
    }.toMap().let { pattern -> computeLoad(pattern) }.let { result -> println(result) }
}
