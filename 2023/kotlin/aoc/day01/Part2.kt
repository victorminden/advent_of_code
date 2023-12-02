fun main() {
    System.`in`.bufferedReader().lineSequence().sumOf { line ->
        line
            .replace("one", "one1one")
            .replace("two", "two2two")
            .replace("three", "three3three")
            .replace("four", "four4four")
            .replace("five", "five5five")
            .replace("six", "six6six")
            .replace("seven", "seven7seven")
            .replace("eight", "eight8eight")
            .replace("nine", "nine9nine")
            .filter { c -> c.isDigit() }
            .let { digits -> "${digits.first()}${digits.last()}" }
            .toInt()
    }.let { result: Int ->
        println(result)
    }
}
