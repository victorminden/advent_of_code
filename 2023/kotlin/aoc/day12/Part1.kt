fun String.toChunkList(): List<Int> = this.split("\\.+".toRegex()).map { it.count() }

fun String.isComplete(): Boolean = this.count { it == '?' } == 0

fun String.matchesCounts(counts: List<Int>): Boolean =
    when {
        !this.isComplete() -> false
        else -> this.trim('.').toChunkList() == counts
    }

fun countArrangements(
    glyphs: String,
    counts: List<Int>,
    remaining: Int,
): Int {
    when {
        remaining == 0 && glyphs.replace('?', '.').matchesCounts(counts) -> return 1
        remaining == 0 || glyphs.isComplete() -> return 0
    }

    return countArrangements(glyphs.replaceFirst('?', '.'), counts, remaining) +
        countArrangements(glyphs.replaceFirst('?', '#'), counts, remaining - 1)
}

fun main() {
    System.`in`.bufferedReader().lineSequence().map { line ->
        val (glyphs, counts) = line.trim().split(' ')
        Pair(glyphs, counts.split(',').map { it.toInt() })
    }.toList().sumOf { (glyphs, counts) ->
        val missingGlyphCount = counts.sum() - glyphs.count { it == '#' }
        countArrangements(glyphs, counts, missingGlyphCount)
    }.let { result -> println(result) }
}
