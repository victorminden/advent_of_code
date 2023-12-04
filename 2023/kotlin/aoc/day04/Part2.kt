fun main() {
    val winCounts =
        System.`in`.bufferedReader().lineSequence().map { line ->
            val (winning, seen) =
                line.trim().split(": ")[1].split(" | ").map { numberString ->
                    numberString.trim().split("\\s+".toRegex()).map {
                        it.toInt()
                    }.toSet()
                }
            winning.intersect(seen).size
        }.toList().reversed()

    val generatedCards = MutableList(winCounts.size) { _ -> 0 }

    (0 until winCounts.size).sumOf { i ->
        generatedCards[i] = winCounts[i]
        (0 until winCounts[i]).forEach { j ->
            generatedCards[i] = generatedCards[i] + generatedCards[i - j - 1]
        }
        1 + generatedCards[i]
    }.let { result ->
        println(result)
    }
}
