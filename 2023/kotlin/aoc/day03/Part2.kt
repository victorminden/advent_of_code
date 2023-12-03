typealias Coordinate = Pair<Int, Int>

fun Char.isSymbol(): Boolean = !this.isDigit() && this != '.'

fun main() {
    val paddedLines =
        System.`in`.bufferedReader().lineSequence().map { line ->
            ".${line.trim()}."
        }.toList().let { lines ->
            val n = lines[0].length
            listOf(".".repeat(n)) + lines + listOf(".".repeat(n))
        }
    val symbolsToParts = mutableMapOf<Coordinate, List<Int>>()
    paddedLines.windowed(3).forEachIndexed { lineIndex, (prev, curr, next) ->
        var partNumber = 0
        var looksGood = false
        var adjacentSymbols = mutableSetOf<Coordinate>()
        for (index in 1 until curr.length - 1) {
            val c = curr[index]
            if (!c.isDigit()) {
                looksGood = false
                partNumber = 0
                adjacentSymbols = mutableSetOf<Coordinate>()
                continue
            }

            partNumber = 10 * partNumber + c.digitToInt()

            (index - 1..index + 1).forEach { colIndex ->
                listOf(Pair(lineIndex - 1, prev[colIndex]), Pair(lineIndex, curr[colIndex]), Pair(lineIndex + 1, next[colIndex])).forEach {
                        (rowIndex, element) ->
                    if (element.isSymbol()) {
                        adjacentSymbols += Coordinate(rowIndex, colIndex)
                        looksGood = true
                    }
                } 
            }

            if (!curr[index + 1].isDigit() && looksGood) {
                adjacentSymbols.forEach { coordinate ->
                    symbolsToParts[coordinate] = (symbolsToParts[coordinate] ?: mutableListOf()) + partNumber
                }
            }
        }
    }

    println(symbolsToParts.values.filter { it.size == 2 }.fold(0) { acc, (a, b) -> acc + (a * b) })
}
