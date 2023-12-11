import kotlin.math.abs

typealias Coordinate = Pair<Int, Int>

fun main() {
    val points: List<Coordinate> =
        System.`in`.bufferedReader().lineSequence().flatMapIndexed { row, line ->
            line.trim().mapIndexedNotNull { col, char ->
                when (char) {
                    '#' -> Coordinate(row, col)
                    else -> null
                }
            }
        }.toList()
    val seenRows = points.map { it.first }.toSet()
    val seenCols = points.map { it.second }.toSet()
    val emptyRows = (0..seenRows.max()).toSet() - seenRows
    val emptyCols = (0..seenCols.max()).toSet() - seenCols

    points.flatMap { pointA ->
        points.map { pointB ->
            Pair(pointA, pointB)
        }
    }.map { (pointA, pointB) ->
        val undilatedDistance =
            abs(pointA.first - pointB.first) + abs(pointA.second - pointB.second)
        undilatedDistance +
            emptyRows.filter { row ->
                row in (pointA.first..pointB.first) ||
                    row in (pointB.first..pointA.first)
            }.count() +
            emptyCols.filter { col ->
                col in (pointA.second..pointB.second) ||
                    col in (pointB.second..pointA.second)
            }.count()
    }.sum().let { doubledResult -> doubledResult / 2 }.let { result -> println(result) }
}
