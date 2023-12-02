import kotlin.math.max

typealias GameId = Int

data class SetSignature(val redCount: Int, val greenCount: Int, val blueCount: Int)

typealias Game = List<SetSignature>

fun parseGameId(s: String): GameId = s.split(" ").getOrNull(1)?.toInt() ?: throw IllegalStateException("ruh roh!")

fun parseGame(s: String): Game =
    s.split("; ").map { setString ->
        val colorToCount =
            setString.split(", ").associate { countColorString ->
                val (countString, color) = countColorString.split(" ")
                color to countString.toInt()
            }
        SetSignature(
            redCount = colorToCount["red"] ?: 0,
            greenCount = colorToCount["green"] ?: 0,
            blueCount = colorToCount["blue"] ?: 0,
        )
    }

fun reduceGame(game: Game): SetSignature =
    game.reduce { acc, element ->
        SetSignature(
            redCount = max(acc.redCount, element.redCount),
            greenCount = max(acc.greenCount, element.greenCount),
            blueCount = max(acc.blueCount, element.blueCount),
        )
    }

fun main() {
    val games: Map<GameId, Game> =
        System.`in`.bufferedReader().lineSequence().associate { line ->
            val (gameIdString, gameString) = line.trim().split(": ")
            parseGameId(gameIdString) to parseGame(gameString)
        }

    games.values.map { game ->
        with(reduceGame(game)) {
            redCount * greenCount * blueCount
        }
    }.sum().let { result: Int ->
        println(result)
    }
}
