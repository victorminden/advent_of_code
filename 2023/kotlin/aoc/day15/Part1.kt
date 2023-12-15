import java.io.File

fun hash(s: String): Int =
    s.fold(0) { acc, it ->
        (17 * (acc + it.code)).mod(256)
    }

fun main() {
    File("input.txt").readText().trim().split(",").map {
        hash(it)
    }.sum().let { result -> println(result) }
}
