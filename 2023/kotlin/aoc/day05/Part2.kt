import java.io.File

fun main() {
    val chunks = File("input.txt").readText().split("\n\n")
    val seedChunk = chunks[0]
    val mapChunks = chunks.drop(1)

    val seeds = seedChunk.split(": ")[1].split(" ").map { it.toLong() }.chunked(2)
    val maps =
        mapChunks.map { chunk ->
            chunk.trim().split("\n").drop(1).map { line ->
                line.split(" ").map { it.toLong() }
            }
        }

    (1..100000000).firstOrNull { i ->
        var x = i.toLong()
        maps.asReversed().forEach { m ->
            m.firstOrNull { (outStart, _, length) ->
                x >= outStart && x < outStart + length
            }?.let { (outStart, inStart, _) ->
                x = inStart + x - outStart
            }
        }
        seeds.any { (start, length) ->
            x >= start && x < start + length
        }
    }?.let { result -> println(result) } ?: println("Try a bigger loop")
}
