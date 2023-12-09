enum class Card {
    ACE,
    KING,
    QUEEN,
    TEN,
    NINE,
    EIGHT,
    SEVEN,
    SIX,
    FIVE,
    FOUR,
    THREE,
    TWO,
    JOKER,
}

enum class HandType {
    FIVE_OF_A_KIND,
    FOUR_OF_A_KIND,
    FULL_HOUSE,
    THREE_OF_A_KIND,
    TWO_PAIR,
    ONE_PAIR,
    HIGH_CARD,
}

data class Hand(val hand: List<Card>, val type: HandType, val bet: Int)

fun handToType(hand: String): HandType {
    val countsMap = hand.groupingBy { it }.eachCount()
    val jokersCount = countsMap['J'] ?: 0
    if (jokersCount == 5) {
        return HandType.FIVE_OF_A_KIND
    }
    val counts =
        countsMap.mapNotNull { (char, count) ->
            when (char) {
                'J' -> null
                else -> count
            }
        }.sortedDescending().mapIndexed { index, count ->
            when (index) {
                0 -> count + jokersCount
                else -> count
            }
        }
    return when {
        counts.contains(5) -> HandType.FIVE_OF_A_KIND
        counts.contains(4) -> HandType.FOUR_OF_A_KIND
        counts.contains(3) && counts.contains(2) -> HandType.FULL_HOUSE
        counts.contains(3) -> HandType.THREE_OF_A_KIND
        counts.count { it == 2 } == 2 -> HandType.TWO_PAIR
        counts.contains(2) -> HandType.ONE_PAIR
        else -> HandType.HIGH_CARD
    }
}

fun handToCardList(hand: String): List<Card> =
    hand.map { it ->
        when (it) {
            'A' -> Card.ACE
            'K' -> Card.KING
            'Q' -> Card.QUEEN
            'J' -> Card.JOKER
            'T' -> Card.TEN
            '9' -> Card.NINE
            '8' -> Card.EIGHT
            '7' -> Card.SEVEN
            '6' -> Card.SIX
            '5' -> Card.FIVE
            '4' -> Card.FOUR
            '3' -> Card.THREE
            '2' -> Card.TWO
            else -> throw IllegalArgumentException("ruh roh: $it")
        }
    }

fun parse(
    hand: String,
    bet: String,
) = Hand(handToCardList(hand), handToType(hand), bet.toInt())

fun main() {
    System.`in`.bufferedReader().lineSequence().map { line ->
        val (hand, bet) = line.trim().split(" ")
        parse(hand, bet)
    }.sortedWith(
        compareBy(Hand::type, { it.hand[0] }, { it.hand[1] }, { it.hand[2] }, { it.hand[3] }, { it.hand[4] }),
    ).toList().reversed()
        .mapIndexed { index, hand ->
            (index + 1) * hand.bet
        }.sum().let { result -> println(result) }
}
