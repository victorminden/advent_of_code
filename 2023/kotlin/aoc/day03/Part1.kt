fun main() {
    val paddedLines =
        System.`in`.bufferedReader().lineSequence().map { line ->
            ".${line.trim()}."
        }.toList().let { lines ->
            val n = lines[0].length
            listOf(".".repeat(n)) + lines + listOf(".".repeat(n))
        }
    var result = 0
    paddedLines.windowed(3).forEach { (prev, curr, next) ->
        var partNumber = 0
        var looksGood = false
        for (index in 1 until curr.length - 1) {
            val c = curr[index]
            if (!c.isDigit()) {
                looksGood = false
                partNumber = 0
                continue
            }
            partNumber = 10 * partNumber + c.digitToInt()
            val neighborhood =
                prev.slice(index - 1..index + 1) +
                    curr.slice(index - 1..index + 1) +
                    next.slice(index - 1..index + 1)
            looksGood = looksGood || neighborhood.any { !it.isDigit() && it != '.' }
            if (!curr[index + 1].isDigit() && looksGood) {
                result += partNumber
            }
        }
    }

    println(result)
}
