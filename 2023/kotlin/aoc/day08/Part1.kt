import java.io.File

fun main() {
    val (steps, pairs) = File("input.txt").readText().split("\n\n")
    val stateMap =
        pairs.trim().split("\n").associate { line ->
            val (key, ps) = line.split(" = (")
            val (left, right) = ps.split(", ")
            val right2 = right.take(3)
            key to Pair(left, right2)
        }
    var curr = "AAA"
    var count = 0
    while (curr != "ZZZ") {
        for (step in steps.trim()) {
            val d =
                if (step == 'R') {
                    1
                } else {
                    0
                }
            curr = stateMap[curr]!!.toList()[d]
            count += 1
            if (curr == "ZZZ") {
                break
            }
        }
    }
    println(count)
}
