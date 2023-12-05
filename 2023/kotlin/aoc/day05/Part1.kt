import java.io.File

fun main() {
    val chunks = File("input.txt").readText().split("\n\n")
    val seedChunk = chunks[0]
    val mapChunks = chunks.drop(1)

    val seeds = seedChunk.split(": ")[1].split(" ").map { it.toLong() }
    val maps =
        mapChunks.map { chunk ->
            chunk.trim().split("\n").drop(1).map { line ->
                line.split(" ").map { it.toLong() }
            }
        }

    seeds.minOf { seed ->
        var x = seed
        maps.forEach { m ->
            m.firstOrNull { (_, inStart, length) ->
                x >= inStart && x < inStart + length
            }?.let { (outStart, inStart, _) ->
                x = outStart + x - inStart
            }
        }
        x
    }.let { result -> println(result) }
}
