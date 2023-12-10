typealias Coordinate = Pair<Int, Int>
typealias DeltaCoordinate = Pair<Int, Int>

enum class Direction(val delta: DeltaCoordinate) {
    NORTH(DeltaCoordinate(-1, 0)),
    SOUTH(DeltaCoordinate(1, 0)),
    EAST(DeltaCoordinate(0, 1)),
    WEST(DeltaCoordinate(0, -1)),
}

enum class Connector(val glyph: Char, val directions: Set<Direction>) {
    UNKNOWN('S', setOf(Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST)),
    NONE('.', setOf()),
    NORTH_SOUTH('|', setOf(Direction.NORTH, Direction.SOUTH)),
    EAST_WEST('-', setOf(Direction.EAST, Direction.WEST)),
    NORTH_EAST('L', setOf(Direction.NORTH, Direction.EAST)),
    NORTH_WEST('J', setOf(Direction.NORTH, Direction.WEST)),
    SOUTH_WEST('7', setOf(Direction.SOUTH, Direction.WEST)),
    SOUTH_EAST('F', setOf(Direction.SOUTH, Direction.EAST)),
    ;

    companion object {
        val lookup: Map<Char, Connector> = Connector.values().associateBy { it.glyph }
    }
}

typealias WorldMap = Map<Coordinate, Connector>

operator fun Coordinate.plus(delta: DeltaCoordinate): Coordinate {
    val (row, col) = this
    val (dRow, dCol) = delta
    return Coordinate(row + dRow, col + dCol)
}

fun WorldMap.neighbors(coordinate: Coordinate): Set<Coordinate> =
    this[coordinate]!!.directions.map { direction ->
        coordinate + direction.delta
    }.filter {
        this[it] != null &&
            this[it] != Connector.NONE
    }.toSet()

fun WorldMap.loopThrough(coordinate: Coordinate): Set<Coordinate>? {
    val visited = mutableSetOf(coordinate)
    var prev = coordinate
    var curr = this.neighbors(coordinate).firstOrNull() ?: return null
    if (!this.neighbors(curr).contains(prev)) {
        return null
    }

    while (true) {
        visited.add(curr)
        // I have a neighbor that is not the previous node, or there is no possible loop.
        val next = this.neighbors(curr).firstOrNull { it != prev } ?: return null
        when {
            // I am my neighbor's neighbor, or there is no possible loop.
            !this.neighbors(next).contains(curr) -> return null
            // My neighbor is the desired coordinate, so the loop is complete.
            next == coordinate -> return visited
            // My neighbor is not the desired coordinate but is part of a smaller loop.
            visited.contains(next) -> return null
        }
        prev = curr
        curr = next
    }
}

fun main() {
    val world: WorldMap =
        System.`in`.bufferedReader().lineSequence().flatMapIndexed { row, line ->
            line.trim().mapIndexed { col, char ->
                Pair(Coordinate(row, col), Connector.lookup[char]!!)
            }
        }.toMap()

    val start = world.entries.first { it.value == Connector.UNKNOWN }.key

    setOf(
        Connector.NORTH_SOUTH,
        Connector.NORTH_WEST,
        Connector.NORTH_EAST,
        Connector.EAST_WEST,
        Connector.SOUTH_EAST,
        Connector.SOUTH_WEST,
    ).firstNotNullOf { connector ->
        val newWorld =
            world.mapValues {
                when (it.value) {
                    Connector.UNKNOWN -> connector else -> it.value
                }
            }
        val loop = newWorld.loopThrough(start)
        when (loop) {
            null -> null
            else -> Pair(newWorld, loop)
        }
    }.let { (newWorld, loop) ->
        val maxRow = newWorld.keys.maxOf { it.first }
        val maxCol = newWorld.keys.maxOf { it.second }
        val inOrOut = mutableMapOf<Coordinate, Int>()
        (0..maxRow).forEach { row ->
            var sum = 0
            var s = ""
            (0..maxCol).forEach { col ->
                val coordinate = Coordinate(row, col)
                if (loop.contains(coordinate)) {
                    sum +=
                        when (newWorld[coordinate]!!) {
                            Connector.EAST_WEST -> 0
                            Connector.NORTH_EAST -> 0
                            Connector.NORTH_WEST -> 0
                            else -> 1
                        }
                    inOrOut[coordinate] = 2
                } else {
                    inOrOut[coordinate] = sum.mod(2)
                }
                s += inOrOut[coordinate]!!.toString()
            }
            //println(s)
        }

        inOrOut.values.count { it == 1 }.let { result -> println(result) }
    }
}
