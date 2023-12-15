import java.io.File

typealias Pattern = Map<Pair<Int, Int>, Char>

fun Pattern.rotate(): Pattern =
    this.mapKeys {
        val (row, col) = it.key
        val newRow = col
        val newCol = this.maxRow() - row
        Pair(newRow, newCol)
    }

fun Pattern.maxRow() = this.maxOf { it.key.first }

fun Pattern.maxCol() = this.maxOf { it.key.second }

fun Pattern.print() {
    (0..this.maxRow()).forEach { row ->
        println((0..this.maxCol()).map { col -> this[Pair(row, col)] }.joinToString(""))
    }
    println("")
}

fun tilt(pattern: Pattern): Pattern =
    (0..pattern.maxCol()).flatMap { col ->
        val glyphs = (0..pattern.maxRow()).map { row -> pattern[Pair(row, col)]!! }.joinToString("")
        val tilted =
            glyphs.split("#").map { chunk ->
                chunk.toCharArray().sortedDescending().joinToString("")
            }.joinToString("#")
        tilted.mapIndexed { row, char -> Pair(row, col) to char }
    }.toMap()

fun computeLoad(pattern: Pattern): Int =
    (0..pattern.maxCol()).sumOf { col ->
        val glyphs = (0..pattern.maxRow()).map { row -> pattern[Pair(row, col)]!! }.joinToString("")
        glyphs.reversed().foldIndexed(0) { index, acc, char ->
            acc +
                when (char) {
                    'O' -> index + 1
                    else -> 0
                }
        }.toInt()
    }

fun part2(pattern: Pattern): Int {
    fun cycle(pattern: Pattern): Pattern = tilt(tilt(tilt(tilt(pattern).rotate()).rotate()).rotate()).rotate()

    val p2i = mutableMapOf(pattern.toString() to 0)
    var p = pattern
    val maxIts = 1000000000
    (1..maxIts).forEach { i ->
        println(i)
        p = cycle(p)

        p2i[p.toString()]?.let { j ->
            val cycleLength = i - j
            val remaining = maxIts - i
            val equivalentRemaining = remaining.mod(cycleLength)
            (1..equivalentRemaining).forEach {
                p = cycle(p)
            }
            return computeLoad(p)
        }
        p2i[p.toString()] = i
    }
    return -1
}

fun main() {
    File("input.txt").readText().split("\n").flatMapIndexed { row, line ->
        line.trim().mapIndexed { col, char ->
            Pair(row, col) to char
        }
    }.toMap().let { pattern -> part2(pattern) }.let { result -> println(result) }
}
