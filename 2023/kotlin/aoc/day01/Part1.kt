fun main() {
    System.`in`.bufferedReader().lineSequence().sumOf { line ->
        line
            .filter { c -> c.isDigit() }
            .let { digits -> "${digits.first()}${digits.last()}" }
            .toInt()
    }.let { result: Int ->
        println(result)
    }
}
