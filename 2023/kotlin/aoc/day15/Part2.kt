import java.io.File

typealias Lens = Pair<String, Int>

fun hash(s: String): Int =
    s.fold(0) { acc, it ->
        (17 * (acc + it.code)).mod(256)
    }

fun <T> List<T>.indexOfFirstOrNull(predicate: ((T) -> Boolean)): Int? = this.indexOfFirst(predicate).takeIf { it >= 0 }

fun main() {
    val boxes = List(256) { mutableListOf<Lens>() }

    File("input.txt").readText().trim().split(",").forEach { s ->
        if (s.endsWith("-")) {
            val label = s.dropLast(1)
            val box = boxes[hash(label)]
            box.indexOfFirstOrNull { it.first == label }?.let { index ->
                box.removeAt(index)
            }
        } else {
            val (label, lengthString) = s.split("=")
            val length = lengthString.toInt()
            val lens = Lens(label, length)
            val box = boxes[hash(label)]
            box.indexOfFirstOrNull { it.first == label }?.let { index ->
                box[index] = lens
            } ?: box.add(lens)
        }
    }
    boxes.flatMapIndexed { boxIndex, box ->
        box.mapIndexed { slotIndex, lens ->
            (boxIndex + 1) * (slotIndex + 1) * lens.second
        }
    }.sum().let { result -> println(result) }
}
