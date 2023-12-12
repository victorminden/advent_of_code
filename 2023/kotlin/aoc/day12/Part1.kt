fun String.toChunkList(): List<Int> = this.split("\\.+".toRegex()).map { it.count() }

fun String.isComplete(): Boolean = this.count { it == '?' } == 0

fun String.matchesCounts(counts: List<Int>): Boolean =
    when {
        !this.isComplete() -> false
        else -> this.trim('.').toChunkList() == counts
    }

typealias Key = Triple<String, List<Int>, Int>

val memoPad = mutableMapOf<Key, Int>()

fun countArrangements(
    glyphs: String,
    counts: List<Int>,
    remaining: Int,
): Int {
    val key = Triple(glyphs, counts, remaining)

    fun Int.memoize() = this.also { memoPad[key] = it }
    when {
        memoPad[key] != null -> return memoPad[key]!!
        remaining == 0 && glyphs.replace('?', '.').matchesCounts(counts) -> return 1.memoize()
        remaining == 0 || glyphs.isComplete() -> return 0.memoize()
    }

    return (
        countArrangements(glyphs.replaceFirst('?', '.'), counts, remaining) +
            countArrangements(glyphs.replaceFirst('?', '#'), counts, remaining - 1)
    ).memoize()
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
