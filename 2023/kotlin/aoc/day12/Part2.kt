fun Boolean.toInt() = if (this) 1 else 0

fun countArrangements(
    glyphs: String,
    counts: List<Int>,
    currentCount: Int = 0,
): Int {
    if (glyphs.count() == 0) {
        return when (counts.count()) {
            0 -> 1
            1 -> (counts[0] == currentCount).toInt()
            else -> 0
        }
    }
    if (counts.count() == 0) {
        return (!glyphs.any { it == '#' }).toInt()
    }

    val head = glyphs.take(1)
    val tail = glyphs.drop(1)

    if (head == "#") {
        // Add to current (possibly empty) group.
        // If it is too big, there are no solutions.
        val newCount = currentCount + 1
        if (newCount > counts[0]) return 0
        return countArrangements(tail, counts, newCount)
    }

    if (head == ".") {
        // If we are not closing a group, just keep going.
        if (currentCount == 0) return countArrangements(tail, counts, 0)
        // Otherwise, if we closed a group of the wrong size, there are no solutions.
        if (currentCount != counts[0]) return 0
        return countArrangements(tail, counts.drop(1), 0)
    }

    return countArrangements("." + tail, counts, currentCount) +
        countArrangements("#" + tail, counts, currentCount)
}

fun main() {
    System.`in`.bufferedReader().lineSequence().map { line ->
        val (glyphs, counts) = line.trim().split(' ')
        Pair(glyphs, counts.split(',').map { it.toInt() })
    }.toList().sumOf { (glyphs, counts) ->
        countArrangements(glyphs + "?" + glyphs + "?" + glyphs + "?" + glyphs + "?" + glyphs, 
        counts + counts + counts + counts + counts).also{println(it)}
    }.let { result -> println(result) }
}
